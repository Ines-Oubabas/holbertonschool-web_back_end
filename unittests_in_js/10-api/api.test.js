'use strict';

const request = require('request');
const { expect } = require('chai');

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
      {
        url: `${base}/login`,
        json: true,           // envoie JSON et tente de parser si la réponse est JSON
        body: payload
      },
      (err, res, body) => {
        expect(err).to.equal(null);
        expect(res.statusCode).to.equal(200);
        // Comme le serveur renvoie du texte, body est généralement une string.
        if (typeof body === 'string') {
          expect(body).to.equal('Welcome Betty');
        } else {
          // fallback selon l'environnement/test runner
          expect(res.body || '').to.equal('Welcome Betty');
        }
        done();
      }
    );
  });
});
