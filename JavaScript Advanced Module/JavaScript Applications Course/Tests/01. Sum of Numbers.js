function sum(aList) {
    let result = 0;
    for (let num of aList) {
        result += +num;
    }
    return result;
}

let expect = require('chai').expect;

describe("Tests for sum()", function() {
    it("should return the sum of all numbers", function() {
        let testList = [1, 2, 3];
        let expected = 6;
        let actual = sum(testList);
        expect(actual).to.be.equal(expected, 'incorrect result');
    }),
    it("should return 0 if array is empty", function() {
        let testList = [];
        let expected = 0;
        let actual = sum(testList);
        expect(actual).to.be.equal(expected, 'incorrect result');
    })
})