function get_hash_params() {
    let hash_string = window.location.hash.substr(1)
    let components = hash_string.split('&')
    let keys = {}
    for (const component in components) {
        let kv_pair = components[component].split('=')
        if (kv_pair[0].length) {
            keys[kv_pair[0]] = kv_pair[1]
        }
    }
    return keys
}


function set_event_listener() {
    //change enter button to submit form

    $('#shorthand,#url').keypress(function (event) {
        if (event.key === "Enter") {
            $('#create-button').click()
        }
    });

    //create button
    $('#create-button').on('click', function () {
        $("#create-form").validate()
        if ($('#shorthand').valid() && $('#url').valid()) {
            post_shorthand({'label': $('#shorthand').val(), 'url': $('#url').val()}).done(() => {
                location.reload()
            })
        }
    })
}

$(document).ready(function () {
    $('#search').on('keyup', function (e) {
        if (e.which == 13) {
            $('[name="shorthand_row"]').hide('slow', () => {
                // TODO not sure why this callback is not triggering
                $(`[name="shorthand_row"]:contains("${$(this).val()}")`).show('slow')
            })
            $(`[name="shorthand_row"]:contains("${$(this).val()}")`).show('slow')
        }
    })

    // This is the code to initialise pulling fragment components
    let hash_params = get_hash_params()
    if (Object.keys(hash_params).length != 0) {
        $('#shorthand').val(hash_params['new'])
        $('#url').focus()
    }

    set_event_listener();
});
