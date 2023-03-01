const sendCodeButton = document.getElementById("btn-sendCode");
const verifyButton = document.getElementById("btn-verify");
const modalOverlay = document.getElementById("overlay");
const modal = document.getElementById("modal");

sendCodeButton.addEventListener("click", () => {
    const userEmail = document.getElementById("email").value;
    fetch(`/login?email=${userEmail}`).then((response) =>
        response.status == 200 ? openModal() : showPopup()
    );
});

verifyButton.addEventListener("click", () => {
    const code = document.getElementById("otp").value;
    fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ code: code }),
    }).then((response) =>
        response.status == 200 ? window.location.reload() : showPopup()
    );
});

function openModal() {
    document.body.classList.add("overlay-active");
    modalOverlay.classList.add("active");
    modal.classList.add("active");
}

modalOverlay.addEventListener("click", () => {
    document.body.classList.remove("overlay-active");
    modalOverlay.classList.remove("active");
    modal.classList.remove("active");
});

function showPopup() {
    console.log("Popup to show error message is appeared");
}
