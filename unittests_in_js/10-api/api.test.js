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

describe('Available payments & login', () => {
  const base = 'http://localhost:7865';

  it('GET /available_payments deep equality', (done) => {
    request.get(`${base}/available_payments`, { json: true }, (err, res, body) => {
      expect(err).to.equal(null);
      expect(res.statusCode).to.equal(200);
      expect(body).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      });
      done();
    });
  });

  it('POST /login returns "Welcome <username>"', (done) => {
    const payload = { userName: 'Betty' };
    request.post(
      { url: `${base}/login`, json: true, body: payload },
      (err, res, body) => {
        expect(err).to.equal(null);
        expect(res.statusCode).to.equal(200);
        // réponse texte => body est souvent une string
        if (typeof body === 'string') {
          expect(body).to.equal('Welcome Betty');
        } else {
          expect(res.body || '').to.equal('Welcome Betty');
        }
        done();
      }
    );
  });
});
