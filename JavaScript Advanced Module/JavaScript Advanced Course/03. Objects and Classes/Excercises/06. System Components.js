function solve(inputList) {
    let result = {};
    for (let item of inputList) {
        let itemSystem = item.split(" | ")[0];
        let itemComponent = item.split(" | ")[1];
        let itemSubcomponent = item.split(" | ")[2];
        if (!Object.keys(result).includes(itemSystem)) {
            result[itemSystem] = {};
        }
        if (!Object.keys(result[itemSystem]).includes(itemComponent)) {
            result[itemSystem][itemComponent] = []
        }
        result[itemSystem][itemComponent].push(itemSubcomponent);
    }
    let sortedSystems = Object.keys(result).sort(function(a, b) {
        let aLen = Object.keys(result[a]).length;    
        let bLen = Object.keys(result[b]).length;    
        if (aLen < bLen) {
                return 1;
            }
        else if (aLen > bLen) {
                return -1;
            }
        else {
            if (a.toUpperCase() < b.toUpperCase()) {
                return -1;
            }
            else {
                return 1;
            }
        }}
    )
    for (let system of sortedSystems) {
        console.log(system);
        let sortedComponents = Object.keys(result[system]).sort(function(a, b) {
            let aLen = result[system][a].length;
            let bLen = result[system][b].length;
            if (aLen < bLen) {
                return 1;
            }
        else if (aLen > bLen) {
                return -1;
            }
        else {
            if (a.toUpperCase() < b.toUpperCase()) {
                return -1;
            }
            else {
                return 1;
            }
        }
        })
        for (let comp of sortedComponents) {
            console.log(`|||${comp}`);
            for (let sub of result[system][comp]) {
                console.log(`||||||${sub}`);
            }
        }
    }
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