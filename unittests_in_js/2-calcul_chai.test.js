'use strict';

const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber(type, a, b) with Chai', () => {
  describe('SUM', () => {
    it('1.4 + 4.5 -> 6', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
    it('0.5 + 0.5 -> 2', () => {
      expect(calculateNumber('SUM', 0.5, 0.5)).to.equal(2);
    });
    it('-1.4 + 0.4 -> -1', () => {
      expect(calculateNumber('SUM', -1.4, 0.4)).to.equal(-1);
    });
  });

  describe('SUBTRACT', () => {
    it('1.4 - 4.5 -> -4', () => {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
    it('0.5 - 0.4 -> 1', () => {
      expect(calculateNumber('SUBTRACT', 0.5, 0.4)).to.equal(1);
    });
    it('-1.6 - 0.4 -> -2', () => {
      expect(calculateNumber('SUBTRACT', -1.6, 0.4)).to.equal(-2);
    });
  });

  describe('DIVIDE', () => {
    it('1.4 / 4.5 -> 0.2', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });
    it('4.6 / 2.1 -> 2.5', () => {
      expect(calculateNumber('DIVIDE', 4.6, 2.1)).to.equal(2.5);
    });
    it('div by zero -> "Error"', () => {
      expect(calculateNumber('DIVIDE', 3.9, 0.2)).to.equal('Error');
    });
  });
});
