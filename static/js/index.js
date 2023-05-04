const modalButtons = document.querySelectorAll("button.btn-modal"),
  overlay = document.getElementById("overlay"),
  loginForm = document.getElementById("login"),
  buttonResend = document.getElementById("btn-resend"),
  verifyForm = document.getElementById("verify");

modalButtons.forEach((button) => (button.onclick = openOverlay));
overlay.onclick = closeOverlay;

loginForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const input = e.target.querySelector("input");
  const button = e.target.querySelector("button");

  button.innerHTML = "<span class='loader'></span>";
  button.setAttribute("disabled", "true");
  const response = await request(`/login?email=${input.value}`);
  if (response.type === "success") {
    button.innerHTML = "Send Code";
    document.querySelector("div.modal").classList.add("active");
  }
});

verifyForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const input = e.target.querySelector("input");
  const button = e.target.querySelector("button");

  button.innerHTML = "<span class='loader'></span>";
  button.setAttribute("disabled", "true");
  const response = await request(
    "/login",
    JSON.stringify({ code: input.value })
  );
  if (response.type === "success") {
    window.location.reload();
  }
});
