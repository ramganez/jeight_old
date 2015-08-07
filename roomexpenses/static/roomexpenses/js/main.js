$(document).ready(function(){
     // your javascript here
    alert("welcome!!")
    $('#id_ready_to_share').change(function() {
    $(this).val() == 'something' ? $('#id_area').hide() : $('#id_area').show();
    alert( "hello world!!" );
});
});

