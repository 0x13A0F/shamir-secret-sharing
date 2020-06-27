let shamir = require('./lib.js');
let decimal = require('decimal.js');

// i put all the code in async function so that i can use 'await'
async function main() {
    const api_key = "72e072a4a8f3d664db60cce141e7c733";
    const share1_hash = "da32e04c447a0d788ba5533cc7b318742e806d0a827a7655d97223c4f13e759b";
    const share2_hash = "5879f70c95d583654c8c47b7d859afb2bb5e6e30ce746ee2e2628fdc0d58e7d6";
    share1 = (await shamir.getShareFromServer(api_key, share1_hash)).data;
    share2 = (await shamir.getShareFromServer(api_key, share2_hash)).data;
    console.log(share1);
    console.log(share2);
    // reconstruct the secret key
    const rsa_private_key = shamir.reconstruct([share1, share2]);
    console.log(rsa_private_key.toHex());
}

main();