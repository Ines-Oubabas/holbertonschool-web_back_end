const express = require('express');
const app = express();

// Define route for '/'
app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

// Listen on port 1245
app.listen(1245, () => {
    console.log('Express server is running on port 1245');
});

module.exports = app;
