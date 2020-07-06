let mathEnforcer = {
    addFive: function (num) {
        if (typeof(num) !== 'number') {
            return undefined;
        }
        return num + 5;
    },
    subtractTen: function (num) {
        if (typeof(num) !== 'number') {
            return undefined;
        }
        return num - 10;
    },
    sum: function (num1, num2) {
        if (typeof(num1) !== 'number' || typeof(num2) !== 'number') {
            return undefined;
        }
        return num1 + num2;
    }
};

const expect = require('chai').expect;
describe('Test Math Enforcer Function', function () {
    describe('Test addFive method', function () {
        it('should return undefined if a string is passed', function () {
            const inputData = 'string';
            const expected = undefined;
            const actual = mathEnforcer.addFive(inputData);
            expect(actual).to.be.equal(expected);
        });

        it('should return proper result input number + 5 with proper inputs', function () {
            const inputData = 10;
            const expected = 15;
            const actual = mathEnforcer.addFive(inputData);
            expect(actual).to.be.equal(expected);
        });
    });

    describe('Test subtractTen method', function () {
        it('should return undefined if a string is passed', function () {
            const inputData = 'string';
            const expected = undefined;
            const actual = mathEnforcer.subtractTen(inputData);
            expect(actual).to.be.equal(expected);
        });

        it('should return proper result input number - 10 with proper inputs', function () {
            const inputData = 10;
            const expected = 0;
            const actual = mathEnforcer.subtractTen(inputData);
            expect(actual).to.be.equal(expected);
        });
    });

    describe('Test sum method', function () {
        it('should return undefined if any parameter if not a number', function () {
            const inputData1 = 'test';
            const inputData2 = 1;
            const expected = undefined;
            const actual = mathEnforcer.sum(inputData1, inputData2);
            expect(actual).to.be.equal(expected);
        });

        it('should return undefined if any parameter if not a number', function () {
            const inputData1 = 2;
            const inputData2 = 'test';
            const expected = undefined;
            const actual = mathEnforcer.sum(inputData1, inputData2);
            expect(actual).to.be.equal(expected);
        });

        it('should return undefined if only 1 parameter is supplied', function () {
            let inputData1;
            const inputData2 = 3;
            const expected = undefined;
            const actual = mathEnforcer.sum(inputData1, inputData2);
            expect(actual).to.be.equal(expected);
        });

        it('should return proper result if two numbers are supplied', function () {
            const inputData1 = 2;
            const inputData2 = 3;
            const expected = 5;
            const actual = mathEnforcer.sum(inputData1, inputData2);
            expect(actual).to.be.equal(expected);
        });
    });

})