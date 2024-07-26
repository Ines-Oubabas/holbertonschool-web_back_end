import getFullResponseFromAPI from '../1-promise';

test('getFullResponseFromAPI resolves correctly', () => {
  return getFullResponseFromAPI(true).then((response) => {
    expect(response).toEqual({ status: 200, body: 'Success' });
  });
});

test('getFullResponseFromAPI rejects correctly', () => {
  expect.assertions(1);
  return getFullResponseFromAPI(false).catch((error) => {
    expect(error.message).toBe('The fake API is not working currently');
  });
});
