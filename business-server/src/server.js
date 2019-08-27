'use strict';

const express = require('express');
const path    = require('path');

// Constants
const PORT = 9999;
const HOST = '0.0.0.0';

// Serve the static files from the React app

// App
const app = express();
app.use(express.static(path.join(__dirname, '/client/build')));

app.get('/', (req,res) =>{
  res.sendFile(path.join(__dirname+'/client/build/index.html'));
});

app.get('/idi', (req, res) => {
  res.send('Idi naxyu\n');
});
  
app.listen(PORT, HOST);

console.log('>>', __dirname);
console.log('>>',process.env.FOO);
console.log(`Running on http://${HOST}:${PORT}`);