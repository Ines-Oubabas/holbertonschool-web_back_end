'use strict';

const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi (hooks + single spy)', () => {
  let logSpy;

  beforeEach(() => {
    logSpy = sinon.spy(console, 'log'); // un seul spy
  });

  afterEach(() => {
    logSpy.restore();
  });

  it('with 100 and 20 logs "The total is: 120" once', () => {
    sendPaymentRequestToApi(100, 20);
    sinon.assert.calledOnce(logSpy);
    sinon.assert.calledWithExactly(logSpy, 'The total is: 120');
  });

  it('with 10 and 10 logs "The total is: 20" once', () => {
    sendPaymentRequestToApi(10, 10);
    sinon.assert.calledOnce(logSpy);
    sinon.assert.calledWithExactly(logSpy, 'The total is: 20');
  });
});
