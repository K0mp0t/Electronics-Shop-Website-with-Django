function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
function checkOrder() {
    var data = {};
    //var csrf_token = getCookie('csrftoken');
    var order_nmb = $('#order_nmb_input').val();
    var url = $('#check_order_btn').data('url');
    //data.csrfmiddlewaretoken = csrf_token;
    data.order_nmb = order_nmb;
    $.ajax({
        url: url,
        type: 'get',
        data: data,
        success: function(data) {
            console.log(url);
        }
    });
}

$(document).ready(function(){
    var form = $('#nmb_form');
    form.on('submit', function(e){
        e.preventDefault();
        var product = {};
        product.name = $('#submit-btn').data('product_name');
        product.nmb = Number($('#number').val());
        product.id = $('#submit-btn').data('product_id');
        product.price = $('#submit-btn').data('product_price');
        product.total_price = product.price * product.nmb;
        var data = {};
        var csrf_token = getCookie('csrftoken');
        var url = form.attr("action");
        data.product_id = product.id;
        data.nmb = product.nmb;
        data.csrfmiddlewaretoken = csrf_token;
        data.purpose = '+'; // '+' for add or create, '-' for remove
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data) {
                $('#cart-total-price').text(data.total_price + ' RUB');
                $('#cart-items-nmb').text(data.total_nmb);
                $('.cart').addClass('hidden');
                $('#cart-total-price').removeClass('hidden');
                $('.nmb-container').removeClass('hidden');
            },
        });
    });
    var total_nmb = document.getElementById('cart-items-nmb').innerHTML;
    if (total_nmb == 0) {
        $('.cart').removeClass('hidden');
    } else {
        $('#cart-total-price').removeClass('hidden');
        $('.nmb-container').removeClass('hidden');
    }
});