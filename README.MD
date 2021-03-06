# wicked_game

![Screenshot](notification.png)

For context,

https://www.youtube.com/watch?v=dlJew-Dw87I

## Usage

Find out what local radio stations that could be playing Chris Isaak's classic "Wicked Game". It will send push notifications when and if a radio station is playing it in Gainesville, Florida. 

Getting started, get your Rdio (now Pandora) API keys: 

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
export APP_SECRET=secret
```
Then just type ```source env.sh``` before you run your app locally, and it will essentially build it for you. Just make sure not to commit your env.sh file.

## The 151 Flag 

You can see when certain parts of Chris Isaak's - Wicked Game are playing, so my favorite part is 1:51 -- so let's say I just want a push notification when the song hits 1:51 you'd run, this only works from radio stations in Gainesville, FL though -- so if you run the 151 flag expecting San Francisco, it wouldn't work. You can change this by editing the ```gainesville.py``` file.

```
python3 gainesville.py -151
```
