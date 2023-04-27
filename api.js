const express = require('express');
const app = express();

// Define an endpoint to return a JSON response
app.get('/hello', (req, res) => {
  const message = { message: 'Hello, world!' };
  res.json(message);
});
// Set up a route to handle a PUT request to /users/:id
// Set up a route to handle a PUT request to /users/:id
// Set up a route to handle a PUT request to /users/:id
// Set up a route to handle a PUT request to /users/:id
app.put('/users/:id', (req, res) => {
    const userId = req.params.id;
    const data = req.body;
    // Do something with the data and user ID...
    res.send(`Received PUT request for user ${userId} with data ${JSON.stringify(data)}`);
});

app.post('/users', (req, res) => {
    const data = req.body;
    // Do something with the data...
    // Do something with the data...
    res.send(`Received POST request for new user with data ${JSON.stringify(data)}`);
});
// Start the server
app.listen(3000, () => console.log('Server is running on port 3000'));
console.log("hhh")