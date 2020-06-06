function solve(inputList) {
    let result = {};
    for (let item of inputList) {
        let itemSystem = item.split(" | ")[0];
        let itemComponent = item.split(" | ")[1];
        let itemSubcomponent = item.split(" | ")[2];
        if (!Object.keys(result).includes(itemSystem)) {
            result[itemSystem] = [];
        }
        if (!Object.keys(result[itemSystem]).includes(itemComponent)) {
            result[itemSystem][itemComponent] = [];
        }
        result[itemSystem][itemComponent].push(itemSubcomponent);
    }
    let sorting = sort(function(a, b) {
        null;
    })
    console.log(result);
}

solve(['SULS | Main Site | Home Page',
       'SULS | Main Site | Login Page',
       'SULS | Main Site | Register Page',
       'SULS | Judge Site | Login Page',
       'SULS | Judge Site | Submittion Page',
       'Lambda | CoreA | A23',
       'SULS | Digital Site | Login Page',
       'Lambda | CoreB | B24',
       'Lambda | CoreA | A24',
       'Lambda | CoreA | A25',
       'Lambda | CoreC | C4',
       'Indice | Session | Default Storage',
       'Indice | Session | Default Security']);