(function () {
    "use strict";

    function getTableLabel(table, index) {
        var heading = table.previousElementSibling;

        while (heading && !/^H[2-6]$/.test(heading.tagName)) {
            heading = heading.previousElementSibling;
        }

        return heading ? heading.textContent.trim() : "Data table " + (index + 1);
    }

    function enhanceTable(table, index) {
        if (table.closest(".data-table") || table.matches(".table-plain")) {
            return;
        }

        var rows = Array.prototype.slice.call(table.tBodies).reduce(function (allRows, body) {
            return allRows.concat(Array.prototype.slice.call(body.rows));
        }, []);
        var label = getTableLabel(table, index);
        var wrapper = document.createElement("div");
        var scroller = document.createElement("div");

        wrapper.className = "data-table" + (rows.length >= 15 ? " data-table--large" : "");
        scroller.className = "data-table__scroll";
        scroller.tabIndex = 0;
        scroller.setAttribute("role", "region");
        scroller.setAttribute("aria-label", label + ", scrollable table");

        table.parentNode.insertBefore(wrapper, table);
        wrapper.appendChild(scroller);
        scroller.appendChild(table);
        table.classList.add("data-table__table");

        if (rows.length < 15) {
            return;
        }

        var toolbar = document.createElement("div");
        var searchGroup = document.createElement("label");
        var searchIcon = document.createElement("i");
        var search = document.createElement("input");
        var count = document.createElement("span");
        var updateCount = function (visible) {
            count.textContent = visible + " of " + rows.length + " entries";
        };

        toolbar.className = "data-table__toolbar";
        searchGroup.className = "data-table__search";
        searchIcon.className = "fas fa-search";
        searchIcon.setAttribute("aria-hidden", "true");
        search.type = "search";
        search.className = "data-table__input";
        search.placeholder = "Filter table…";
        search.setAttribute("aria-label", "Filter " + label);
        count.className = "data-table__count";
        count.setAttribute("aria-live", "polite");

        search.addEventListener("input", function () {
            var query = search.value.trim().toLocaleLowerCase();
            var visible = 0;

            rows.forEach(function (row) {
                var matches = !query || row.textContent.toLocaleLowerCase().indexOf(query) !== -1;
                row.hidden = !matches;
                if (matches) {
                    visible += 1;
                }
            });

            updateCount(visible);
        });

        searchGroup.appendChild(searchIcon);
        searchGroup.appendChild(search);
        toolbar.appendChild(searchGroup);
        toolbar.appendChild(count);
        wrapper.insertBefore(toolbar, scroller);
        updateCount(rows.length);
    }

    document.addEventListener("DOMContentLoaded", function () {
        Array.prototype.forEach.call(document.querySelectorAll("#content table"), enhanceTable);
    });
}());
