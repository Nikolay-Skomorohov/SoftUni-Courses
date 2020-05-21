function solve(list = Array()) {
    let theArray = list;
    let sumResult = 0;
    let inverseSum = 0;
    let concatResult = ''
    theArray.forEach(element => {
        sumResult += element
    });
    theArray.forEach(element => {
        inverseSum += 1 / element
    })
    theArray.forEach(element => {
        concatResult += element
    })

    console.log(sumResult)
    console.log(inverseSum)
    console.log(concatResult)
}

solve([1, 2, 3])