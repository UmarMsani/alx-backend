import { createQueue, Job } from 'kue';

const BLACKLISTED_NUMBERS = [4153518780, 4153518781];
const queue = createQueue();

// Function to send notification
function sendNotification(phoneNumber, message, done, job) {
    if (BLACKLISTED_NUMBERS.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}
