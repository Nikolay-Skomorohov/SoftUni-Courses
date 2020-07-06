function lookupChar(string, index) {
    if (typeof(string) !== 'string' || !Number.isInteger(index)) {
        return undefined;
    }
    if (string.length <= index || index < 0) {
        return "Incorrect index";
    }

    return string.charAt(index);
}

const expect = require('chai').expect;
describe('Tests for "lookupChar" function', function() {
    it('should return undefined if supplied with string for index ', function () {
        const inputString = 'Ivan';
        const inputIndex = 'Ivan';
        const expected = undefined;
        const actual = lookupChar(inputString, inputIndex);
        expect(actual).to.be.equal(expected);
    })

    it('should return undefined if supplied with float for index ', function () {
        const inputString = 'Ivan';
        const inputIndex = 2.3;
        const expected = undefined;
        const actual = lookupChar(inputString, inputIndex);
        expect(actual).to.be.equal(expected);
    })

    it('should return "Incorrect index" if supplied larger index', function () {
        const inputString = 'Ivan';
        const inputIndex = 100;
        const expected = "Incorrect index";
        const actual = lookupChar(inputString, inputIndex);
        expect(actual).to.be.equal(expected);
    })

    it('should return "Incorrect index" if supplied with negative index', function () {
        const inputString = 'Ivan';
        const inputIndex = -1;
        const expected = "Incorrect index";
        const actual = lookupChar(inputString, inputIndex);
        expect(actual).to.be.equal(expected);
    })

    it('should return "Incorrect index" if supplied with empty string for text', function () {
        const inputString = '';
        const inputIndex = 0;
        const expected = "Incorrect index";
        const actual = lookupChar(inputString, inputIndex);
        expect(actual).to.be.equal(expected);
    })

    it('should return the correct char if supplied with proper inputs', function () {
        const inputString = 'Ivan';
        const inputIndex = 1;
        const expected = 'v';
        const actual = lookupChar(inputString, inputIndex);
        expect(actual).to.be.equal(expected);
    })
})


