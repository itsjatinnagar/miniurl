const shortenButton = document.getElementById("btn-shorten");

shortenButton.addEventListener("click", () => {
    const url = document.getElementById("url").value;
    fetch("/shorten", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ long_url: url }),
    }).then((response) =>
        response.status == 200 ? window.location.reload() : showPopup()
    );
});
