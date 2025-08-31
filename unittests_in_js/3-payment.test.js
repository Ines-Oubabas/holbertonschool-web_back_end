'use strict';

const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi (spies)', () => {
  let spy;

  beforeEach(() => {
    // Évite le bruit dans la sortie de test
    sinon.stub(console, 'log');
    spy = sinon.spy(Utils, 'calculateNumber');
  });

  afterEach(() => {
    spy.restore();
    console.log.restore();
  });

  it('utilise Utils.calculateNumber("SUM", 100, 20)', () => {
    sendPaymentRequestToApi(100, 20);
    sinon.assert.calledOnce(spy);
    sinon.assert.calledWithExactly(spy, 'SUM', 100, 20);
  });
});
