function solve(aMatrix) {
    let result;
    for (i = 0; i < aMatrix.length; i++) {
        for (x = 0; x < aMatrix[i].length; x++) {
            if (! result) {
                result = aMatrix[i][x];
            }
            else {
                if (aMatrix[i][x] > result) {
                    result = aMatrix[i][x];
                }
            }
        }
    }
    console.log(result);
}

solve([[20, 50, 10], [8, 33, 145]]);
solve([[3, 5, 7, 12], [-1, 4, 33, 2], [8, 3, 0, 4]]);