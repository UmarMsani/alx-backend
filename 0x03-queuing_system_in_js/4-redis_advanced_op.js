import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Function to create a hash in Redis
client.hset(
  'HolbertonSchools',
  {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2,
  },
  redis.print
);

// Function to display the hash stored in Redis
client.hgetall('HolbertonSchools', (err, reply) => {
  console.log(reply);
});
