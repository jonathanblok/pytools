# Script that checks the BoC website for changes

import sys 
import hashlib
import urllib.request
import webbrowser

url = 'http://www.boardsofcanada.com';
expectedUrl = 'https://bleep.com/artist/78-boards-of-canada';
prevHash = 'b40948e552196ba7dfb2e823b15afce7';

response = urllib.request.urlopen(url)
html = response.read()
md5HashLib = hashlib.md5();
md5HashLib.update(html);
currentHash = md5HashLib.hexdigest();

if(response.url!=expectedUrl):
	print('New redirect..: '+response.url);
else:
	print('No change detected..');

#if(currentHash != prevHash) :
#	print('Hashes do not match: ('+prevHash+') and ('+currentHash+')');
#	webbrowser.open(url);
#else:
#	print('No change detected..');





