function solve(aList) {
    const result = [];
    for (let i = 0; i < aList.length; i++) {
        if (i % 2 === 1) {
            result.push(aList[i] * 2);
        }
    }

    console.log(result.reverse());
}

solve([10, 15, 20, 25]);
solve([3, 0, 10, 4, 7, 3]);