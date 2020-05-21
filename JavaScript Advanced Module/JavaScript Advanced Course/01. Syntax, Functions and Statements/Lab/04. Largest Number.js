function solveLargest(arr1, arr2, arr3) {
    let result;
    let num1 = +arr1;
    let num2 = +arr2;
    let num3 = +arr3;
    result = num1
    
    if (num2 > num1 && num2 > num3) {
        result = num2
    }
    if (num3 > num1 && num3 > num2) {
        result = num3
    }
    console.log('The largest number is' + ' ' + result + '.')
}

solveLargest(5, -3, 16)