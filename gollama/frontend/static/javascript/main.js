$(document).ready(function () {
    $('#search').on('keyup', function (e) {
        if (e.which == 13) {
            console.log('enter key pressed')
            $('[name="shorthand_row"]').hide('slow', () => {
                // TODO not sure why this callback is not triggering
                $(`[name="shorthand_row"]:contains("${$(this).val()}")`).show('slow')
            })
            $(`[name="shorthand_row"]:contains("${$(this).val()}")`).show('slow')
        }
    })
});
