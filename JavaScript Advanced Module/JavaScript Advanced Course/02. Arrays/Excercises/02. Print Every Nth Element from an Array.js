function solve(aList) {
    const printStep = Number(aList[aList.length - 1]);
    const anArray = aList.slice(0, -1);
    for (let i = 0; i < anArray.length; i += printStep) {
        console.log(anArray[i]);
    }
}

solve(['5', '20', '31', '4', '20', '2']);
solve(['dsa', 'asd', 'test', 'tset', '2']);
solve(['1', '2', '3', '4', '5', '6']);