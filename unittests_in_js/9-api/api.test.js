'use strict';

const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const base = 'http://localhost:7865/';

  it('Correct status code?', (done) => {
    request.get(base, (err, res) => {
      expect(err).to.equal(null);
      expect(res && res.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result?', (done) => {
    request.get(base, (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', () => {
  const base = 'http://localhost:7865';

  it('200 when :id is a number', (done) => {
    request.get(`${base}/cart/12`, (err, res, body) => {
      expect(err).to.equal(null);
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('404 when :id is NOT a number', (done) => {
    request.get(`${base}/cart/hello`, (err, res) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
