let shamir = require('./lib.js');
let decimal = require('decimal.js');
let crypto = require('crypto');

const api_key = "72e072a4a8f3d664db60cce141e7c735";
// Generate RSA pair (public,private)
const keys = shamir.generateKeys();
// split the keys.private into 2 shares with minimun of 2 required
var shares = shamir.split(keys.private, 2, 2);
// send email containing the shares hash to the prof and delegue
const share1_hash = shares[0].hash;
const share2_hash = shares[1].hash;
// send the shares to the api
//shamir.sendToServer(shares, api_key);

// just some verbosity
console.log('Private key:  ', keys.private);
console.log('Share1 hash:  ', share1_hash);
console.log('Share2 hash:  ', share2_hash);