document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        // Lógica para procesar el formulario
        var mensajeElement = document.querySelector('#mensaje');
        var rutaElement = document.querySelector('#ruta');

        // Simulación de una solicitud de muestra
        var mensaje = "Descarga exitosa";
        var ruta = "/ruta/del/video.mp4";

        // Actualiza la interfaz con el mensaje y la ruta obtenidos.
        if (mensaje) {
            mensajeElement.textContent = mensaje;

            if (ruta) {
                rutaElement.textContent = "Video guardado en: " + ruta;
            }
        }
    });
});
