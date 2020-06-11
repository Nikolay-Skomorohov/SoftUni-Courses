function attachEventsListeners() {
    const mainDiv = document.querySelector('main');
    let inputValue;

    mainDiv.addEventListener('click', function(event) {
        const targetElem = event.target.getAttribute('id');        
        if (targetElem === "daysBtn") {
            inputValue = +document.getElementById('days').value;
            document.getElementById('hours').value = inputValue * 24;
            document.getElementById('minutes').value = inputValue * 1440;
            document.getElementById('seconds').value = inputValue * 86400;
        }
        else if (targetElem === "hoursBtn") {
            inputValue = +document.getElementById('hours').value;
            document.getElementById('days').value = inputValue / 24;
            document.getElementById('minutes').value = inputValue * 60;
            document.getElementById('seconds').value = inputValue * 3600;
        }
        else if (targetElem === 'minutesBtn') {
            inputValue = +document.getElementById('minutes').value;
            document.getElementById('days').value = inputValue / 24;
            document.getElementById('hours').value = inputValue / 60;
            document.getElementById('seconds').value = inputValue * 60;
        }
        else if (targetElem === 'secondsBtn') {
            inputValue = +document.getElementById('seconds').value;
            document.getElementById('days').value = inputValue / 86400;
            document.getElementById('hours').value = inputValue / 3600;
            document.getElementById('minutes').value = inputValue / 60;
        }
    })
}