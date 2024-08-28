class TextEditor {
    constructor(containerSelector, textareaSelector, toolsBarSelector) {
        this.editor = null;

        this.container = document.querySelector(containerSelector);
        this.textarea = document.querySelector(textareaSelector);
        this.toolsBar = document.querySelector(toolsBarSelector);

        if (this.container && this.textarea && this.toolsBar) {
            if (typeof Squire !== 'undefined') {
                this.initializeEditor();
                this.bindEvents();
            }
        } else {
            console.error("No element was defined for the editor to inject to.");
        }
    }

    initializeEditor() {
        this.editor = new Squire(this.container);

        if (this.textarea && this.textarea.value) {
            this.editor.setHTML(this.textarea.value);
        }

        this.listenEvents();
    }

    listenEvents() {
        // Agregar manejadores de eventos en el editor
        this.editor.addEventListener('input', this.syncContent.bind(this));
        this.editor.addEventListener('keyup', this.syncContent.bind(this));
        this.editor.addEventListener('mousemove', this.syncContent.bind(this));
        this.editor.addEventListener('change', this.syncContent.bind(this));

        // Agregar manejadores para eventos táctiles
        this.editor.addEventListener('touchstart', this.syncContent.bind(this));
        this.editor.addEventListener('touchend', this.syncContent.bind(this));
        this.editor.addEventListener('touchmove', this.syncContent.bind(this));
        this.editor.addEventListener('touchcancel', this.syncContent.bind(this));

        // Agregar manejadores de eventos en el barra de herramientas
        this.toolsBar.addEventListener('click', this.syncContent.bind(this));
        this.toolsBar.addEventListener('dblclick', this.syncContent.bind(this));
        this.toolsBar.addEventListener('mousemove', this.syncContent.bind(this));

        // Agregar manejadores para eventos táctiles
        this.toolsBar.addEventListener('touchstart', this.syncContent.bind(this));
        this.toolsBar.addEventListener('touchend', this.syncContent.bind(this));
        this.toolsBar.addEventListener('touchmove', this.syncContent.bind(this));
        this.toolsBar.addEventListener('touchcancel', this.syncContent.bind(this));
    }

    syncContent() {
        let content = this.editor.getHTML().toString();

        content = content.replace(/<\/div><div>/g, '');
        content = content.replace(/<div><br><\/div>/g, '<br>');

        this.textarea.value = content;
    }

    squireAction(action) {
        const test = {
            value: 'bold',
            testBold: this.editor.testPresenceinSelection('bold', action, 'B', (/>B\b/)),
            testItalic: this.editor.testPresenceinSelection('italic', action, 'I', (/>I\b/)),
            testUnderline: this.editor.testPresenceinSelection('underline', action, 'U', (/>U\b/)),
            testOrderedList: this.editor.testPresenceinSelection('makeOrderedList', action, 'OL', (/>OL\b/)),
            testLink: this.editor.testPresenceinSelection('makeLink', action, 'A', (/>A\b/)),
            testQuote: this.editor.testPresenceinSelection('increaseQuoteLevel', action, 'blockquote', (/>blockquote\b/)),
            isNotValue: (a) => a === action && this.value !== ''
        };

        this.editor.alignRight = () => { this.editor.setTextAlignment('right'); };
        this.editor.alignCenter = () => { this.editor.setTextAlignment('center'); };
        this.editor.alignLeft = () => { this.editor.setTextAlignment('left'); };
        this.editor.alignJustify = () => { this.editor.setTextAlignment('justify'); };
        this.editor.makeHeading = () => { this.editor.setFontSize('2em'); this.editor.bold(); };

        if (test.testBold || test.testItalic || test.testUnderline || test.testOrderedList || test.testLink || test.testQuote) {
            if (test.testBold) this.editor.removeBold();
            if (test.testItalic) this.editor.removeItalic();
            if (test.testUnderline) this.editor.removeUnderline();
            if (test.testLink) this.editor.removeLink();
            if (test.testOrderedList) this.editor.removeList();
            if (test.testQuote) this.editor.decreaseQuoteLevel();
        } else if (test.isNotValue('makeLink') || test.isNotValue('insertImage') || test.isNotValue('selectFont')) {
            // No action required for dropdowns
        } else {
            this.editor[action]();
            this.editor.focus();
        }
    }

    setFont(idButton, fontSize) {
        document.querySelector(idButton)?.addEventListener('click', () => {
            this.editor.setFontSize(fontSize);
        });
    }

    setTextColor(idButton, textColor) {
        document.querySelector(idButton)?.addEventListener('click', () => {
            this.editor.setTextColor(textColor);
        });
    }

    loadAction(idButton, action) {
        document.querySelector(idButton)?.addEventListener('click', () => {
            this.squireAction(action);
        });
    }

    bindEvents() {
        Squire.prototype.testPresenceinSelection = function (name, action, format, validation) {
            const path = this.getPath();
            const test = (validation.test(path) || this.hasFormat(format));
            return name === action && test;
        };

        this.setFont('#sq-heading1', '3.7rem');
        this.setFont('#sq-heading2', '3.1rem');
        this.setFont('#sq-heading3', '2.6rem');
        this.setFont('#sq-heading4', '2.2rem');
        this.setFont('#sq-heading5', '1.8rem');
        this.setFont('#sq-heading6', '1.5rem');
        this.setFont('#sq-heading7', '1.2rem');
        this.setFont('#sq-heading8', '1.0rem');

        this.setTextColor('#sq-color1', '#dc3545');
        this.setTextColor('#sq-color2', '#ffc107');
        this.setTextColor('#sq-color3', '#28a745');
        this.setTextColor('#sq-color4', '#007bff');
        this.setTextColor('#sq-color5', '#6c757d');
        this.setTextColor('#sq-color6', '#fd7e14');

        this.loadAction('#sq-undo', 'undo');
        this.loadAction('#sq-redo', 'redo');

        this.loadAction('#sq-removeAllFormatting', 'removeAllFormatting');
        this.loadAction('#sq-makeOrderedList', 'makeOrderedList');

        this.loadAction('#sq-makeHeading', 'makeHeading');
        this.loadAction('#sq-bold', 'bold');
        this.loadAction('#sq-italic', 'italic');
        this.loadAction('#sq-underline', 'underline');

        this.loadAction('#sq-alignLeft', 'alignLeft');
        this.loadAction('#sq-alignCenter', 'alignCenter');
        this.loadAction('#sq-alignRight', 'alignRight');
    }
}

new TextEditor('#editor', '.wysiwyg-textarea', '#tool-bar');