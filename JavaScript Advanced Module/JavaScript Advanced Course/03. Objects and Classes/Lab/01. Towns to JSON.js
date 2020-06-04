function solve(aList) {
    const result = [];
    const final = []
    let re = /(^\|\s)|(\s\|$)/g;
    for (let i = 0; i < aList.length; i++) {
       let items = aList[i].replace(re, "").split(" | ");
       for (let x = 1; x < items.length; x++) {
              if (! isNaN(items[x])) {
                     items[x] = Number(items[x]).toFixed(2);
              }
       }
       result.push(items);
    }
    for (let y = 1; y < result.length; y++){
       let obj = {};
       for (let k = 0; k < result[0].length; k++) {
              isNaN(result[y][k]) ? obj[result[0][k]] = result[y][k] : obj[result[0][k]] = Number(result[y][k]);  
       }
       final.push(obj);
    }
    console.log(JSON.stringify(final));
}

solve(['| Town | Latitude | Longitude |',
       '| Sofia | 42.696552 | 23.32601 |',
       '| Beijing | 39.913818 | 116.363625 |']);
// solve(['| Town | Latitude | Longitude |',
//        '| Veliko Turnovo | 43.0757 | 25.6172 |',
//        '| Monatevideo | 34.50 | 56.11 |']);