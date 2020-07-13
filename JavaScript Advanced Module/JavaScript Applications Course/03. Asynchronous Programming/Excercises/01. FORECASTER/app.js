function attachEvents() {
    const inputTextElem = document.getElementById('location');
    const inputButtonElem = document.getElementById('submit');
    const currentCondElem = document.getElementById('current');
    const next3DaysElem = document.getElementById('upcoming');

    inputButtonElem.addEventListener('click', function() {
        const requestedCity = inputTextElem.value;

        function getCode(requestedCity) {
            return fetch('https://judgetests.firebaseio.com/locations.json')
                .then(function(response) {
                    if (response.status === 200) {
                        return response.json();
                    }
                })
                .then(data => {
                    for (let i = 0; i < data.length; i++) {
                        if (data[i].name === requestedCity) {
                            return data[i].code;
                        }
                    }

                })
                .catch(error => console.log('Error'));
        }

        function getCurrentWeather(cityCode) {
            return fetch(`https://judgetests.firebaseio.com/forecast/today/${cityCode}.json`)
                .then(function(response) {
                    if (response.status === 200) {
                        return response.json();
                    }
                })
                .then(data => {
                    return data.forecast;
                })
                .catch(error => console.log('Error'));
        }

        function getNext3Weather(cityCode) {
            return fetch(`https://judgetests.firebaseio.com/forecast/upcoming/${cityCode}.json`)
                .then(function(response) {
                    if (response.status === 200) {
                        return response.json();
                    }
                })
                .then(data => {
                    return data.forecast;
                })
                .catch(error => console.log('Error'));
        }


        async function getInfo(requestedCity) {
            try {
                let cityCode = await getCode(requestedCity);
                let currentCondition = await getCurrentWeather(cityCode);
                let next3days = await getNext3Weather(cityCode);

                return { 'current': currentCondition,
                         'next3days': next3days };
            }
            catch (e) {
                console.log('Error');
            }
        }

        let cityWeather = getInfo(requestedCity).then(r => r);

        document.getElementById('forecast').style.display = 'visible';

        let newSpaCity = document.createElement('span')
        newSpaCity.className = 'forecast-data';
        newSpaCity.textContent = cityWeather.name;
        currentCondElem.appendChild(newSpaCity);

        let newSpanTemp = document.createElement('span')
        newSpaCity.className = 'forecast-data';
        newSpaCity.textContent = `${cityWeather.forecast.low}&#176;/${cityWeather.forecast.high}&#176;`;
        currentCondElem.appendChild(newSpanTemp);

        let newSpanCond = document.createElement('span')
        newSpaCity.className = 'forecast-data';
        newSpaCity.textContent = `${cityWeather.forecast.condition}`;
        currentCondElem.appendChild(newSpanCond);


    })
}

attachEvents();