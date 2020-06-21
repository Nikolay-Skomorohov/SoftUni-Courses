function solve(aCarReqs) {
    const engineTypes = {
        'Small engine': { power: 90, volume: 1800 },
        'Normal engine': { power: 120, volume: 2400 },
        'Monster engine': { power: 200, volume: 3500 }
    };

    function engineCheck() {
        if (aCarReqs.power <= 90) {
            return engineTypes['Small engine'];
        }
        else if (aCarReqs.power <= 120) {
            return engineTypes['Normal engine'];
        }
        else if (aCarReqs.power > 120) {
            return engineTypes['Monster engine'];
        }
    }

    const carriageTypes = {
        'Hatchback': { type: 'hatchback', color: 'as required' },
        'Coupe': { type: 'coupe', color: 'as required' }
    };

    function carriageCheck() {
        if (aCarReqs.carriage === 'hatchback') {
            return carriageTypes['Hatchback'];
        }
        else if (aCarReqs.carriage === 'coupe') {
            return carriageTypes['Coupe'];
        };
    }

    function wheelsCheck() {
        let newSize = aCarReqs.wheelsize;
        if (newSize % 2 === 0) {
            newSize--; 
            }
        return [newSize, newSize, newSize, newSize];
    }

    let newCar = {
        model: aCarReqs.model,
        engine: engineCheck(),
        carriage: carriageCheck(),
        wheels: wheelsCheck()
        };
    newCar.carriage.color = aCarReqs.color;
    console.log(newCar);
    return newCar;
}

solve({ model: 'VW Golf II',
        power: 90,
        color: 'blue',
        carriage: 'hatchback',
        wheelsize: 14 }
);
solve({ model: 'Opel Vectra',
        power: 110,
        color: 'grey',
        carriage: 'coupe',
        wheelsize: 17 }
);