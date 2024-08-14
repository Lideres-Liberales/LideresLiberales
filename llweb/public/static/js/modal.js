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

document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('myModal');
    const modalBody = document.querySelector('#myModal .modal-body');

    const modalXxx = `
        <div class="spinner-border" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    `;

    new bootstrap.Modal(modal, { backdrop: false });
    modalBody.innerHTML = modalXxx;

    modal.addEventListener('shown.bs.modal', async function (event) {
        let body = document.querySelector('body');
        body.removeAttribute('class');
        body.removeAttribute('style');

        modalBody.innerHTML = await fetchData(
            event.relatedTarget.getAttribute('data-url')
        );
    });

    modal.addEventListener('hidden.bs.modal', async function () {
        modalBody.innerHTML = modalXxx;
    });
});
