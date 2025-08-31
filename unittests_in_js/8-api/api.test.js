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

  it('Content-Type header present', (done) => {
    request.get(base, (err, res) => {
      expect(res.headers).to.have.property('content-type');
      done();
    });
  });
});
