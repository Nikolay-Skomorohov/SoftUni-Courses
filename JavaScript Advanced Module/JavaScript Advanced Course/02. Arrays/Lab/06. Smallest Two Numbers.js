function solve(aList) {
    let result = aList.sort((a, b) => a - b);
    console.log(result.slice(0, 2));
}

solve([30, 15, 50, 5]);
solve([3, 0, 10, 4, 7, 3]);