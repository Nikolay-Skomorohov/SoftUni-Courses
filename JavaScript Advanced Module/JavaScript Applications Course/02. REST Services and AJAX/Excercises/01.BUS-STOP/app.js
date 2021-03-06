function getInfo() {
    const stopIDtextEl = document.getElementById('stopId');
    const stopIDbuttonEl = document.getElementById('submit');
    const stopNameEl = document.getElementById('stopName');
    const stopListEl = document.getElementById('buses');

    stopIDbuttonEl.addEventListener('click', function checkBusStop() {
        stopNameEl.innerText = "";
        stopListEl.innerHTML = "";
        if (stopIDtextEl.value) {

            const inputText = stopIDtextEl.value;
            fetch(`https://judgetests.firebaseio.com/businfo/${inputText}.json`)
                .then(function(response) {
                    if (response.status !== 200) {
                        stopNameEl.textContent = 'Error';
                    }
                    else {
                        return response.json()
                    }})
                .then(function(data) {
                    stopNameEl.textContent = data.name;

                    for (let bus of Object.keys(data.buses)) {
                        let newLi = document.createElement('li');
                        newLi.innerText = `Bus ${bus} arrives in ${data.buses[bus]} minutes`;
                        stopListEl.appendChild(newLi);
                    }
                })
            stopIDtextEl.value = "";
        }
    });
}