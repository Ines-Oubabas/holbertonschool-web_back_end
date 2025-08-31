'use strict';

const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi (stubs)', () => {
  let stub;
  let logSpy;

  beforeEach(() => {
    stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    logSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    stub.restore();
    logSpy.restore();
  });

  it('stub Utils.calculateNumber and verify console.log', () => {
    const res = sendPaymentRequestToApi(100, 20);

    sinon.assert.calledOnce(stub);
    sinon.assert.calledWithExactly(stub, 'SUM', 100, 20);

    sinon.assert.calledOnce(logSpy);
    sinon.assert.calledWithExactly(logSpy, 'The total is: 10');

    // facultatif: vérifier la valeur retournée
    // const { expect } = require('chai');
    // expect(res).to.equal(10);
  });
});
