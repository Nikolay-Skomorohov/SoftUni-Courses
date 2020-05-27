function solve(aMatrix) {
    let result = 0;
    for (i = 0; i < aMatrix.length; i++) {
        for (x = 0; x < aMatrix[i].length; x++) {
            if ((i - 1) >= 0 && aMatrix[i][x] === aMatrix[i - 1][x]) {
                result += 1;
            }
            if ((i + 1) < aMatrix.length && aMatrix[i][x] === aMatrix[i + 1][x]) {
                result += 1;
            }
            if ((x - 1) >= 0 && aMatrix[i] === aMatrix[i][x - 1]) {
                result += 1;
            }
            if ((x + 1) < aMatrix[i].length && aMatrix[i][x] === aMatrix[i][x + 1]) {
                result += 1;
            }
            aMatrix[i][x] = null;
        }   
    }
    console.log(result);
}

solve([['2', '3', '4', '7', '0'], 
       ['4', '0', '5', '3', '4'], 
       ['2', '3', '5', '4', '2'], 
       ['9', '8', '7', '5', '4']]);

solve([['test', 'yes', 'yo', 'ho'], 
       ['well', 'done', 'yo', '6'], 
       ['not', 'done', 'yet', '5']]);

solve([[2, 2, 5, 7, 4], 
       [4, 0, 5, 3, 4],
       [2, 5, 5, 4, 2]]);