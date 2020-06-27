# Shamir Secret Sharing - API

This is a Lib written in Node.js to help sharing a secret such as <br>
an RSA private key between multiple entities using Shamir Secret Sharing algorithm. <br>
To help make it more secure, i developed an API with Flask, exposing the following endpoints:

[GET] **/share**   request all available shares stored on the database. THIS SHOULD BE REMOVED IN PRODUCTIONS APPS.

[POST] **/share**  add a new share on the server

[GET] **/share/\<hash\>**  get a specific share by specifiying its hash

[DELETE] **/shares**   delete all shares. THIS SHOULD BE REMOVED IN PRODUCTIONS APPS.

# How to use

Run the api in background

`nohup python3 api.y &`


Install dependencies

`npm install`

Split private key and send it to server

`node split.js`

Retrieve shares from the server

`node reconstruct.py`
