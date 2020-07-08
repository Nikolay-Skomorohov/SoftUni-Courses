function solve() {
    const departButtonElem = document.getElementById('depart');
    const arriveButtonElem = document.getElementById('arrive');
    const textInfoElem = document.querySelector('#info .info');
    let currentBusStop = 'depot';
    let nextBusStop;

    function depart() {
        fetch(`https://judgetests.firebaseio.com/schedule/${currentBusStop}.json`)
            .then(function(response) {
                if (response.status !== 200) {
                    textInfoElem.value = 'Error';
                    departButtonElem.setAttribute('disabled', 'true');
                    arriveButtonElem.setAttribute('disabled', 'true');
                }
                else {
                    return response.json();
                }
            })
            .then(function(data) {
                textInfoElem.textContent = `Next stop ${data.name}`;
                currentBusStop = data.name;
                departButtonElem.setAttribute('disabled', 'true');
                arriveButtonElem.removeAttribute('disabled');
                nextBusStop = data.next;
            })
    }

    function arrive() {
        textInfoElem.textContent = `Arriving at ${currentBusStop}`;
        departButtonElem.removeAttribute('disabled');
        arriveButtonElem.setAttribute('disabled', 'true');
        currentBusStop = nextBusStop;
        console.log('Arrive TODO...');
    }

    return {
        depart,
        arrive
    };
}

let result = solve();