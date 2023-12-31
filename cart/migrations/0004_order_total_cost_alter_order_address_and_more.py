# Generated by Django 4.2.7 on 2023-11-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_cost',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_list',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='tel',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
