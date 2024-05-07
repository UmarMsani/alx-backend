import redis from 'redis';

// Create a Redis publisher client
const client = redis.createClient();

// Event listener for successful connection
client.on('connect', function() {
  console.log('Redis client connected to the server');
});

/ Event listener for connection error
client.on('error', function(err) {
  console.log('Redis client not connected to the server: ' + err);
});

// Function to publish a message after a specified time
client.subscribe('holberton school channel');

client.on('message', function(channel, message) {
  console.log('Message received on channel ' + channel + ': ' + message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
