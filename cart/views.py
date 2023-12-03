from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404, _get_queryset
from .models import *
from django.http import Http404, HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import requests

def index(request):
    data = {'products': Product.objects.all(),
            'cart': Cart.objects.all()}
    return render(request, 'index.html', data)


def buy(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    try:
        one_more = get_object_or_404(Cart, product=item)
        one_more.count += 1
        one_more.total_cost = one_more.count_total_price()
        one_more.save()
    except Http404:
        Cart.objects.create(
            count=1,
            product=item,
            total_cost=item.price
        )
    return redirect('home')


def to_cart(request):
    try:
        data = {'cart': get_list_or_404(Cart),
                'total': sum([item.count_total_price() for item in get_list_or_404(Cart)])}
    except Http404:
        data = {'cart': '',
                'total': 0}
    return render(request, 'cart_page.html', data)


def delete(request, product_id):
    get_object_or_404(Cart, id=product_id).delete()
    return redirect('to_cart')


def delete_all(request):
    [item.delete() for item in get_list_or_404(Cart)]
    return redirect('to_cart')


@method_decorator(csrf_exempt, name='dispatch')
def final_cart(request):
    print(1)
    if request.POST:
        print(request)
        cart: list[Cart] = get_list_or_404(Cart)
        products = ' *** '.join([item.__str__() for item in cart])
        new_order: Order = Order.objects.create(order_list=products, **request.POST)
        new_order.save()
        print(new_order)
        message = f"{new_order}".replace(' *** ', ' ₽\n') + ' ₽'
        send_message(message)
        get_object_or_404(Cart).delete()
        return JsonResponse(data={'message': 'data post success', 'link': '../'})
    return redirect('home')


def send_message(message):
    TOKEN = "6212594744:AAHGswqaPzPw-dvf4JVBypW_rc20l-TKDAY"
    chat_id = "-894979806"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())  # Эта строка отсылает сообщение
