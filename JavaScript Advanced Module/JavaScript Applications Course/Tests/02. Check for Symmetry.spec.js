function isSymmetric(arr) {
    if (!Array.isArray(arr))
        return false; // Non-arrays are non-symmetric
    let reversed = arr.slice(0).reverse(); // Clone and reverse
    let equal = (JSON.stringify(arr) == JSON.stringify(reversed));
    return equal;
}

let expect = require("chai").expect;

describe('Test isSymmetric function', function() {
    it('should return false if non array is passed as argument', function () {
        const expected = false;
        const actual = isSymmetric(3);
        expect(actual).to.be.equal(expected);
    }),

    it('should return false if  array is not symmetrical', function () {
        const expected = false;
        const actual = isSymmetric([1, 2, 3, 4, 5]);
        expect(actual).to.be.equal(expected);
    }),

    it('should return true with symmetrical array', function () {
        const expected = true;
        const actual = isSymmetric([1, 3, 1]);
        expect(actual).to.be.equal(expected);
    })
});