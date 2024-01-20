document.addEventListener('DOMContentLoaded', function () {
    const image1Input = document.getElementById('image1');
    const image2Input = document.getElementById('image2');
    const preview1 = document.getElementById('preview1');
    const preview2 = document.getElementById('preview2');

    image1Input.addEventListener('change', function () {
        previewImage(this, preview1);
    });

    image2Input.addEventListener('change', function () {
        previewImage(this, preview2);
    });

    function previewImage(input, preview) {
        const file = input.files[0];

        if (file) {
            const reader = new FileReader();

            reader.onload = function (e) {
                preview.src = e.target.result;
            };

            reader.readAsDataURL(file);
        }
    }
});
