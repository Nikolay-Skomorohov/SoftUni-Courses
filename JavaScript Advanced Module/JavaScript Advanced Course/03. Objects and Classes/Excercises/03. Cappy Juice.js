function solve(inputList) {
    let result = {};
    let juiceData = {};
    for (let juice of inputList) {
        let juiceName = juice.split(" => ")[0]
        let juiceCount = Number(juice.split(" => ")[1]);
        if (! Object.keys(juiceData).includes(juiceName)) {
            juiceData[juiceName] = Number(juiceCount);
        }
        else {
            juiceData[juiceName] += Number(juiceCount);
        }
        if (juiceData[juiceName] >= 1000) {
            if (! Object.keys(result).includes(juiceName)) {
                result[juiceName] = Math.floor(juiceData[juiceName] / 1000);
                juiceData[juiceName] -= result[juiceName] * 1000;
            }
            else {
                result[juiceName] += Math.floor(juiceData[juiceName] / 1000);
                juiceData[juiceName] -= result[juiceName] * 1000;
            }
        }
    }
    let key = Object.keys(result);
    for (let i of key) {
        console.log(`${i} => ${result[i]}`)
    }
}

solve(['Orange => 2000',
       'Peach => 1432',
       'Banana => 450',
       'Peach => 600',
       'Strawberry => 549']
);
solve(['Kiwi => 234',
       'Pear => 2345',
       'Watermelon => 3456',
       'Kiwi => 4567',
       'Pear => 5678',
       'Watermelon => 6789']
);