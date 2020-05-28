function solve(aList) {
    let initialNum = 1;
    const resultList = [];
    for (let i = 0; i < aList.length; i++) {
        switch (aList[i]) {
            case 'add':
                resultList.push(initialNum);
                break;
        
            case 'remove':
                resultList.pop(-1);
                break;
        }
        initialNum += 1;
    }
    if (resultList.length === 0) {
        console.log('Empty');
    }
    else if (resultList != []) {
        resultList.forEach(element => console.log(element));
    }
}

// solve(['add', 'add', 'add', 'add']);
// solve(['add', 'add', 'remove', 'add', 'add']);
solve(['remove', 'remove', 'remove']);