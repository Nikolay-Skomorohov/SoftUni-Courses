function getInfo() {
    const stopIDtextEl = document.getElementById('stopId');
    const stopIDbuttonEl = document.getElementById('submit');
    const stopNameEl = document.getElementById('stopName');
    const stopListEl = document.getElementById('buses');

    stopIDbuttonEl.addEventListener('click', function checkBusStop() {
        if (stopIDtextEl.value !== '') {
            const inputText = stopIDtextEl.value;
            const incomingData = fetch(`https://judgetests.firebaseio.com/businfo/${inputText}.json`)
                .then(function(response) {
                    if (response.status === 200) {
                        return response.json()
                    }
                    else {
                        return stopNameEl.textContent = 'Error';
                    }})
                .then(function (r) {
                    return r;
                })
            stopNameEl.textContent = incomingData.name;
            for (let bus of Object.keys(incomingData.buses)) {
                let newLi = document.createElement('li');
                newLi.innerText = bus;
                stopListEl.appendChild(newLi);
            }
        }
    });
}