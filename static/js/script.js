const request = (uri, method, headers, body) =>
    new Promise(async (resolved) => {
        const response = await fetch(uri, {
            method: method,
            headers: headers,
            body: body,
        });
        if (response.status === 200) resolved(true);
        else if (response.status === 500) showPopup();
        else resolved(false, response.status, response.body());
    });

function showPopup() {
    console.log("Popup to show error message is appeared");
}

const openMenu = () => {
    menu.classList.add("active");
    menuButton.dataset.action = "close";
};

const closeMenu = () => {
    menu.classList.remove("active");
    menuButton.dataset.action = "open";
};

const menuButton = document.getElementById("btn-menu");
const menu = document.getElementById("menu");

menuButton.onclick = (event) => {
    switch (event.target.dataset.action) {
        case "open":
            openMenu();
            break;

        case "close":
            closeMenu();
            break;

        default:
            console.error("Invalid menuButton action");
            break;
    }
};
