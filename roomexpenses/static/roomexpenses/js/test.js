$(document).ready(function(){
    //alert('welcome!!')
    $('#id_ready_to_share').change(function() {
    //alert( this.value );
    var opt = $(this).val();

    opt == 'some_amount' ? $('#some_amount').show() : $('#some_amount').hide();
    //alert( "hello world!!" );
    });
    });

