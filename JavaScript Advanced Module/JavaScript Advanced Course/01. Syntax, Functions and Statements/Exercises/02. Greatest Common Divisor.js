function commonDivisor(num1, num2) {
    let result;
    let largestDivisor = (num1 < num2) ? num1 : num2;
    for (let i = 1; i < (largestDivisor + 1); i++) {
        if (num1 % i === 0 && num2 % i === 0) {
            result = i
        }
    }
    console.log(result);
}

commonDivisor(2154, 458);