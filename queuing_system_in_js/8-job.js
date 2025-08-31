// 8-job.js
import kue from 'kue';

export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((data) => {
    const job = queue.create('push_notification_code_3', data).save((err) => {
      if (!err) console.log(`Notification job created: ${job.id}`);
    });

    job.on('complete', () => console.log(`Notification job ${job.id} completed`));
    job.on('failed', (err) => console.log(`Notification job ${job.id} failed: ${err}`));
    job.on('progress', (progress) => console.log(`Notification job ${job.id} ${progress}% complete`));
  });
}

// Optional helper to run manually (like in the statement):
// import createPushNotificationsJobs from './8-job.js';
// const queue = kue.createQueue();
// createPushNotificationsJobs([{ phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' }], queue);
