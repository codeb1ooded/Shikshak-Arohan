$(function() {
    var $to, $from;
    $( ".calendar" ).datepicker({
        dateFormat: 'dd/mm/yy',
        firstDay: 1
    });

    $(document).on('click', '.date-picker .input', function(e){
        var $me = $(this),
                $parent = $me.parents('.date-picker');
        $parent.toggleClass('open');
    });

    $(".calendar-to").on("change",function(){
        var $me = $(this),
                $selected = $me.val(),
                $parent = $me.parents('.date-picker');
        $parent.find('.result').children('span').html($selected);
        $to = $selected;
        $("#apply-button").attr("href", "{{ url }}" + "&to=" + $to + "&from=" + $from);
    });

    $(".calendar-from").on("change",function(){
        var $me = $(this),
                $selected = $me.val(),
                $parent = $me.parents('.date-picker');
        $parent.find('.result').children('span').html($selected);
        $from = $selected;
        $("#apply-button").attr("href", "{{ url }}" + "&to=" + $to + "&from=" + $from);
    });
});
