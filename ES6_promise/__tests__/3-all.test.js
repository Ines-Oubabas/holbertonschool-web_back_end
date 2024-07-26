import handleProfileSignup from '../3-all';

test('handleProfileSignup logs correct message', () => {
  console.log = jest.fn();
  return handleProfileSignup().then(() => {
    expect(console.log).toHaveBeenCalledWith('photo-profile-1 Guillaume Salva');
  });
});
