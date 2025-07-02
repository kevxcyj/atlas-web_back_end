const chai = require('chai');
const expect = chai.expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  it('should perform addition correctly', () => {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
  });

  it('should perform subtraction correctly', () => {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    expect(calculateNumber('SUBTRACT', 10, 7)).to.equal(3);
  });

  it('should perform division correctly', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    expect(calculateNumber('DIVIDE', 10, 3)).to.equal(3);
  });

  it('should return Error for division by zero', () => {
    expect(calculateNumber('DIVIDE', 10, 0)).to.equal('Error');
  });

  it('should throw an error for invalid operation type', () => {
    expect(() => calculateNumber('INVALID', 1, 2)).to.throw();
  });
});