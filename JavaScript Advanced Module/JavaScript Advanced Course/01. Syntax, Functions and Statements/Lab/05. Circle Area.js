function circleArea(arg) {
    let result;
    let inputType = typeof(arg);
    if (inputType === 'number') {
        result = Math.pow(arg, 2) * Math.PI;
        console.log(result.toFixed(2))
    }
    else {
        console.log(`We can not calculate the circle area, because we receive a ${inputType}.`)
    }
}

circleArea('name')