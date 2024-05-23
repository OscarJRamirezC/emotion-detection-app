$(document).ready(function() {
    $('#upload-form').submit(function(event) {
        event.preventDefault();
        var formData = new FormData();
        formData.append('file', $('#image-upload')[0].files[0]);

        $.ajax({
            url: 'http://localhost:8000/predict-emotion/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                $('#result').text('Detected Emotion: ' + data.emotion);
            },
            error: function() {
                $('#result').text('Error occurred while predicting emotion.');
            }
        });
    });
});
