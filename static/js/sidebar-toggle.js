(function () {
    "use strict";

    var storageKey = "misp-content-sidebar-hidden";
    var layouts = document.querySelectorAll("[data-sidebar-layout]");

    function savedPreference() {
        try {
            return window.localStorage.getItem(storageKey) === "true";
        } catch (error) {
            return false;
        }
    }

    function savePreference(isHidden) {
        try {
            window.localStorage.setItem(storageKey, String(isHidden));
        } catch (error) {
            // The control still works when browser storage is unavailable.
        }
    }

    Array.prototype.forEach.call(layouts, function (layout) {
        var button = layout.querySelector("[data-sidebar-toggle]");
        var label = layout.querySelector("[data-sidebar-toggle-label]");

        if (!button || !label) {
            return;
        }

        function setSidebar(hidden) {
            layout.classList.toggle("is-sidebar-hidden", hidden);
            button.setAttribute("aria-expanded", String(!hidden));
            label.textContent = hidden ? "Show sidebar" : "Hide sidebar";
        }

        setSidebar(savedPreference());
        button.hidden = false;

        button.addEventListener("click", function () {
            var hidden = !layout.classList.contains("is-sidebar-hidden");
            setSidebar(hidden);
            savePreference(hidden);
        });
    });
}());
