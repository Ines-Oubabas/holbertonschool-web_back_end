'use strict';

/**
 * Round a and b and return their sum.
 * @param {number} a
 * @param {number} b
 * @returns {number}
 */
function calculateNumber(a, b) {
  const A = Math.round(a);
  const B = Math.round(b);
  return A + B;
}

module.exports = calculateNumber;
