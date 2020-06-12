function encodeAndDecodeMessages() {
    const mainDiv = document.getElementById('main');
    const sendDiv = mainDiv.querySelector('div');
    const sendText = sendDiv.querySelector('textarea');
    const receiveDiv = mainDiv.querySelector('div:last-child');
    const receiveText = receiveDiv.querySelector('textarea');

    mainDiv.addEventListener('click', function(e) {
        eventTarget = e.target;
        if (eventTarget.tagName === "BUTTON" && eventTarget.textContent === "Encode and send it") {
            let newText = sendText.value;
            let ASCIImsg = [];
            for (let index = 0; index < newText.length; index++) {
                newValue = (newText.charCodeAt(index)) + 1;
                ASCIImsg.push(String.fromCharCode(newValue));
            }
            receiveText.value = ASCIImsg.join("");
            sendText.value = ""
        }
        else if (eventTarget.tagName === "BUTTON" && eventTarget.textContent === "Decode and read it") {
            let toDecode = receiveText.value;
            let ASCIImsg2 = [];
            for (let i = 0; i < toDecode.length; i++) {
                let newValue2 = (toDecode.charCodeAt(i)) - 1;
                ASCIImsg2.push((String.fromCharCode(newValue2)));
            }
            receiveText.value = ASCIImsg2.join("");
        }
    });
}