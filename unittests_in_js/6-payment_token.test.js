'use strict';

const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('resolves correctly when success = true (using done)', (done) => {
    getPaymentTokenFromAPI(true)
      .then((res) => {
        expect(res).to.deep.equal({ data: 'Successful response from the API' });
        done();
      })
      .catch(done);
  });
});
