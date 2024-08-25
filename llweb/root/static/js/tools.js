const redirect = (url) => window.location.href = url;

class FormValidator {
    constructor(formId) {
        this.form = document.querySelector(`#${formId}`);
        if (!this.form) {
            throw new Error(`No se encontró el formulario con ID ${formId}`);
        }
        this.inputs = this.form.querySelectorAll('input, textarea, select');
        this.inputsErrors = new Map();
        this.init();
    }

    checked(input) {
        let inputsError = this.inputsErrors.get(`#${input.id}_error`);

        if (input.checkValidity()) {
            input.classList.remove("is-invalid");
            if (inputsError) inputsError.textContent = "";
        } else {
            input.classList.add("is-invalid");
            if (inputsError) inputsError.textContent = input.validationMessage;
        }
    }

    handleInputChange = (event) => {
        this.checked(event.target);
    }

    init() {
        this.inputs.forEach(input => {
            input.addEventListener("input", this.handleInputChange, false);
            input.addEventListener("blur", this.handleInputChange, false);

            if (input.id) {
                let key = `#${input.id}_error`;
                let value = document.querySelector(key);

                this.inputsErrors.set(key, value);
            }
        });

        this.form.addEventListener("submit", (event) => {
            event.preventDefault();
            this.inputs.forEach(input => { if (input.id) { this.checked(input); } });
            if (this.form.checkValidity()) this.form.submit();
        });
    }
}
