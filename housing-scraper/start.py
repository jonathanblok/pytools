# Script that checks the BoC website for changes

import sys 
import hashlib
import urllib.request
import webbrowser

# urls for sites to scrape
pararius_url = https://www.pararius.nl/
woningnet_url = https://www.woningnetregioutrecht.nl/

# get hash from response
def hash_response(response):
	md5hashlib = hashlib.md5()
	md5HashLib.update(html)
	currentHash = md5HashLib.hexdigest()
	return currentHash

def get_html_response(url):
	response = urllib.request.urlopen(url)
	html_respnse = response.read()
	return html_reponse

def main():
    # my code here

if __name__ == "__main__":
    main()
