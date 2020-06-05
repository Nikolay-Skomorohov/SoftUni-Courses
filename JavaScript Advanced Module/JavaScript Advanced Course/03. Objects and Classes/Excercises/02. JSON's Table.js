function solve(aList) {
    let result = "\<table\>\n";
    let objArray = [];
    for (let i of aList) {
        let personObj = JSON.parse(i);
        result += "\<tr\>\n";
        for (let x of Object.keys(personObj)) {
            result += `\<td\>${personObj[x]}\<\/td\>\n`;
        }
        result += "\<\/tr\>\n";
    }
    result += "\<\/table\>";
    console.log(result);
}

solve(['{"name":"Pesho","position":"Promenliva","salary":100000}',
       '{"name":"Teo","position":"Lecturer","salary":1000}',
       '{"name":"Georgi","position":"Lecturer","salary":1000}']
);