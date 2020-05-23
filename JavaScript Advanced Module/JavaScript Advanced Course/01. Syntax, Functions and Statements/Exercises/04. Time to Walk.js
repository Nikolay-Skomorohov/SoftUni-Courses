function timeWalk(steps, spread, speed) {
    let totalTime = 0
    let travelDistance = steps * spread
    let speedMS = (speed * 5) / 18
    let hours;
    let mins;
    totalTime += Math.floor(travelDistance / 500) * 60
    totalTime += (travelDistance / speedMS)
    if (totalTime >= 3600) {
        hours = Math.floor(totalTime / 3600)
        totalTime -= hours * 3600
    }
    else {
        hours = 0
    }
    if (totalTime >= 60) {
        mins = Math.floor(totalTime / 60)
        totalTime -= mins * 60
    }
    else {
        mins = 0
    }
    hours = hours.toString()
    if (hours.length == 1) {
        hours = `0` + hours
    }
    mins = mins.toString()
    if (mins.length == 1) {
        mins = `0` + mins
    }
    totalTime = totalTime.toFixed(0)
    totalTime = totalTime.toString()
    if (totalTime.length == 1) {
        totalTime += `0` + totalTime
    }
    console.log(`${hours}:${mins}:${totalTime}`)
}

timeWalk(4000, 0.60, 5)
timeWalk(2564, 0.70, 5.5)