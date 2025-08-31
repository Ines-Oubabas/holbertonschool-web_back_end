'use strict';

const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber (sum, rounding)', () => {
  it('1 + 3 = 4', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('1 + 3.7 ~ 1 + 4 = 5', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('1.2 + 3.7 ~ 1 + 4 = 5', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('1.5 + 3.7 ~ 2 + 4 = 6', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('0.4 + 0.4 ~ 0 + 0 = 0', () => {
    assert.strictEqual(calculateNumber(0.4, 0.4), 0);
  });

  it('0.5 + 0.4 ~ 1 + 0 = 1', () => {
    assert.strictEqual(calculateNumber(0.5, 0.4), 1);
  });

  it('-1.4 + 0.4 ~ -1 + 0 = -1', () => {
    assert.strictEqual(calculateNumber(-1.4, 0.4), -1);
  });

  it('-1.5 + 0.4 ~ -1 + 0 = -1', () => {
    assert.strictEqual(calculateNumber(-1.5, 0.4), -1);
  });

  it('-1.6 + 0.4 ~ -2 + 0 = -2', () => {
    assert.strictEqual(calculateNumber(-1.6, 0.4), -2);
  });

  it('big numbers are ok', () => {
    assert.strictEqual(calculateNumber(99.9, 100.1), 200);
  });
});
