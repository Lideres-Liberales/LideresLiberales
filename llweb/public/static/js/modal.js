async function fetchData(url) {
    try {
        let response = await fetch(url);

        if (!response.ok) {
            throw new Error('La respuesta de la red no fue correcta');
        }

        return response.text();
    } catch (error) {
        console.error('Ha habido un problema con tu operación de fetch:', error);
        return 'Error al cargar el contenido';
    }
}

document.addEventListener('shown.bs.modal', async function (event) {
    var button = event.relatedTarget;
    var url = button.getAttribute('data-url');

    var modalTitle = document.getElementById('miModalLabel');
    var modalBody = document.querySelector('#miModal .modal-body');

    modalTitle.textContent = "Título " + url;
    modalBody.innerHTML = await fetchData(url);
});