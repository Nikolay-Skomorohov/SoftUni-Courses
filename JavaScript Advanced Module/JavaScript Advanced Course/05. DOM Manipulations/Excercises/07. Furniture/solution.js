function solve() {
    const mainDiv = document.getElementById('exercise');
    const inputField = mainDiv.getElementsByTagName('textarea')[0];
    const inputData = (inputField.value)
    inputData.slice(1, -1)
    inputData.split(', ');
    const generateButton = mainDiv.getElementsByTagName('button')[0];
    const tableBody = document.querySelector('tbody');
    const newRow = document.createElement('tr');
    const objectsLength = inputData.length;
    let currentObjIndex = 0;
    tableBody.appendChild(newRow);

    generateButton.addEventListener('click', function() {
        const currentObj = JSON.parse(inputData[currentObjIndex]);
        const newRow = document.createElement('tr');
        tableBody.appendChild(newRow);
        const lastRow = tableBody.querySelector('tr:last-child');
        const objKeys = Object.keys(currentObj);
        for (let i = 0; i < 5; i++) {
            
            let rowContent = "<td>"
            if (i === 1) {
                rowContent += `<img scr=${currentObj[objKeys[i]]}>`
            }
            else {
                rowContent += `<p>${currentObj[objKeys[i]]}<\/p>`;
            }
            rowContent += '<\/td>';
        }
        lastRow.innerHTML(rowContent);
    })
}

