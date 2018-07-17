function deleteCartItem(id) {
    var data = {};
    var url = $('.delete').data('url');
    var csrf_token = getCookie('csrftoken');
    data.csrfmiddlewaretoken = csrf_token;
    data.purpose = '-';
    data.id = id;
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
        success: function(data) {
            $('#'+data.id).remove();
            var len = document.getElementById('cart-ul').getElementsByTagName('li').length;
            console.log(data.id, len);
            if (len == 0) {
                $('#cart-empty').removeClass('hidden');
                $('#items-container').addClass('hidden');
            }
            $('#cart-total-price').text(data.total_price + ' RUB');
            $('#cart-items-nmb').text(data.total_nmb);
            if (data.total_nmb == 0) {
                $('#cart-total-price').addClass('hidden');
                $('.nmb-container').addClass('hidden');
                $('.cart').removeClass('hidden');
            }
        },
    });
}

function preMakeOrder() {
    var data = {};
    var csrf_token = getCookie('csrftoken');
    data.csrfmiddlewaretoken = csrf_token;
    $('ul.items > li').each(function(){
        var id = this.id;
        var nmb = $(this).find('#'+id).val();
        data[id] = nmb;
    });
    var url = $('#make_order').data('url');
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
    });
}

$(document).ready(function(){
    var len = document.getElementById('cart-ul').getElementsByTagName('li').length;
    if (len == 0) {
        $('#cart-empty').removeClass('hidden');
        $('#items-container').addClass('hidden');
    } else {
        $('#items-container').removeClass('hidden');
        $('#cart-empty').addClass('hidden');
    }
    $(document).on('change', '.nmb-input', function() {
        var total_order_amount = 0;
        var current_li = $(this).closest('li');
        var current_nmb = $(this).val();
        var current_price = parseFloat(current_li.find('#item-price').text()).toFixed(2);
        var total_amount = parseFloat(current_nmb*current_price).toFixed(2);
        current_li.find('.total-amount').text(total_amount);
        $('.total-amount').each(function() {
            total_order_amount = total_order_amount + parseFloat($(this).text());    
        });
        $('#total-order-amount').text(total_order_amount.toFixed(2) + ' RUB');
        $('#cart-total-price').text(total_order_amount.toFixed(2) + ' RUB');
    }); 
});
