import { createQueue, Job } from 'kue';

// Array of blacklisted phone numbers
const BLACKLISTED_NUMBERS = [4153518780, 4153518781];
// Create a Kue queue
const queue = createQueue();

// Function to send notification
function sendNotification(phoneNumber, message, done, job) {
    if (BLACKLISTED_NUMBERS.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}
