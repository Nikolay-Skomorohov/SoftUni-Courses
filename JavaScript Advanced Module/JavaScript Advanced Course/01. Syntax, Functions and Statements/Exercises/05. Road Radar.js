function roadRadar(arrayList) {
    switch (arrayList[1]) {
        case 'motorway':
            if (130 < arrayList[0] && arrayList[0] <= 150) {
                console.log('speeding')
            }
            else if (150 < arrayList[0] && arrayList[0] <= 170) {
                console.log('excessive speeding')
            }
            else if (arrayList[0] > 170) {
                console.log('reckless driving')
            }
            break;
        case 'interstate':
            if (90 < arrayList[0] && arrayList[0] <= 110) {
                console.log('speeding')
            }
            else if (110 < arrayList[0] && arrayList[0] <= 130) {
                console.log('excessive speeding')
            }
            else if (arrayList[0] > 130) {
                console.log('reckless driving')
            }
            break;
        case 'interstate':
            if (90 < arrayList[0] && arrayList[0] <= 110) {
                console.log('speeding')
            }
            else if (110 < arrayList[0] && arrayList[0] <= 130) {
                console.log('excessive speeding')
            }
            else if (arrayList[0] > 130) {
                console.log('reckless driving')
            }
            break;
        case 'city':
            if (50 < arrayList[0] && arrayList[0] <= 70) {
                console.log('speeding')
            }
            else if (70 < arrayList[0] && arrayList[0] <= 90) {
                console.log('excessive speeding')
            }
            else if (arrayList[0] > 90) {
                console.log('reckless driving')
            }
            break;
        case 'residential':
            if (20 < arrayList[0] && arrayList[0] <= 40) {
                console.log('speeding')
            }
            else if (40 < arrayList[0] && arrayList[0] <= 60) {
                console.log('excessive speeding')
            }
            else if (arrayList[0] > 60) {
                console.log('reckless driving')
            }
            break;
    }
}

roadRadar([40, 'city'])
roadRadar([21, 'residential'])
roadRadar([120, 'interstate'])
roadRadar([200, 'motorway'])