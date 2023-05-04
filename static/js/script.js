window.onload = () =>
  (document.getElementById("current-year").innerText =
    new Date().getFullYear());

const request = (uri, body) => {
  return new Promise(async (resolve, reject) => {
    const response = await fetch(uri, {
      method: body ? "POST" : "GET",
      headers: { "Content-Type": "application/json" },
      body: body,
    });
    if (response.status === 200)
      resolve({ type: "success", message: await response.text() });
    else if (response.status === 500) showPopup();
    else reject({ type: "error", message: await response.text() });
  });
};

const openOverlay = () => document.body.classList.add("active-overlay");

const closeOverlay = () => document.body.classList.remove("active-overlay");
