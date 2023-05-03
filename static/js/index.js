const openModal = () => document.body.classList.add("active-overlay");

const closeModal = () => document.body.classList.remove("active-overlay");

const modalButtons = document.querySelectorAll("button.btn-modal"),
    overlay = document.getElementById("overlay"),
    emailInput = document.getElementById("email"),
    buttonLogin = document.getElementById("btn-login"),
    buttonResend = document.getElementById("btn-resend"),
    codeInput = document.getElementById("code"),
    verifyButton = document.getElementById("btn-verify");

modalButtons.forEach((button) => (button.onclick = openModal));
overlay.onclick = closeModal;

buttonLogin.addEventListener("click", () => {});
