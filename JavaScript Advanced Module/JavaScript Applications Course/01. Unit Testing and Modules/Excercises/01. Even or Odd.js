function isOddOrEven(string) {
    if (typeof(string) !== 'string') {
        return undefined;
    }
    if (string.length % 2 === 0) {
        return "even";
    }

    return "odd";
}

// module.exports = { isOddOrEven }
// const isOddOrEven = require('../01. Unit Testing and Modules/Excercises/01. Even or Odd.js').isOddOrEven;

let expect = require('chai').expect;

describe('Test isOddorEven function', function() {
    it('should return undefined if supplied with empty array', function () {
        const inputData = [];
        const expected = undefined;
        const actual = isOddOrEven(inputData);
        expect(actual).to.be.equal(expected);
    })

    it('should return even if supplied with "Ivan', function () {
        const inputData = "Ivan";
        const expected = 'even';
        const actual = isOddOrEven(inputData);
        expect(actual).to.be.equal(expected);
    })

    it('should return odd if supplied with "Petko"', function () {
        const inputData = "Petko";
        const expected = 'odd';
        const actual = isOddOrEven(inputData);
        expect(actual).to.be.equal(expected);
    })

    it('should return undefined if supplied with a number', function () {
        const inputData = 3;
        const expected = undefined;
        const actual = isOddOrEven(inputData);
        expect(actual).to.be.equal(expected);
    })

    it('should return odd if no input is supplied', function () {
        let inputData;
        const expected = undefined;
        const actual = isOddOrEven(inputData);
        expect(actual).to.be.equal(expected);
    })
})
