$(document).ready(function() {
    $('#select-button').click(function() {
        $('#image-upload').click();
    });

    $('#image-upload').change(function() {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('#selected-image').attr('src', e.target.result).show();
        }
        reader.readAsDataURL(this.files[0]);
    });

    $('#upload-form').submit(function(event) {
        event.preventDefault();
        var formData = new FormData();
        var file = $('#image-upload')[0].files[0];

        if (!file) {
            $('#result').text('Por favor, selecciona una imagen.');
            return;
        }

        formData.append('file', file);

        $.ajax({
            url: '/predict-emotion',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                $('#result').text('Emoción detectada: ' + data.emotion);
            },
            error: function() {
                $('#result').text('Ocurrió un error al predecir la emoción.');
            }
        });
    });
});
