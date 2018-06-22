#!/usr/bin/env python3
import sys
import json
import logging
from datetime import datetime
from os.path import getmtime

FILENAME = '/build/config.json'

logging.basicConfig(filename='/build/logs.log',level=logging.DEBUG)



def main():
	redirect_urls = json.load(open(FILENAME))
	time_change = int(getmtime(FILENAME))
	request  = sys.stdin.readline()
	while request:
		logging.debug(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '------------------------------------------------')
		if (time_change != int(getmtime(FILENAME))):
			redirect_urls = json.load(open(FILENAME))
			time_change = int(getmtime(FILENAME))
		logging.debug(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' request: ' + request )
		request = request.split(' ')
		logging.debug(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' url: ' + request[0] +'\n')
		response = '' 
		for url in redirect_urls.keys():
			if url in request[0]:
				response = 'OK rewrite-url="{}"'.format(redirect_urls[url])
				break 
		if response:
			logging.debug(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' redirect: ' + response +'\n')
		sys.stdout.write(response + "\n")
		sys.stdout.flush()
		request = sys.stdin.readline()


if __name__ == "__main__":
	main()