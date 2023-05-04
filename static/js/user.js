const fetchSidebar = async (e) => {
  const response = await request(`/miniurl?id=${e.target.dataset.id}`);
  if (response.type === "success") {
    document.getElementById("sidebar").innerHTML = response.message;
  }
};

const sidebarButtons = document.querySelectorAll("button.btn-sidebar"),
  overlay = document.getElementById("overlay"),
  shortenForm = document.getElementById("shorten");

sidebarButtons.forEach((button) => {
  button.addEventListener("click", fetchSidebar);
  button.addEventListener("click", openOverlay);
});
overlay.onclick = closeOverlay;

shortenForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const input = e.target.querySelector("input");
  const button = e.target.querySelector("button");

  button.innerHTML = "<span class='loader'></span>";
  button.setAttribute("disabled", "true");
  const response = await request(
    "/shorten",
    JSON.stringify({ long_url: input.value })
  );
  if (response.type === "success") {
    window.location.reload();
  }
});
