function solve() {
    const alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, 
                      "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
                      "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
                      "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                      "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
                      "z": 26 };
    const eventTarget = document.getElementsByTagName('button')[0];
    eventTarget.addEventListener('click', function() {

        const inputElem = document.getElementsByTagName('input')[0];
        const inputText = inputElem.value;
        const firstLetter = (alphabet[inputText[0].toLowerCase()]) - 1;
        const outputElem = document.getElementsByTagName('li')[firstLetter];
        const outputText = outputElem.textContent;
        if (outputText === "") {
            outputElem.textContent = inputText[0].toUpperCase() + inputText.slice(1).toLowerCase()
        }
        else {
            const outputList = Array.from(outputText.split(', '));
            outputList.push(inputText[0].toUpperCase() + inputText.slice(1).toLowerCase());
            outputElem.textContent = outputList.join(', ');
        }
        inputElem.value = "";
    })
}