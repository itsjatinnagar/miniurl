const openLoginModal = () =>
    document.body.classList.add(...["modal-active", "login-modal"]);

const closeLoginModal = () =>
    document.body.classList.remove(...["modal-active", "login-modal"]);

const loginButtons = document.querySelectorAll("button.btn-get-started");
loginButtons.forEach((button) => (button.onclick = openLoginModal));

const loginOverlay = document.getElementById("overlay");
loginOverlay.onclick = closeLoginModal;

const sendCodeButton = document.getElementById("btn-send-code"),
    emailInput = document.getElementById("email");

sendCodeButton.addEventListener("click", async () => {
    const response = await request(`/login?email=${emailInput.value}`, "GET");
    if (response) document.getElementById("modal").classList.add("code-sent");
});

const submitButton = document.getElementById("btn-submit"),
    otpInputs = document.querySelectorAll("#otp-input input");

otpInputs.forEach((input, index) => {
    input.addEventListener("keyup", (event) => {
        const currentInput = input,
            nextInput = input.nextElementSibling,
            prevInput = input.previousElementSibling;

        if (currentInput.value.length > 1) {
            currentInput.value = "";
            return;
        }

        if (
            nextInput &&
            nextInput.hasAttribute("disabled") &&
            currentInput.value !== ""
        ) {
            nextInput.removeAttribute("disabled");
            nextInput.focus();
        }

        if (event.key === "Backspace") {
            otpInputs.forEach((input, innerIndex) => {
                if (index <= innerIndex && prevInput) {
                    input.setAttribute("disabled", true);
                    currentInput.value = "";
                    prevInput.focus();
                }
            });
        }
    });
});

submitButton.addEventListener("click", async () => {
    let code = "";
    otpInputs.forEach((input) => (code += input.value));
    const response = await request(
        "/login",
        "POST",
        { "Content-Type": "application/json" },
        JSON.stringify({ code: code })
    );

    if (response) {
        window.location.reload();
    }
});
