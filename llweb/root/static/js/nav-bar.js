class Collapsebles {
    constructor(varargin) {
        this.button = document.getElementById(varargin.button);
        this.container = document.getElementById(varargin.container);

        this.button.addEventListener('click', this.toggle);
    }

    toggle = () => {
        if (this.button.getAttribute('data-collapsed') === 'true') {
            this.button.setAttribute('data-collapsed', 'false');
            this.show(this.container);
        } else {
            this.button.setAttribute('data-collapsed', 'true');
            this.hide(this.container);
        }
    }

    executeAfterTransition = (callback, transitionElement) => {
        const emulatedDuration = this.getTransitionDurationFromElement(transitionElement) + 5;

        let called = false;
        const handler = ({ target }) => {
            if (target !== transitionElement) return;
            called = true;
            transitionElement.removeEventListener('transitionend', handler);
            callback();
        };

        transitionElement.addEventListener('transitionend', handler);
        setTimeout(() => {
            if (!called) transitionElement.dispatchEvent(new Event('transitionend'));
        }, emulatedDuration);
    };

    getTransitionDurationFromElement = element => {
        let { transitionDuration, transitionDelay } = window.getComputedStyle(element);

        const floatTransitionDuration = Number.parseFloat(transitionDuration);
        const floatTransitionDelay = Number.parseFloat(transitionDelay);

        if (!floatTransitionDuration && !floatTransitionDelay) return 0;

        transitionDuration = transitionDuration.split(',')[0];
        transitionDelay = transitionDelay.split(',')[0];

        return (Number.parseFloat(transitionDuration) + Number.parseFloat(transitionDelay)) * 1000;
    };
}

class NavBarCollapseblesVertical extends Collapsebles {
    constructor(varargin) {
        super(varargin)
    }

    show = element => {
        element.classList.remove('collapse-v');
        element.classList.add('collapsing-v');
        element.style.height = '0px';

        this.executeAfterTransition(() => {
            element.classList.remove('collapsing-v');
            element.classList.add('collapse-v', 'show');
            element.style.height = '';
        }, element);

        element.style.height = element.scrollHeight + 'px';
    };

    hide = element => {
        element.style.height = element.scrollHeight + 'px';
        element.offsetHeight;
        element.classList.add('collapsing-v');
        element.classList.remove('collapse-v', 'show');

        element.style.height = '';
        this.executeAfterTransition(() => {
            element.classList.remove('collapsing-v');
            element.classList.add('collapse-v');
        }, element);
    };
}

class NavBarCollapseblesHorinzontal extends Collapsebles {
    constructor(varargin) {
        super(varargin)
    }

    show = element => {
        element.classList.remove('collapse-h');
        element.classList.add('collapsing-h');
        element.style.width = '0px';

        this.executeAfterTransition(() => {
            element.classList.remove('collapsing-h');
            element.classList.add('collapse-h', 'show');
            element.style.width = '';
        }, element);

        element.style.width = element.scrollWidth + 'px';
    }

    hide = element => {
        element.style.width = element.scrollWidth + 'px';
        element.offsetWidth;
        element.classList.add('collapsing-h');
        element.classList.remove('collapse-h', 'show');

        element.style.width = '';
        this.executeAfterTransition(() => {
            element.classList.remove('collapsing-h');
            element.classList.add('collapse-h');
        }, element);
    }
}

(() => {
    const navHeader = document.getElementById('nav-header');
    const navSearch = document.getElementById('nav-search');

    if (navHeader) {
        new NavBarCollapseblesVertical({
            button: 'button-toggler',
            container: 'navbar-collapse'
        });
    }

    if (navSearch) {
        new NavBarCollapseblesHorinzontal({
            button: 'search-toggler',
            container: 'nav-search-collapse'
        })
    }
})();