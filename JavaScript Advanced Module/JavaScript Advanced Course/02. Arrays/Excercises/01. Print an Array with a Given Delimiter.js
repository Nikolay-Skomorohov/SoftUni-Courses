function solve(aList) {
    const delimiter = aList[aList.length - 1];
    console.log(aList.slice(0, -1).join(delimiter));
}

solve(['One', 'Two', 'Three', 'Four', 'Five', '-']);
solve(['How about no?', 'I', 'will', 'not', 'do', 'it!', '_']);