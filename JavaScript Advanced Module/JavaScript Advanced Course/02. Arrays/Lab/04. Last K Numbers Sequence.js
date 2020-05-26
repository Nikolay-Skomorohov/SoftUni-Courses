function solve(num1, num2) {
    const result = [1];

    for (i = 1; i < num1; i++) {
        var tempSum = 0;
        for (x = 1; x <= num2; x++) {
            tempNum = i - x;
            if (tempNum >= 0) {
                tempSum += result[tempNum];
            }
            else {
                break;
            }
        }
        result.push(tempSum);
    }
    console.log(result);
}

solve(6, 3);
solve(8, 2);