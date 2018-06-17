# wicked_game

Find out what local radio stations that could be playing Chris Isaak's classic "Wicked Game". It will send push notifications when and if a radio station is playing it in Gainesville, Florida. 

Getting started, get your Rdio API keys: 

```
RDIO_API_KEY
RDIO_API_SECRET
```

You get these variables from the Rdio developer site (sign in and create a new app):

http://developer.rdio.com/

Additionally, you'll need this variable for the echo nest api:

An easy way to set up your vars is to create a file called env.sh and make it look like this:

```
export RDIO_API_KEY=yourkey
export RDIO_API_SECRET=yoursecret
export ECHO_NEST_API_KEY=yourkey
export APP_SECRET=secret
```

Then just type ```source env.sh``` before you run your app locally, and it will essentially build it for you. Just make sure not to commit your env.sh file.
