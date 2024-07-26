import getResponseFromAPI from '../0-promise';

test('getResponseFromAPI returns a promise', () => {
  expect(getResponseFromAPI() instanceof Promise).toBe(true);
});
