# Sendverse
An anonymous chatting server you can deploy for your friends.
See it in action:
https://sendverse-python.herokuapp.com/

#### The software
This repo includes the server side and frontend software required to run your own chatting app. The server is written in Python and the frontend is written in javascript. It uses Flask to serve files, and socket.io, for the the realtime communication between the server and client.

##### Contents
In this repo, you will find the server-side software, *main.py*, and the frontend, deployable software, located in the *static* directory. The frontend src files are located in the *src* directory.

#### Deploy your own
*To clone this repo:*
``` bash
    git clone https://github.com/liam-ilan/sendverse-python.git
```

##### Running the app
*To start up a local server on port 5000:*
``` bash
    npm start
```
note: you will be starting a python server.

#### Development 
*Start up a localhost on port 5000 for python development:*

``` bash
    npm start
```
*For JavaScript development start Webpack:*

``` bash
    npm run js
```

*Lint javascript:*
``` bash
    npm run lint
```

#### Author
I'm Liam Ilan, a 13 year old software developer who is never working, but always playing around.
I thank my dad who is like super duper awesome!!!!1 (not me)