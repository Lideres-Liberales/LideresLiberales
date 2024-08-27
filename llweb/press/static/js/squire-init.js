let editor;

const squireAction = (action) => {
    var test = {
        value: 'bold',
        testBold: editor.testPresenceinSelection('bold', action, 'B', (/>B\b/)),
        testItalic: editor.testPresenceinSelection('italic', action, 'I', (/>I\b/)),
        testUnderline: editor.testPresenceinSelection('underline', action, 'U', (/>U\b/)),
        testOrderedList: editor.testPresenceinSelection('makeOrderedList', action, 'OL', (/>OL\b/)),
        testLink: editor.testPresenceinSelection('makeLink', action, 'A', (/>A\b/)),
        testQuote: editor.testPresenceinSelection('increaseQuoteLevel', action, 'blockquote', (/>blockquote\b/)),
        isNotValue: function (a) { return a === action && this.value !== ''; }
    };

    editor.alignRight = function () { editor.setTextAlignment('right'); };
    editor.alignCenter = function () { editor.setTextAlignment('center'); };
    editor.alignLeft = function () { editor.setTextAlignment('left'); };
    editor.alignJustify = function () { editor.setTextAlignment('justify'); };
    editor.makeHeading = function () { editor.setFontSize('2em'); editor.bold(); };

    if (test.testBold || test.testItalic || test.testUnderline || test.testOrderedList || test.testLink || test.testQuote) {
        if (test.testBold) editor.removeBold();
        if (test.testItalic) editor.removeItalic();
        if (test.testUnderline) editor.removeUnderline();
        if (test.testLink) editor.removeLink();
        if (test.testOrderedList) editor.removeList();
        if (test.testQuote) editor.decreaseQuoteLevel();
    } else if (test.isNotValue('makeLink') || test.isNotValue('insertImage') || test.isNotValue('selectFont')) {
        // No action required for dropdowns
    } else {
        editor[action]();
        editor.focus();
    }
}

const setFont = (id_buttom, fontSize) => {
    document.querySelector(id_buttom)?.addEventListener('click', () => {
        editor.setFontSize(fontSize);
    });
}

const setTextColor = (id_buttom, textColor) => {
    document.querySelector(id_buttom)?.addEventListener('click', () => {
        editor.setTextColor(textColor);
    });
}

const loadAction = (id_buttom, action) => {
    document.querySelector(id_buttom)?.addEventListener('click', () => {
        squireAction(action);
    });
}

(() => {
    Squire.prototype.testPresenceinSelection = function (name, action, format, validation) {
        var path = this.getPath();
        var test = (validation.test(path) || this.hasFormat(format));
        return name === action && test;
    };

    let container = document.querySelector('#editor');
    let textarea = document.querySelector('.wysiwyg.wysiwyg-textarea');
    if (container) {
        editor = new Squire(container);

        if (textarea) {
            if (textarea.value && textarea.value != undefined && textarea.value != null) {
                editor.setHTML(textarea.value);
            }
        }

        container.addEventListener('input', () => {
            textarea.value = editor.getHTML();
        });
    } else {
        console.error("No element was defined for the editor to inject to.");
    }

    setFont('#sq-heading1', '3.7rem');
    setFont('#sq-heading2', '3.1rem');
    setFont('#sq-heading3', '2.6rem');
    setFont('#sq-heading4', '2.2rem');
    setFont('#sq-heading5', '1.8rem');
    setFont('#sq-heading6', '1.5rem');
    setFont('#sq-heading7', '1.2rem');
    setFont('#sq-heading8', '1.0rem');

    setTextColor('#sq-color0', '#000000');
    setTextColor('#sq-color1', '#dc3545');
    setTextColor('#sq-color2', '#ffc107');
    setTextColor('#sq-color3', '#28a745');
    setTextColor('#sq-color4', '#007bff');
    setTextColor('#sq-color5', '#6c757d');
    setTextColor('#sq-color6', '#fd7e14');

    loadAction('#sq-undo', 'undo');
    loadAction('#sq-redo', 'redo');

    loadAction('#sq-removeAllFormatting', 'removeAllFormatting');

    loadAction('#sq-makeHeading', 'makeHeading');
    loadAction('#sq-bold', 'bold');
    loadAction('#sq-italic', 'italic');
    loadAction('#sq-underline', 'underline');

    loadAction('#sq-alignLeft', 'alignLeft');
    loadAction('#sq-alignCenter', 'alignCenter');
    loadAction('#sq-alignRight', 'alignRight');


})();
