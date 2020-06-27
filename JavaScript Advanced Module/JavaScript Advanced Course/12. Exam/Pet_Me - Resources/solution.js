function solve() {
    const inputNameElement = document.querySelectorAll('#container input')[0];
    const inputAgeElement = document.querySelectorAll('#container input')[1];
    const inputKindElement = document.querySelectorAll('#container input')[2];
    const inputCurrentOwnerElement = document.querySelectorAll('#container input')[3];
    const adoptionSectionElement = document.querySelector('#adoption ul');
    const adoptedSectionElement = document.querySelector('#adopted ul');

    document.querySelector('#container button').addEventListener('click', addTask);

    function addTask(event) {
        event.preventDefault();

        const nameInput = inputNameElement.value;
        const ageInput = inputAgeElement.value;
        const kindInput = inputKindElement.value;
        const ownerInput = inputCurrentOwnerElement.value;
        const newLi = document.createElement('li');

        if (nameInput.length > 0 && 
            ageInput.length > 0 &&
            !isNaN(ageInput) &&
            kindInput.length > 0 &&
            ownerInput.length > 0) {
                let result = `<p><strong>${nameInput}<\/strong> is a <strong>${ageInput}<\/strong> year old <strong>${kindInput}<\/strong><\/p><span>Owner: ${ownerInput}</span><button>Contact with owner<\/button>`
                newLi.innerHTML = result;
                adoptionSectionElement.appendChild(newLi);

                newLi.querySelector('button').addEventListener('click', function(event) {
                    let targetElement = event.target;
                    targetElementParent = targetElement.parentElement;
                    targetElement.remove();
                    targetElementParent.innerHTML += '<div><input placeholder="Enter your names"><button>Yes! I take it!<\/button><\/div>';

                    newLi.querySelector('button').addEventListener('click', function(event) {
                        const nameField = newLi.querySelector('div input');
                        if (nameField.value.length > 0) {
                            adoptedSectionElement.appendChild(newLi);
                            newLi.innerHTML = `<p><strong>${nameInput}<\/strong> is a <strong>${ageInput}<\/strong> year old <strong>${kindInput}<\/strong><\/p><span>New Owner: ${nameField.value}</span><button>Checked<\/button>`
                        };
                        newLi.querySelector('button').addEventListener('click', function(event) {
                            newLi.remove();
                        });
                    });
                });
        
            };


        inputNameElement.value = "";
        inputAgeElement.value = "";
        inputKindElement.value = "";
        inputCurrentOwnerElement.value = "";
    };
}

