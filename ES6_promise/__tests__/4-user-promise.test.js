import signUpUser from '../4-user-promise';

test('signUpUser returns correct object', () => {
  return signUpUser('Bob', 'Dylan').then((response) => {
    expect(response).toEqual({ firstName: 'Bob', lastName: 'Dylan' });
  });
});
