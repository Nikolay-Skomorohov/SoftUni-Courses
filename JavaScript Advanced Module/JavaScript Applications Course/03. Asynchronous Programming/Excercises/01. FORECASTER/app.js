function attachEvents() {
    const inputTextElem = document.getElementById('location');
    const inputButtonElem = document.getElementById('submit');
    const currentCondElem = document.getElementById('current');
    const next3DaysElem = document.getElementById('upcoming');

    inputButtonElem.addEventListener('click', function() {
        const requestedCity = inputTextElem.value;
        getInfo(requestedCity);

        async function getCode(requestedCity) {
            const response = await fetch('https://judgetests.firebaseio.com/locations.json')
            const fetchData = await response.json();
            const resultObj = fetchData.find(element => element.name === requestedCity);
            return resultObj.code;
        }

        async function getCurrentWeather(cityCode) {
            const response = await fetch(`https://judgetests.firebaseio.com/forecast/today/${cityCode}.json`);
            const fetchData = await response.json();
            // console.log(fetchData.forecast)
            return fetchData.forecast;
        }

        async function getNext3Weather(cityCode) {
            const response = await fetch(`https://judgetests.firebaseio.com/forecast/upcoming/${cityCode}.json`);
            const fetchData = await response.json();
            // console.log(fetchData.forecast)
            return fetchData.forecast;
        }

        async function getInfo(requestedCity) {
            let cityCode = await getCode(requestedCity);
            let currentCondition = await getCurrentWeather(cityCode);
            let next3days = await getNext3Weather(cityCode);

            const cityWeather = { 'name': requestedCity, 'current': currentCondition, 'next3days': next3days };

            document.getElementById('forecast').style.display = 'block';

            let newSpaCity = document.createElement('span')
            newSpaCity.className = 'forecast-data';
            newSpaCity.textContent = cityWeather.name;
            currentCondElem.appendChild(newSpaCity);

            let newSpanTemp = document.createElement('span')
            newSpanTemp.className = 'forecast-data';
            newSpanTemp.textContent = `${cityWeather.current.low}&#176;/${cityWeather.current.high}&#176;`;
            currentCondElem.appendChild(newSpanTemp);

            let newSpanCond = document.createElement('span')
            newSpanCond.className = 'forecast-data';
            newSpanCond.textContent = `${cityWeather.next3days.condition}`;
            next3DaysElem.appendChild(newSpanCond);
        }
    })
}
attachEvents();