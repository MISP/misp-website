(function () {
    "use strict";

    var scriptElement = document.currentScript;
    var sourceUrl = scriptElement && scriptElement.dataset.tipsUrl;
    var repositoryUrl = "https://github.com/cudeso/misp-tip-of-the-week";
    var titleElement = document.getElementById("tip-of-the-week-title");
    var textElement = document.getElementById("tip-of-the-week-text");
    var linkElement = document.getElementById("tip-of-the-week-link");
    var refreshButton = document.getElementById("tip-of-the-week-refresh");
    var tips = [];
    var currentIndex = -1;

    if (!titleElement || !textElement || !linkElement || !refreshButton) {
        return;
    }

    if (!sourceUrl) {
        sourceUrl = "/data/misp-tip-of-the-week.json";
    }

    function firstString(object, keys) {
        for (var i = 0; i < keys.length; i += 1) {
            if (typeof object[keys[i]] === "string" && object[keys[i]].trim()) {
                return object[keys[i]].trim();
            }
        }
        return "";
    }

    function normalizeTip(tip) {
        if (typeof tip === "string") {
            return { title: "MISP tip of the week", text: tip, url: "" };
        }

        if (!tip || typeof tip !== "object") {
            return null;
        }

        var text = firstString(tip, ["tip", "description", "content", "text", "body"]);
        if (!text) {
            return null;
        }

        return {
            title: firstString(tip, ["title", "name", "subject"]) || "MISP tip of the week",
            text: text,
            url: firstString(tip, ["url", "link", "reference", "source"])
        };
    }

    function findEntries(data) {
        if (Array.isArray(data)) {
            return data;
        }

        if (!data || typeof data !== "object") {
            return [];
        }

        var preferredEntries = data.tips || data.items || data.entries;
        if (Array.isArray(preferredEntries)) {
            return preferredEntries;
        }

        var keys = Object.keys(data);
        for (var i = 0; i < keys.length; i += 1) {
            if (Array.isArray(data[keys[i]])) {
                return data[keys[i]];
            }
        }

        return [];
    }

    function safeHttpUrl(value) {
        if (!value) {
            return "";
        }

        try {
            var url = new URL(value, repositoryUrl);
            return url.protocol === "https:" || url.protocol === "http:" ? url.href : "";
        } catch (error) {
            return "";
        }
    }

    function showRandomTip() {
        var nextIndex;

        if (!tips.length) {
            return;
        }

        do {
            nextIndex = Math.floor(Math.random() * tips.length);
        } while (tips.length > 1 && nextIndex === currentIndex);

        currentIndex = nextIndex;
        titleElement.textContent = tips[currentIndex].title;
        textElement.textContent = tips[currentIndex].text;

        var tipUrl = safeHttpUrl(tips[currentIndex].url);
        linkElement.href = tipUrl || repositoryUrl;
        linkElement.hidden = !tipUrl;
    }

    refreshButton.addEventListener("click", showRandomTip);

    fetch(sourceUrl, { headers: { "Accept": "application/json" } })
        .then(function (response) {
            if (!response.ok) {
                throw new Error("Tip request failed with status " + response.status);
            }
            return response.json();
        })
        .then(function (data) {
            tips = findEntries(data).map(normalizeTip).filter(Boolean);

            if (!tips.length) {
                throw new Error("The tip feed did not contain any supported tips");
            }

            showRandomTip();
            refreshButton.hidden = tips.length < 2;
        })
        .catch(function () {
            titleElement.textContent = "MISP tip of the week";
            textElement.textContent = "The community tip could not be loaded right now.";
            linkElement.href = repositoryUrl;
            linkElement.textContent = "Browse all tips";
            linkElement.hidden = false;
        });
}());
