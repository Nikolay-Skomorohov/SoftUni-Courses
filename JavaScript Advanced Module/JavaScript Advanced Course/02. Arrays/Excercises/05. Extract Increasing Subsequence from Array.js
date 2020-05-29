function solve(aList) {
    let result;
    for (let i = 0; i < aList.length; i++) {
        if (typeof(result) === 'undefined') {
            result = [aList[0]]
        }
        else {
            if (aList[i] >= result[result.length - 1]) {
                result.push(aList[i]);
            }
        }
    }
    result.forEach(element => console.log(element));
}

solve([1, 3, 8, 4, 10, 12, 3, 2, 24]);
solve([1, 2, 3, 4]);
solve([20, 3, 2, 15, 6, 1]);