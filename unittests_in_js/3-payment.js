'use strict';

const Utils = require('./utils');

/**
 * Calls Utils.calculateNumber('SUM', totalAmount, totalShipping)
 * and logs "The total is: <result>"
 * @param {number} totalAmount
 * @param {number} totalShipping
 * @returns {number|string} result (returned for convenience)
 */
function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const result = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${result}`);
  return result;
}

module.exports = sendPaymentRequestToApi;
