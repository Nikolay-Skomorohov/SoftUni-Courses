function solve(inputList) {
    let result = [];
    let juiceData = [];
    for (let juice of inputList) {
        let juiceName = juice.split(" => ")[0]
        let juiceCount = Number(juice.split(" => ")[1]);
        for (let obj of juiceData) {
            if (! Object.keys(obj).includes(juiceName)) {
                let newObj = {};
                newObj[juiceName] = Number(juiceCount);
                juiceData.push(newObj);
            }
            else {
                obj[juiceName] += Number(juiceCount);
            }
            if (obj[juiceName] >= 1000) {
                let resultObj = {};
                resultObj[juiceName] = Math.floor(obj[juiceName] / 1000);
                obj[juiceName] -= bottles * 1000
                result.push(resultObj);

            }
        }
    }
    console.log(result);

}

solve(['Orange => 2000',
       'Peach => 1432',
       'Banana => 450',
       'Peach => 600',
       'Strawberry => 549']
);
// solve(['Kiwi => 234',
//        'Pear => 2345',
//        'Watermelon => 3456',
//        'Kiwi => 4567',
//        'Pear => 5678',
//        'Watermelon => 6789']
// );