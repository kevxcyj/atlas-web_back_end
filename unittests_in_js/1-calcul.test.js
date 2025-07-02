const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('should perform addition correctly', () => {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
  });

  it('should perform subtraction correctly', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    assert.strictEqual(calculateNumber('SUBTRACT', 10, 7), 3);
  });

  it('should perform division correctly', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    assert.strictEqual(calculateNumber('DIVIDE', 10, 3), 3);
  });

  it('should return Error for division by zero', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 10, 0), 'Error');
  });

  it('should throw an error for invalid operation type', () => {
    assert.throws(() => calculateNumber('INVALID', 1, 2), { name: 'Error' });
  });
});