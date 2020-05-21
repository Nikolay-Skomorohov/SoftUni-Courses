function mathOperations(num1, num2, operator) {
    let finalResult;
    switch (operator) {
        case '+':
            finalResult = num1 + num2
            break;
        case '-':
            finalResult = num1 - num2
            break;
        case '*':
            finalResult = num1 * num2
            break;
        case '/':
            finalResult = num1 / num2
            break;
        case '%':
            finalResult = num1 % num2
            break;
        case '**':
            finalResult = num1 ** num2
            break;
    }
    console.log(finalResult)
}

mathOperations(3, 5.5, '*')