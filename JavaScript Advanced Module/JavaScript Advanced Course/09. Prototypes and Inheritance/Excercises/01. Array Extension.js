Array.prototype.last = function() {
    return this[this.length -1];
};
Array.prototype.skip = function(n) {
    let result = this.slice(n);
    return result;
};
Array.prototype.take = function(n)  {
    let result = this.slice(0, n);
    return result;
};
Array.prototype.sum = function() {
    let result = this.reduce((acc, curr) => acc + curr);
    return result;
};
Array.prototype.average = function() {
    let result = this.sum() / this.length;
    return result;
};  
var testArray = [1, 2, 3];
console.log(Array.prototype.hasOwnProperty('last'));
console.log(testArray.last());
console.log(testArray.skip(2));
console.log(testArray.take(2));
console.log(testArray.sum());
console.log(testArray.average());
