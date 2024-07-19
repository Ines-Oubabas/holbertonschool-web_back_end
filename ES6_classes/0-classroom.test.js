import ClassRoom from './0-classroom';

describe('ClassRoom', () => {
  it('should set maxStudentsSize properly', () => {
    const room = new ClassRoom(10);
    expect(room._maxStudentsSize).toBe(10);
  });
});
