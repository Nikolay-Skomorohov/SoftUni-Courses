function lockedProfile() {
    const main = document.getElementById('main');
    main.addEventListener('click', function(e){
        const eventTarget = e.target;
        const targetParent = eventTarget.parentElement;
        const lockElem = targetParent.querySelector('input');
        const unlockElem = targetParent.querySelectorAll('input')[1];
        const infoDiv = targetParent.querySelector('div');
        const buttonElem = targetParent.querySelector('button');
        if (eventTarget.tagName === 'BUTTON' && lockElem.checked === false) {
            if (infoDiv.style.display === 'none' || infoDiv.style.display === '') {
                infoDiv.style.display = "block";
                buttonElem.textContent = "Hide it";
            }
            else if (infoDiv.style.display === "block") {
                infoDiv.style.display = 'none'
                buttonElem.textContent = "Show More";
            }
        }
        else if (eventTarget.tagName === 'INPUT' && eventTarget.type === 'radio') {
            if (eventTarget.value === "lock" && lockElem.checked === true && infoDiv.style.display === 'block') {
                unlockElem.checked = false;
                infoDiv.style.display = 'none';
                buttonElem.textContent = "Show More";
                }
            else if (eventTarget.value === "unlock" && unlockElem.checked === true) {
                lockElem.checked = false;
                unlockElem.checked = true;
            }
        }
    })
}
