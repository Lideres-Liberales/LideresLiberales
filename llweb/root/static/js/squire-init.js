class Compare {
    constructor() {
        this.__node__ = null;
        this.__font__ = null;
        this.__class__ = null;
        this.__color__ = null;
        this.__align__ = null;
    }

    hexToRgb(hex) {
        let r = 0, g = 0, b = 0;
        if (hex.length === 7) { // #RRGGBB
            [r, g, b] = [1, 3, 5].map(i => parseInt(hex.slice(i, i + 2), 16));
        } else if (hex.length === 4) { // #RGB
            [r, g, b] = [1, 2, 3].map(i => parseInt(hex[i] + hex[i], 16));
        }
        return `rgb(${r}, ${g}, ${b})`;
    }

    node(node) { this.__node__ = node; return this; }
    font(font) { this.__font__ = font; return this; }
    color(color) { this.__color__ = this.hexToRgb(color); return this; }
    align(align) { this.__align__ = align; return this; }
    class_(class_) { this.__class__ = class_; return this; }

    build() {
        return (node) => {
            return (
                node.nodeName === this.__node__ &&
                node.classList.contains(this.__class__) &&
                (this.__color__ === null || node.style.color === this.__color__) &&
                (this.__font__ === null || node.style.fontSize === this.__font__) &&
                (this.__align__ === null || node.style.textAlign === this.__align__)
            );
        };
    }
}

class TextEditor {
    colorRules = [
        { 'id': '#sq-color1', 'tag': 'c1', 'color': '#dc3545' },
        { 'id': '#sq-color2', 'tag': 'c2', 'color': '#ffc107' },
        { 'id': '#sq-color3', 'tag': 'c3', 'color': '#28a745' },
        { 'id': '#sq-color4', 'tag': 'c4', 'color': '#007bff' },
        { 'id': '#sq-color5', 'tag': 'c5', 'color': '#6c757d' },
        { 'id': '#sq-color6', 'tag': 'c6', 'color': '#fd7e14' }
    ];

    fonfRules = [
        { 'id': '#sq-heading1', 'tag': 'z1', 'font': '3.7em' },
        { 'id': '#sq-heading2', 'tag': 'z2', 'font': '3.1em' },
        { 'id': '#sq-heading3', 'tag': 'z3', 'font': '2.6em' },
        { 'id': '#sq-heading4', 'tag': 'z4', 'font': '2.2em' },
        { 'id': '#sq-heading5', 'tag': 'z5', 'font': '1.8em' },
        { 'id': '#sq-heading6', 'tag': 'z6', 'font': '1.5em' },
        { 'id': '#sq-heading7', 'tag': 'z7', 'font': '1.2em' },
        { 'id': '#sq-heading8', 'tag': 'z8', 'font': '1.2em' },
    ];

    alignRules = [
        { 'id': '#sq-alignLeft', 'action': 'alignLeft', 'tag': 'al', 'class_': 'align-left', 'align': 'left' },
        { 'id': '#sq-alignCenter', 'action': 'alignCenter', 'tag': 'ac', 'class_': 'align-center', 'align': 'center' },
        { 'id': '#sq-alignRight', 'action': 'alignRight', 'tag': 'ar', 'class_': 'align-right', 'align': 'right' },
    ]

    constructor(containerSelector, textareaSelector, toolsBarSelector) {
        this.container = document.querySelector(containerSelector);
        this.textarea = document.querySelector(textareaSelector);
        this.toolsBar = document.querySelector(toolsBarSelector);

        if (this.container && this.textarea && this.toolsBar) {
            if (typeof Squire !== 'undefined' && typeof TurndownService !== 'undefined') {
                this.initializeEditor();
                this.bindEvents();
            }
        } else {
            console.error("No element was defined for the editor to inject to.");
        }
    }

    initializeEditor() {
        this.editor = new Squire(this.container, { blockTag: 'P' });
        this.parser = new TurndownService();

        if (this.textarea && this.textarea.value) {
            this.editor.setHTML(this.textarea.value);
            this.syncContent();
        }

        this.listenEvents();
        this.addPatterns();
    }

    addPatterns() {
        this.parser.addRule('underline', {
            filter: (node) => node.nodeName === 'U',
            replacement: (content) => `[u]${content}[/u]`
        });

        this.colorRules.forEach(rule => {
            this.parser.addRule(rule.id, {
                'filter': new Compare().node('SPAN').class_('color').color(rule.color).build(),
                'replacement': (content) => `[${rule.tag}]${content}[/${rule.tag}]`
            });
        });

        this.fonfRules.forEach(rule => {
            this.parser.addRule(rule.id, {
                'filter': new Compare().node('SPAN').class_('size').font(rule.font).build(),
                'replacement': (content) => `[${rule.tag}]${content}[/${rule.tag}]`
            });
        });

        this.alignRules.forEach(rule => {
            this.parser.addRule(rule.id, {
                'filter': new Compare().node('P').class_(rule.class_).align(rule.align).build(),
                'replacement': (content) => `[${rule.tag}]${content}[/${rule.tag}]`
            });
        });
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
        this.textarea.value = this.parser.turndown(content);
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

        this.fonfRules.forEach(rule => {
            console.log(rule.font)
            this.setFont(rule.id, rule.font);
        });

        this.colorRules.forEach(rule => {
            this.setTextColor(rule.id, rule.color);
        });

        this.alignRules.forEach(rule => {
            this.loadAction(rule.id, rule.action);
        });

        this.loadAction('#sq-undo', 'undo');
        this.loadAction('#sq-redo', 'redo');

        this.loadAction('#sq-removeAllFormatting', 'removeAllFormatting');
        this.loadAction('#sq-makeOrderedList', 'makeOrderedList');

        this.loadAction('#sq-makeHeading', 'makeHeading');
        this.loadAction('#sq-bold', 'bold');
        this.loadAction('#sq-italic', 'italic');
        this.loadAction('#sq-underline', 'underline');
    }
}

new TextEditor('#editor', '.wysiwyg-textarea', '#tool-bar');