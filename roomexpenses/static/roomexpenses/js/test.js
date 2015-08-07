$(document).ready(function(){
    alert('welcome!!')
    $('#id_ready_to_share').change(function() {
    alert( this.value );
    var opt = $(this).val();
    opt == 'xxx' ? $('#id_x_field').show() : $('#id_x_field').hide();
    alert( "hello world!!" );
    });
    });

