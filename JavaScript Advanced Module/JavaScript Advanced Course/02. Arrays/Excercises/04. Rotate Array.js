function solve(aList) {
    const rotateNum = aList[aList.length - 1];
    let anArray = aList.slice(0, -1);
    const rotations = rotateNum % (anArray.length);
    for (let i = 0  ; i < rotations; i++) {
        const lastItem = anArray.pop();
        anArray.unshift(lastItem);
    }
    console.log(anArray.join(" "));
}

solve(['1', '2', '3', '4', '2']);
solve(['Banana', 'Orange', 'Coconut', 'Apple', '15']);