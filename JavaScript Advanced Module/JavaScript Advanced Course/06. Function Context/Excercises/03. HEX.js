class Hex {
    constructor(value) {
        this.value = value;
    }

    valueOf() {
        return this.value;
    }

    toString() {
        let result = this.value.toString(16).toUpperCase();
        return `0x${result}`;
    }

    plus(number) {
        let result = number instanceof Hex ? this.valueOf() + number.valueOf() : this.valueOf() + number;
        return new Hex(result);
    }

    minus(number) {
        let result = number instanceof Hex ? this.valueOf() - number.valueOf() : this.value - number;
        return new Hex(result);
    }

    parse(string) {
        return string.toString(10);
    }
}

let FF = new Hex(255);
console.log(FF.toString());
FF.valueOf() + 1 == 256;
let a = new Hex(10);
let b = new Hex(5);
console.log(a.plus(b).toString());
console.log(a.plus(b).toString()==='0xF');
