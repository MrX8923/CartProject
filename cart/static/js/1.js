$(document).ready(function () {
    $('#result').hide()
})

$('#final').click(function () {
    $('#result').show()
})

$('#sub-button').click(function () {
    $.ajax(
        '/cart/final/',
        {
            method: 'POST',
            data: {
                'address': $('#address').val(),
                'name': $('#name').val(),
                'tel': $('#ph-number').val(),
            },
            success: function (response) {
                console.log(response.message)
                window.location.href = response.link
            },
            error: function (response) {
                console.log(response)
            }
        }
        )
})
