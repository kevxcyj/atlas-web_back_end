function calculateNumber(type, a, b) {
  switch (type.toUpperCase()) {
    case 'SUM':
      return Math.round(a) + Math.round(b);
    case 'SUBTRACT':
      return Math.round(a) - Math.round(b);
    case 'DIVIDE':
      if (Math.round(b) === 0) {
        return 'Error';
      }
      return Math.round(a) / Math.round(b);
    default:
      throw new Error('Invalid operation type');
  }
}

module.exports = calculateNumber;