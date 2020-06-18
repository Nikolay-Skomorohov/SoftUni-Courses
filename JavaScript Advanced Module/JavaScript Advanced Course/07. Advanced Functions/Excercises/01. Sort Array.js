function solve(aList, aString) {
    if (aString === 'asc') {
        return aList.sort((a, b) => a - b);
    }
    else if (aString === 'desc') {
        return aList.sort((a, b) => b - a);
    }
}

solve([14, 7, 17, 6, 8], 'asc');
solve([14, 7, 17, 6, 8], 'desc');