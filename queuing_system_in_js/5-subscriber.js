// 5-subscriber.js
import redis from 'redis';

const sub = redis.createClient();

sub.on('connect', () => {
  console.log('Redis client connected to the server');
});

sub.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

sub.subscribe('holberton school channel');

sub.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    sub.unsubscribe();
    sub.quit();
  }
});
