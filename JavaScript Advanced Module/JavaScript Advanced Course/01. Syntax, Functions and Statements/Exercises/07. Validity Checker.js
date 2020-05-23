function solve(inputList) {
    let resultValid;
    let point1 = [inputList[0], inputList[1]];
    let point2 = [inputList[2], inputList[3]];
    let center = [0, 0];
    if (Number.isInteger(Math.sqrt(((center[0] - point1[0]) ** 2) + ((center[1] - point1[1]) ** 2)))) {
        console.log(`{${point1[0]}, ${point1[1]}} to {${center[0]}, ${center[1]}} is valid`)
    }
    else {
        console.log(`{${point1[0]}, ${point1[1]}} to {${center[0]}, ${center[1]}} is invalid`)
    }
    if (Number.isInteger(Math.sqrt(((center[0] - point2[0]) ** 2) + ((center[1] - point2[1]) ** 2)))) {
        console.log(`{${point2[0]}, ${point2[1]}} to {${center[0]}, ${center[1]}} is valid`)
    }
    else {
        console.log(`{${point2[0]}, ${point2[1]}} to {${center[0]}, ${center[1]}} is invalid`)
    }
    if (Number.isInteger(Math.sqrt(((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2)))) {
        console.log(`{${point1[0]}, ${point1[1]}} to {${point2[0]}, ${point2[1]}} is valid`)
    }
    else {
        console.log(`{${point1[0]}, ${point1[1]}} to {${point2[0]}, ${point2[1]}} is invalid`)
    }
}

solve([3, 0, 0, 4])
solve([2, 1, 1, 1])