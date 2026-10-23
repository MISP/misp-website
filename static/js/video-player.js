(function () {
    "use strict";

    document.querySelectorAll("[data-video-player]").forEach(function (player) {
        var video = player.querySelector("video");
        var button = player.querySelector("[data-video-play]");

        if (!video || !button) {
            return;
        }

        function showPlayButton() {
            button.hidden = false;
        }

        function hidePlayButton() {
            // Preserve keyboard focus when the activated button disappears.
            if (document.activeElement === button) {
                video.focus({ preventScroll: true });
            }
            button.hidden = true;
        }

        video.addEventListener("playing", hidePlayButton);
        video.addEventListener("pause", showPlayButton);
        video.addEventListener("ended", showPlayButton);

        button.addEventListener("click", function () {
            var playback = video.play();
            if (playback && typeof playback.catch === "function") {
                // Keep the action available if playback is blocked or fails.
                playback.catch(showPlayButton);
            }
        });

        // Native controls remain usable when JavaScript is unavailable.
        if (video.paused || video.ended) {
            showPlayButton();
        }
    });
}());
