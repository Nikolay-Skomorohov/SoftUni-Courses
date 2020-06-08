function toggle() {
    const buttonElem = document.getElementsByClassName('button')[0];
    const hiddenDiv = document.getElementById('extra');
    if (buttonElem.textContent === "More") {
        buttonElem.textContent = "Less";
        hiddenDiv.style.display = 'block';
    }
    else if (buttonElem.textContent === "Less") {
        buttonElem.textContent = "More";
        hiddenDiv.style.display = 'none';
    }
}