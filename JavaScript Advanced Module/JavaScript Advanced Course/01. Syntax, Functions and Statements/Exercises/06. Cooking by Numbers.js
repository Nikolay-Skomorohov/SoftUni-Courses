function solve(inputList) {
    let theNum = +inputList[0];
    for (i = 1; i < inputList.length; i++) {
        switch (inputList[i]) {
            case 'chop':
                theNum /= 2;
                break;
            case 'dice':
                theNum = Math.sqrt(theNum);
                break;
            case 'spice':
                theNum += 1;
                break;
            case 'bake':
                theNum *= 3;
                break;
            case 'fillet':
                theNum *= 0.8;
                break;
        }
        console.log(theNum);
    }
}

solve(['32', 'chop', 'chop', 'chop', 'chop', 'chop'])
solve(['9', 'dice', 'spice', 'chop', 'bake', 'fillet'])