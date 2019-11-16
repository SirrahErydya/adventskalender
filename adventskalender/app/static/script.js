var csrf_token_name = "csrfmiddlewaretoken";

function open_window(window_id) {
    var csrf_token = $('input[name="'+csrf_token_name+'"]').attr('value');
    var data = JSON.stringify({'day': window_id});
    $.ajaxSetup({
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrf_token);
        }
    });
    $.ajax({
        url: '/app/open',
        data: data,
        dataType: 'json',
        method: 'POST',
        async: false
      });
    document.location.reload(false)
}

function show_img(window_id) {
    var csrf_token = $('input[name="'+csrf_token_name+'"]').attr('value');
    var data = JSON.stringify({'day': window_id});
    var modal = document.getElementById('modal');
    var img = document.getElementById('loot');
    var caption = document.getElementById('caption');

    modal.style.display = 'block';
    caption.innerHTML = '<h1>' + window_id.toString() + '. Dezember</h1>';

    $.ajaxSetup({
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrf_token);
        }
    });
    $.ajax({
        url: '/app/show',
        data: data,
        dataType: 'json',
        method: 'POST',
        async: false,
        success: function (data) {
            img.src = data.url;
            caption.innerHTML += '<p>' + data.descr + '</p>';
        }
      });
}

function close_modal() {
    var modal = document.getElementById('modal');
    modal.style.display = 'none';
}