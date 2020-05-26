function solve(aList) {
    let result = '';
    for (i = 0; i < aList.length; i++) {
        if (i % 2 === 0) {
            result += ' ' + aList[i]
        }
    }
    console.log(result)
}

solve(['20', '30', '40']);
solve(['5', '10']);
