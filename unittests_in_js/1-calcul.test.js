'use strict';

const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber(type, a, b)', () => {
  describe('SUM', () => {
    it('1.4 + 4.5 -> 1 + 5 = 6', () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
    it('1.5 + 3.5 -> 2 + 4 = 6', () => {
      assert.strictEqual(calculateNumber('SUM', 1.5, 3.5), 6);
    });
  });

  describe('SUBTRACT', () => {
    it('1.4 - 4.5 -> 1 - 5 = -4', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
    it('1.5 - 3.5 -> 2 - 4 = -2', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.5), -2);
    });
  });

  describe('DIVIDE', () => {
    it('1.4 / 4.5 -> 1 / 5 = 0.2', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
    it('1.4 / 0 -> Error', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
    it('4.6 / 2.1 -> 5 / 2 = 2.5', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 4.6, 2.1), 2.5);
    });
  });
});
