function getFibonator() {
    var aNum = 0;
    var bNum = 0;
    return function test() {
        if (aNum === 0) {
            aNum++
            return 1;
        }
        else if (aNum === 1 && bNum === 0) {
            bNum = aNum;
            return 1;
        }
        result = aNum + bNum;
        aNum = bNum;
        bNum = result;
        return result;
    }
}

let fib = getFibonator();
console.log(fib()); // 1
console.log(fib()); // 1
console.log(fib()); // 2
console.log(fib()); // 3
console.log(fib()); // 5
console.log(fib()); // 8
console.log(fib()); // 13
