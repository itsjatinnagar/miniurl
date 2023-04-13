const shortenButton = document.getElementById("btn-shorten"),
    shortenInput = document.getElementById("shorten");

shortenButton.addEventListener("click", async () => {
    const response = await request(
        "/shorten",
        "POST",
        { "Content-Type": "application/json" },
        JSON.stringify({ long_url: shortenInput.value })
    );
    if (response) {
        window.location.reload();
    }
});

// shortenButton.addEventListener("click", () => {
//     const url = document.getElementById("url").value;
//     fetch("/shorten", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//         },
//         body: JSON.stringify({ long_url: url }),
//     }).then((response) =>
//         response.status == 200 ? window.location.reload() : showPopup()
//     );
// });

// linksButton.forEach((button) => {
//     button.addEventListener("click", () => {
//         fetch(`/get/${button.dataset.linkid}`)
//             .then((response) =>
//                 response.status == 200 ? response.text() : showPopup()
//             )
//             .then((data) => openSidebar(data));
//     });
// });

// function openSidebar(HTML_CONTENT) {
//     document.body.classList.add("overlay-active");
//     sidebarOverlay.classList.add("active");
//     sidebar.classList.add("active");
//     sidebar.innerHTML = HTML_CONTENT;
//     activateClipboard();
// }

// sidebarOverlay.addEventListener("click", () => {
//     document.body.classList.remove("overlay-active");
//     sidebarOverlay.classList.remove("active");
//     sidebar.classList.remove("active");
//     sidebar.innerHTML = "";
// });

// function activateClipboard() {
//     const copyButton = document.getElementById("btn-copy");
//     copyButton.addEventListener("click", () => {
//         navigator.clipboard
//             .writeText(sidebar.querySelector("p.short-link").textContent)
//             .then((response) => console.log(response))
//             .catch((error) => console.log(error));
//     });
// }
