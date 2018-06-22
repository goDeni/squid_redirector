#!/usr/bin/env python3
import sys
import json
import logging
from datetime import datetime
from os.path import getmtime
import re

FILENAME = '/build/config.json'

logging.basicConfig(filename='/build/logs.log',level=logging.DEBUG)

def getList():
	try:
		l = json.load(open(FILENAME))
	except FileNotFoundError:
		json.dump({},open(FILENAME, 'w'))
		return getList()
	return l

def main():
	redirect_urls = getList()
	time_change = int(getmtime(FILENAME))
	request  = sys.stdin.readline()
	response = '' 
	logging.debug(datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
		+ '------------------------------------------------')
	
	if (time_change != int(getmtime(FILENAME))):
		redirect_urls = getList()
		time_change = int(getmtime(FILENAME))
	
	logging.debug(datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
		+ ' request: {}'.format(request) )
	
	url, ip, method = request.split(' ')[:3]

	if method == "CONNECT":
		url = url.replace('www.','')
		url = url.split(':')[0]
	elif method == "GET":
		url = re.findall(r'http://www\.\w*\.\w{2,3}/?',url)[0]

	# 'www\.\w*\.\w{2,3}' - www.yandex.ru
	# 'http://www\.\w*\.\w{2,3}/?' - http://www.yandex.ru/
	
	logging.debug(datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
		+ ' url: {} method: {}'.format(url,method))
	
	
	if url in redirect_urls.keys():
		response = 'OK rewrite-url="{}"'.format(redirect_urls[url])
	
	if response:
		logging.debug(datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
			+ 'redirect: ' + response)
	sys.stdout.write(response + "\n")
	sys.stdout.flush()

if __name__ == "__main__":
	main()
