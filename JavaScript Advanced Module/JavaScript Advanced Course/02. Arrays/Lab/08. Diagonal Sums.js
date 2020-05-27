function solve(aMatrix) {
    let primeDia = 0;
    let secondDia = 0;
    for (i = 0; i < aMatrix.length; i++) {
        primeDia += aMatrix[i][i];
        secondDia += aMatrix[i][(aMatrix.length - 1) - i];
    }
    const result = [primeDia, secondDia];
    console.log(result.join(" "));
}

solve([[20, 40], [10, 60]]);
solve([[3, 5, 17], [-1, 7, 14], [1, -8, 89]]);