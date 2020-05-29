function solve(aList) {
    aList.sort(function(a, b) {
        if (a.length - b.length != 0) {
            return a.length - b.length;
        }
        else if (a < b) {
            return -1;
        }
    })
    aList.forEach(element => {
       console.log(element)
    });
}

solve(['alpha', 'beta', 'gamma']);
solve(['Isacc', 'Theodor', 'Jack', 'Harrison', 'George']);
solve(['test', 'Deny', 'omen', 'Default']);