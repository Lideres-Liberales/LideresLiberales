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
            r = parseInt(hex.slice(1, 3), 16);
            g = parseInt(hex.slice(3, 5), 16);
            b = parseInt(hex.slice(5, 7), 16);
        } else if (hex.length === 4) { // #RGB
            r = parseInt(hex[1] + hex[1], 16);
            g = parseInt(hex[2] + hex[2], 16);
            b = parseInt(hex[3] + hex[3], 16);
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
    constructor(containerSelector, textareaSelector, toolsBarSelector) {
        this.editor = null;
        this.parser = null;

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
        this.addExtraPattern();
    }

    addExtraPattern() {
        console.log(new Compare().node('SPAN').class_('color').color('#dc3545').build())
        this.parser.addRule('underline', {
            filter: (node) => node.nodeName === 'U',
            replacement: (content) => `[u]${content}[/u]`
        });

        this.parser.addRule('llweb-color1', {
            'filter': new Compare().node('SPAN').class_('color').color('#dc3545').build(),
            'replacement': (content) => `[c1]${content}[/c1]`
        });

        this.parser.addRule('llweb-color2', {
            'filter': new Compare().node('SPAN').class_('color').color('#ffc107').build(),
            'replacement': (content) => `[c2]${content}[/c2]`
        });

        this.parser.addRule('llweb-color3', {
            'filter': new Compare().node('SPAN').class_('color').color('#28a745').build(),
            'replacement': (content) => `[c3]${content}[/c3]`
        });

        this.parser.addRule('llweb-color4', {
            'filter': new Compare().node('SPAN').class_('color').color('#007bff').build(),
            'replacement': (content) => `[c4]${content}[/c4]`
        });

        this.parser.addRule('llweb-color5', {
            'filter': new Compare().node('SPAN').class_('color').color('#6c757d').build(),
            'replacement': (content) => `[c5]${content}[/c5]`
        });

        this.parser.addRule('llweb-color6', {
            'filter': new Compare().node('SPAN').class_('color').color('#fd7e14').build(),
            'replacement': (content) => `[c6]${content}[/c6]`
        });

        this.parser.addRule('llweb-size1', {
            'filter': new Compare().node('SPAN').class_('size').font('3.7rem').build(),
            'replacement': (content) => `[z1]${content}[/z1]`
        });

        this.parser.addRule('llweb-size2', {
            'filter': new Compare().node('SPAN').class_('size').font('3.1rem').build(),
            'replacement': (content) => `[z2]${content}[/z2]`
        });

        this.parser.addRule('llweb-size3', {
            'filter': new Compare().node('SPAN').class_('size').font('2.6rem').build(),
            'replacement': (content) => `[z3]${content}[/z3]`
        });

        this.parser.addRule('llweb-size4', {
            'filter': new Compare().node('SPAN').class_('size').font('2.2rem').build(),
            'replacement': (content) => `[z4]${content}[/z4]`
        });

        this.parser.addRule('llweb-size5', {
            'filter': new Compare().node('SPAN').class_('size').font('1.8rem').build(),
            'replacement': (content) => `[z5]${content}[/z5]`
        });

        this.parser.addRule('llweb-size6', {
            'filter': new Compare().node('SPAN').class_('size').font('1.5rem').build(),
            'replacement': (content) => `[z6]${content}[/z6]`
        });

        this.parser.addRule('llweb-size7', {
            'filter': new Compare().node('SPAN').class_('size').font('1.2rem').build(),
            'replacement': (content) => `[z7]${content}[/z7]`
        });

        this.parser.addRule('llweb-size8', {
            'filter': new Compare().node('SPAN').class_('size').font('1.0rem').build(),
            'replacement': (content) => `[z8]${content}[/z8]`
        });

        this.parser.addRule('llweb-align-left', {
            'filter': new Compare().node('P').class_('align-left').align('left').build(),
            'replacement': (content) => `[al]${content}[/al]`
        });

        this.parser.addRule('llweb-align-center', {
            'filter': new Compare().node('P').class_('align-center').align('center').build(),
            'replacement': (content) => `[ac]${content}[/ac]`
        });

        this.parser.addRule('llweb-align-right', {
            'filter': new Compare().node('P').class_('align-right').align('right').build(),
            'replacement': (content) => `[ar]${content}[/ar]`
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