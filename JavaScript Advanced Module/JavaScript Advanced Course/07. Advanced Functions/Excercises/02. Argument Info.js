function solve(...args) {
    const argCounts = {};
    const funcArgs = args;
    for (let arg of funcArgs) {
        console.log(`${typeof(arg)}: ${arg}`);
        if (!Object.keys(argCounts).includes(typeof(arg))) {
            argCounts[typeof(arg)] = 0;
        }
        argCounts[typeof(arg)] += 1;
    }
    let result = Object.entries(argCounts).sort((a, b) => b[1] - a[1]);
    for (let obj of result) {
        console.log(`${obj[0]} = ${obj[1]}`);
    }
}        

solve('cat', 42, function () { console.log('Hello world!'); });
// solve({ name: 'bob'}, 3.333, 9.999);
// solve(42, 'cat', 15, 'kitten', 'tomcat');
