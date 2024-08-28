class HtmlSanitizer {
    constructor() {
        this.allowedTags = ['div', 'ol', 'li', 'span', 'b', 'i', 'u', 'br'];
        this.allowedAttributes = ['class', 'style'];
    }

    sanitize(input) {
        const template = document.createElement('template');

        if (input instanceof Node) {
            template.innerHTML = input.outerHTML;
        } else {
            template.innerHTML = input;
        }

        const sanitizeNode = (node) => {
            if (node.nodeType === Node.ELEMENT_NODE) {
                if (!this.allowedTags.includes(node.nodeName.toLowerCase())) {
                    node.remove();
                    return;
                }

                Array.from(node.attributes).forEach(attr => {
                    if (!this.allowedAttributes.includes(attr.name)) {
                        node.removeAttribute(attr.name);
                    }
                });

                Array.from(node.childNodes).forEach(child => sanitizeNode(child));
            } else if (node.nodeType === Node.TEXT_NODE) {
                return;
            }
        };

        sanitizeNode(template);

        return template;
    }
}

const htmlSanitizer = new HtmlSanitizer();