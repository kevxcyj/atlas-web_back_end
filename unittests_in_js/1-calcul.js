function calculateNumber(type, a, b) {
  if (type.toUpperCase() !== 'DIVIDE') {
    return Math.round(a) + Math.round(b);
  }

  if (Math.round(b) === 0) {
    return 'Error';
  }

  return Math.round(a) / Math.round(b);
}

module.exports = calculateNumber;