function solve(aList) {
    const result = [];
    for (i = 0; i < aList.length; i++) {
        if (aList[i] >= 0) {
            result.push(aList[i]);
        }
        else {
            result.unshift(aList[i]);
        }
    }
    result.forEach(element => console.log(element));   
}

solve([7, -2, 8, 9]);
solve([3, -2, 0, -1]);