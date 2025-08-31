'use strict';

/**
 * calculateNumber with type ('SUM' | 'SUBTRACT' | 'DIVIDE')
 * Rounds a and b before operation.
 * @param {'SUM'|'SUBTRACT'|'DIVIDE'} type
 * @param {number} a
 * @param {number} b
 * @returns {number|string}
 */
function calculateNumber(type, a, b) {
  const A = Math.round(a);
  const B = Math.round(b);

  if (type === 'SUM') return A + B;
  if (type === 'SUBTRACT') return A - B;
  if (type === 'DIVIDE') {
    if (B === 0) return 'Error';
    return A / B;
  }
  throw new Error('Unknown type');
}

module.exports = calculateNumber;
