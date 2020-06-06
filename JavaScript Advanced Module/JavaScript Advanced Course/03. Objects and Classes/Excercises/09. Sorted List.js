class List {
    constructor() {
        this.list = [];
        this.size = this.list.length;
    }

    add(element) {
        this.list.push(Number(element));
        this.size = this.list.length;
        return this.list.sort((a, b) => a - b);
    }

    remove(index) {
        if (index <= this.size - 1 && index >= 0) {
            this.list.splice(index, 1);
            this.size = this.list.length;
            return this.list.sort((a, b) => a - b);
        } 
    }

    get(index) {
        if (index <= this.size - 1 && index >= 0) {
            return this.list[index];
        }
    }
}

let list = new List();
list.add(5);
list.add(6);
list.add(7);
console.log(list.get(1)); 
list.remove(1);
console.log(list.get(1));

