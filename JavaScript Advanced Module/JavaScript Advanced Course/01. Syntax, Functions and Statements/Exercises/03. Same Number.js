function solve(num) {
    let resultSum = 0;
    let resultBool = true
    let numStr = num.toString()
    for (let i = 0; i < numStr.length; i++) {
        resultSum += +numStr.charAt(i)
        if (numStr.charAt(0) !== numStr.charAt(i)) {
            resultBool = false
        }
    }
    console.log(resultBool);
    console.log(resultSum);
}

solve(1234)