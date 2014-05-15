#!/usr/bin/env python

import oauth2 as oauth
import urllib2 as urllib
import HTMLParser
import json

access_token_key = ""
access_token_secret = ""


consumer_key = ""
consumer_secret = ""

oauth_token = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_handler = urllib.HTTPHandler(debuglevel = 0)
https_handler = urllib.HTTPSHandler(debuglevel = 0)

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
	print "Tweeted: "+parsed_input+"\n"

def get_my_timeline():
	print "\n"
	html_parser =  HTMLParser.HTMLParser()
	url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
	parameters = {"count": 50}
	response = twitterreq(url, "GET", parameters)
	resp = json.loads(response.read())
	for line in resp:
		print "@"+line["user"]["screen_name"]+ ": "+html_parser.unescape(line["text"])
		print "\n"

def process_input(uinput):
	if len(uinput) > 140:
		return uinput[:141]
	return uinput

def debug_response(resp):
	for line in resp:
		print line

def main_menu():
	while (True):
		choice = raw_input("Here are your options following options:"+"\n"+
			"Type 'tweet' to start composing a new tweet"+"\n" +
			"Type 'timeline' to get your 50 most recent tweets on your timeline"+"\n" +
			"Type 'exit' to exit"+"\n").strip()
		if choice == "tweet":
			send_tweet()
		elif choice == "timeline":
			get_my_timeline()
		elif choice == "exit":
			return
		else:
			print "\n"


if __name__ == '__main__':
	main_menu() 
