jQuery.each(['patch', 'delete'], function (i, method) {
    jQuery[method] = function (url, data, callback, type) {
        if (jQuery.isFunction(data)) {
            type = type || callback;
            callback = data;
            data = undefined;
        }

        return jQuery.ajax({
            url: url,
            type: method,
            dataType: type,
            data: data,
            success: callback
        });
    };
});

function csrfIgnoreMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    function(xhr, settings) {
        if (!csrfIgnoreMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken)
        }
    }
})

function get_shorthands() {
    return $.get('/api/v1/shorthand/')
}

function post_shorthand(payload) {
    return $.post('/api/v1/shorthand/', payload)
}

function patch_shorthand(id, payload) {
    return $.patch(`/api/v1/shorthand/${id}/`, payload)
}

function delete_shorthand(id) {
    return $.delete(`/api/v1/shorthand/${id}/`)
}

