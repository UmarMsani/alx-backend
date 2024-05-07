import { createQueue } from 'kue';

// Create a Kue queue
const queue = createQueue({ name: 'push_notification_code' });
// Create an object containing the Job data
const job = queue.create('push_notification_code', {
    phoneNumber: string,
    message: string,
});

job.on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
})
job.on('error', (err) => {
    console.log(`Notification job ${job.id} failed: ${err}`);
});
job.on('complete', () => { 
    console.log(`Notification job ${job.id} completed`);
});
