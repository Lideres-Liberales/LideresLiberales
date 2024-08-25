const redirect = (url) => window.location.href = url;

const validationMessages = {
    en: {
        valueMissing: "This field is required.",
        typeMismatch: "Please enter a valid value.",
        tooShort: "This field is too short.",
        tooLong: "This field is too long.",
        rangeUnderflow: "The value is too low.",
        rangeOverflow: "The value is too high.",
        patternMismatch: "The value does not match the required pattern."
    },
    es: {
        valueMissing: "Este campo es obligatorio.",
        typeMismatch: "Por favor, introduce un valor válido.",
        tooShort: "Este campo es demasiado corto.",
        tooLong: "Este campo es demasiado largo.",
        rangeUnderflow: "El valor es demasiado bajo.",
        rangeOverflow: "El valor es demasiado alto.",
        patternMismatch: "El valor no coincide con el patrón requerido."
    }
};

class ValidationTranslator {
    constructor(language = "en") {
        this.language = language;
    }

    setLanguage(lang) {
        if (validationMessages[lang]) {
            this.language = lang;
        } else {
            console.warn(`Idioma ${lang} no soportado.`);
        }
    }

    translate(validationType, attributes = {}) {
        const messages = validationMessages[this.language];
        let message = messages[validationType];

        if (!message) {
            console.warn(`Tipo de validación ${validationType} no soportado.`);
            return;
        }

        for (const [key, value] of Object.entries(attributes)) {
            const placeholder = `{${key}}`;
            if (message.includes(placeholder)) {
                message = message.replace(placeholder, value);
            }
        }

        return message;
    }


    errorType(input) {
        const validity = input.validity;
        let errorType;

        if (validity.valueMissing) errorType = "valueMissing";
        else if (validity.typeMismatch) errorType = "typeMismatch";
        else if (validity.tooShort) errorType = "tooShort";
        else if (validity.tooLong) errorType = "tooLong";
        else if (validity.rangeUnderflow) errorType = "rangeUnderflow";
        else if (validity.rangeOverflow) errorType = "rangeOverflow";
        else if (validity.patternMismatch) errorType = "patternMismatch";

        return errorType;
    }
}

class FormValidator {
    constructor({formId, validationTranslator}) {
        this.translator = validationTranslator;
        this.form = document.querySelector(`#${formId}`);

        if (!this.form) {
            throw new Error(`No se encontró el formulario con ID ${formId}`);
        }

        this.inputs = this.form.querySelectorAll("input, textarea, select");
        this.inputsErrors = new Map();
        this.init();
    }

    checked(input) {
        let inputsError = this.inputsErrors.get(`#${input.id}_error`);

        if (input.checkValidity()) {
            input.classList.remove("is-invalid");

            if (inputsError) {
                inputsError.textContent = "";
            }

        } else {
            input.classList.add("is-invalid");

            if (inputsError) {
                let errorType = this.translator.errorType(input);
                let message = this.translator.translate(errorType);

                inputsError.textContent = message;
            }
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
