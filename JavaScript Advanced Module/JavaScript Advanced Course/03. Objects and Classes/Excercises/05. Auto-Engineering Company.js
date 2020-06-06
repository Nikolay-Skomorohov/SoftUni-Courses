function solve(inputList) {
    let result = {};
    for (let item of inputList) {
        let itemBrand = item.split(" | ")[0];
        let itemModel = item.split(" | ")[1];
        let itemQuantity = item.split(" | ")[2];

        if (!Object.keys(result).includes(itemBrand)) {
            result[itemBrand] = {};
        }
        if (!Object.keys(result[itemBrand]).includes(itemModel)) {
            result[itemBrand][itemModel] = Number(itemQuantity);
        }
        else {
            result[itemBrand][itemModel] += Number(itemQuantity);
        }
    }
    for (let brand of Object.keys(result)) {
        console.log(brand);

        brandModels = Object.keys(result[brand]);
        brandModels.forEach(element => {
            console.log(`###${element} -> ${result[brand][element]}`);
        });
    }
}

solve(['Audi | Q7 | 1000',
       'Audi | Q6 | 100',
       'BMW | X5 | 1000',
       'BMW | X6 | 100',
       'Citroen | C4 | 123',
       'Volga | GAZ-24 | 1000000',
       'Lada | Niva | 1000000',
       'Lada | Jigula | 1000000',
       'Citroen | C4 | 22',
       'Citroen | C5 | 10']
);