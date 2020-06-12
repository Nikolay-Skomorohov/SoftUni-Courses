function solve() {
    const mainDiv = document.getElementById('exercise');
    const inputField = mainDiv.getElementsByTagName('textarea')[0];
    const inputDataList = JSON.parse(inputField.value);
    const generateButton = mainDiv.getElementsByTagName('button')[0];
    const buyButton = mainDiv.getElementsByTagName('button')[1];
    const buyField = mainDiv.getElementsByTagName('textarea')[1];
    const tableBody = document.querySelector('tbody');

    generateButton.addEventListener('click', function() {
        for (let obj of inputDataList) {
            const newRow = document.createElement('tr');
            tableBody.appendChild(newRow);
            const newestRow = tableBody.lastChild;
            let rowContent = "";
            rowContent += `<td><img src=${obj['img']}><\/td>` +
                        `<td><p>${obj['name']}<\/p><\/td>` +
                        `<td><p>${obj['price']}<\/p><\/td>` +
                        `<td><p>${obj['decFactor']}<\/p><\/td>` +
                        `<td><input type="checkbox"\/><\/td>`;
            newestRow.innerHTML = rowContent;
        }
    })

    tableBody.addEventListener('click', function(e) {
        eventTarget = e.target;
        if (eventTarget.tagName === "INPUT") {
            eventTarget.checked ? eventTarget.checked = true : eventTarget.checked = false;
        }
    })

    buyButton.addEventListener('click', function(e) {
        const checkMarksElems = Array.from(document.querySelectorAll('td > input'));
        eventTarget = e.target;
        if (eventTarget.tagName === "BUTTON" && eventTarget.textContent === "Buy") {
            let itemNames = [];
            let itemsPrice = 0;
            let itemsDecor = [];
            for (let item = 0; item < checkMarksElems.length; item++) {
                if (checkMarksElems[item].checked === true) {
                    const parentTDs = checkMarksElems[item].parentElement.parentElement.getElementsByTagName('td');
                    itemNames.push(parentTDs[1].textContent);
                    itemsPrice += +parentTDs[2].textContent;
                    itemsDecor.push(+parentTDs[3].textContent);
                }
            }
            itemsDecorAverage = itemsDecor.reduce((a, b) => a + b, 0) / itemsDecor.length;
            buyField.value = ("Bought furniture: " + itemNames.join(", ") + "\n" 
                                    + "Total price: " + itemsPrice.toFixed(2) + "\n"
                                    + "Average decoration factor: " + itemsDecorAverage);
        }
    })
}