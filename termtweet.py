#!/usr/bin/env python

import oauth2 as oauth
import urllib2 as urllib
import json

access_token_key = ""
access_token_secret = ""

consumer_key = ""
consumer_secret = ""

_debug = 0

oauth_token = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_handler = urllib.HTTPHandler(debuglevel = _debug)
https_handler = urllib.HTTPSHandler(debuglevel = _debug)

'''
Construct, sign and open twitter session
'''

def twitterreq(url, method, parameters):
	http_method = method
	req = oauth.Request.from_consumer_and_token(oauth_consumer, token=oauth_token,http_method=http_method, http_url=url, parameters=parameters)
	req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)
	headers = req.to_header()

	if http_method == "POST":
		encoded_post_data = req.to_postdata()
	else:
		encoded_post_data = None
		url = req.to_url()

	opener = urllib.OpenerDirector()
	opener.add_handler(http_handler)
	opener.add_handler(https_handler)
	response = opener.open(url, encoded_post_data)

	return response

def send_tweet():
	url = "https://api.twitter.com/1.1/statuses/update.json"
	uinput = raw_input("Enter up to 140 characters:")
	parsed_input = process_input(uinput)
	parameters = {"status": parsed_input}
	response = twitterreq(url, "POST", parameters)

def process_input(uinput):
	if len(uinput) > 140:
		return uinput[:141]
	return uinput


def debug_response(resp):
	for line in resp:
		print line


if __name__ == '__main__':
	send_tweet()
