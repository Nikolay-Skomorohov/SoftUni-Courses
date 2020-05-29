function solve(aMatrix) {
    const result = [];
    for (let i = 0; i < aMatrix.length; i++) {
        result.push(aMatrix[i].reduce((acc, current) => acc + current));
        let column = 0
        for (let x = 0; x < aMatrix.length; x++) {
            column += aMatrix[x][i];
        }
        result.push(column);
    } 
    if (result.length > 1) {
        console.log(result.every(current => current === result[0]));
    }
    else {
        consolve.log(true);
    }
}

solve([[4, 5, 6],
       [6, 5, 4],
       [5, 5, 5]]
   );
solve([[11, 32, 45],
       [21, 0, 1],
       [21, 1, 1]]
   );
solve([[1, 0, 0],
       [0, 0, 1],
       [0, 1, 0]]
   );
