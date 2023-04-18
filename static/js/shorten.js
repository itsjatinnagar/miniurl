const shortenButton = document.getElementById("btn-shorten"),
    shortenInput = document.getElementById("shorten");

shortenButton.addEventListener("click", async () => {
    shortenButton.innerHTML = '<span class="loader light"></span>';
    const response = await request(
        "/shorten",
        "POST",
        { "Content-Type": "application/json" },
        JSON.stringify({ long_url: shortenInput.value })
    );
    if (response) {
        shortenButton.innerHTML = "Shorten It!";
        window.location.reload();
    }
});

const dateSpans = document.querySelectorAll("span.date");
dateSpans.forEach((span) => {
    const datetimeUTC = new Date(span.textContent * 1000);
    const datetime = new Date(
        datetimeUTC.getFullYear(),
        datetimeUTC.getMonth(),
        datetimeUTC.getDate()
    );
    span.textContent = Intl.DateTimeFormat().format(datetime);
});

const copyButtons = document.querySelectorAll("button.btn-copy");
copyButtons.forEach((button) => {
    button.addEventListener("click", () =>
        navigator.clipboard
            .writeText(button.dataset.link)
            .catch((error) => console.log(error))
    );
});
