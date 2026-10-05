(function () {
    "use strict";

    var container = document.getElementById("misp-security-advisories");
    if (!container) {
        return;
    }

    var status = container.querySelector("[data-feed-status]");
    var list = container.querySelector("[data-feed-entries]");
    var feedUrl = container.dataset.feedUrl;
    var atomNamespace = "http://www.w3.org/2005/Atom";
    var controller = new AbortController();
    var timeout = setTimeout(function () { controller.abort(); }, 10000);

    function children(element, name) {
        return Array.from(element.children).filter(function (child) {
            return child.namespaceURI === atomNamespace && child.localName === name;
        });
    }

    function text(element, name) {
        var child = children(element, name)[0];
        return child ? child.textContent.trim() : "";
    }

    async function loadAdvisories() {
        status.hidden = false;
        status.textContent = "Loading recent CVE advisories…";
        container.setAttribute("aria-busy", "true");

        try {
            if (!feedUrl) {
                throw new Error("Feed unavailable at build time");
            }
            var response = await fetch(feedUrl, {
                headers: { "Accept": "application/atom+xml" },
                signal: controller.signal
            });
            if (!response.ok) {
                throw new Error("Feed request failed");
            }

            var xml = new DOMParser().parseFromString(await response.text(), "application/xml");
            var feed = xml.documentElement;
            if (xml.getElementsByTagName("parsererror").length ||
                    feed.localName !== "feed" || feed.namespaceURI !== atomNamespace) {
                throw new Error("Invalid Atom feed");
            }

            var fragment = document.createDocumentFragment();
            children(feed, "entry").slice(0, 30).forEach(function (entry) {
                var title = text(entry, "title");
                var link = children(entry, "link").find(function (candidate) {
                    return !candidate.getAttribute("rel") || candidate.getAttribute("rel") === "alternate";
                });
                if (!title || !link || !link.getAttribute("href")) {
                    return;
                }

                var url;
                try {
                    url = new URL(link.getAttribute("href"), container.dataset.sourceUrl);
                } catch (error) {
                    return;
                }
                if (url.protocol !== "https:" && url.protocol !== "http:") {
                    return;
                }

                var item = document.createElement("li");
                var anchor = document.createElement("a");
                anchor.href = url.href;
                anchor.textContent = title;
                item.appendChild(anchor);

                var updated = text(entry, "updated");
                var date = new Date(updated || text(entry, "published"));
                if (!isNaN(date.getTime())) {
                    var label = document.createElement("small");
                    label.className = "text-muted";
                    label.appendChild(document.createTextNode(" — "));
                    var time = document.createElement("time");
                    time.dateTime = date.toISOString();
                    time.textContent = (updated ? "Updated " : "Published ") + date.toLocaleDateString("en-US", {
                        year: "numeric", month: "short", day: "numeric", timeZone: "UTC"
                    });
                    label.appendChild(time);
                    item.appendChild(label);
                }
                fragment.appendChild(item);
            });

            list.replaceChildren(fragment);
            status.textContent = list.children.length ? "" : "No recent CVE advisories are available in this feed.";
            status.hidden = list.children.length > 0;
        } catch (error) {
            status.textContent = "Recent advisories are temporarily unavailable. Please use the full vulnerability list above.";
        } finally {
            clearTimeout(timeout);
            container.setAttribute("aria-busy", "false");
        }
    }

    loadAdvisories();
}());
