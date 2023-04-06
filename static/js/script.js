function showPopup() {
    console.log("Popup to show error message is appeared");
}

const menuOpenAction = () => {
    menu.classList.add("active");
    menuButton.dataset.action = "close";
};

const menuCloseAction = () => {
    menu.classList.remove("active");
    menuButton.dataset.action = "open";
};

const menuButton = document.getElementById("btn-menu");
const menu = document.getElementById("menu");

menuButton.onclick = (event) => {
    switch (event.target.dataset.action) {
        case "open":
            menuOpenAction();
            break;

        case "close":
            menuCloseAction();
            break;

        default:
            console.error("Invalid menuButton action");
            break;
    }
};
