// static/js/upload_progress.js

$(document).ready(function() {
    $('#uploadForm').on('submit', function(e) {
        e.preventDefault();
        var formData = new FormData(this);
        $('#progressBarContainer').show();
        $.ajax({
            xhr: function() {
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener('progress', function(evt) {
                    if (evt.lengthComputable) {
                        var percentComplete = (evt.loaded / evt.total) * 100;
                        $('#progressBar').css('width', percentComplete + '%');
                        $('#progressStatus').html(percentComplete.toFixed(2) + '%');
                    }
                }, false);
                return xhr;
            },
            type: 'POST',
            url: $(this).attr('action'),
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                $('#progressBar').css('width', '100%');
                $('#progressStatus').html('100%');
                setTimeout(function() {
                    $('#progressBarContainer').hide();
                }, 1000);
                // Handle success response
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
                // Handle error response
            }
        });
    });
});
