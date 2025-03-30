const express = require('express');
const app = express();
app.get('/api', (req, res) => res.send('Receipt API'));
module.exports = app;