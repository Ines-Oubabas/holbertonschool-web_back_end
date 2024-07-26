import uploadPhoto from '../5-photo-reject';

test('uploadPhoto rejects with correct error', () => {
  expect.assertions(1);
  return uploadPhoto('guillaume.jpg').catch((error) => {
    expect(error.message).toBe('guillaume.jpg cannot be processed');
  });
});
