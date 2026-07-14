(function () {
    var footer = document.getElementById('site-footer');
    var main = document.querySelector('main');
    if (!footer || !main) return;

    function syncFooterSpace() {
        main.style.paddingBottom = footer.offsetHeight + 'px';
    }

    if ('ResizeObserver' in window) {
        new ResizeObserver(syncFooterSpace).observe(footer);
    } else {
        syncFooterSpace();
        window.addEventListener('resize', syncFooterSpace);
    }
})();