termtweet
=========

A simple python script that establishes a connection to Twitter and allows you to write a tweet from the terminal. Thanks to Twitter's
awesome API, hashtags(#) and user mentions (@) are supported out of the box. 

Setup
=======

Dependencies: oauth2 library for Python.

You'll need to register the script as your own app at Twitter's developer center. Yes, this means that you'll have to supply your own
customer key and secret as well as generate your own access token and keys. To add these, just edit the code where relevant.

If you want to avoid typing `python termtweet.py` every time, give it execute permissions.


Things to do
=============

Support adding media (pics and links) to tweets. The current functionality is pretty basic (just an excuse for me to mess around with
Twitter's API). 

Might also look into making it easier to setup the script - ideally someone can just download the script and authorize it as an app 
quickly.
