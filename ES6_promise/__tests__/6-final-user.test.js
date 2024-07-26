import handleProfileSignup from '../6-final-user';

test('handleProfileSignup returns correct array', () => {
  return handleProfileSignup('Bob', 'Dylan', 'bob_dylan.jpg').then((results) => {
    expect(results).toEqual([
      { status: 'fulfilled', value: { firstName: 'Bob', lastName: 'Dylan' } },
      { status: 'rejected', value: new Error('bob_dylan.jpg cannot be processed') }
    ]);
  });
});
