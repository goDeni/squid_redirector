from os import system

system("sudo apt-get install squid -y")
system("mkdir /build ")
system("cp redirector.py /build/")

try:
	text = open('/etc/squid/squid.conf', 'r').read()
	new_text = 'url_rewrite_extras "%>a %>rm %un"\nurl_rewrite_children 1\nurl_rewrite_program /build/redirector.py\n'
	if not new_text in text:
		text = new_text + text
	open('/etc/squid/squid.conf', 'w').write(text)
except:
	system('cp squid.conf /etc/squid/')
system('cp config.json /build/')
system("chmod -R 777 /build")
system("systemctl restart squid")
system("echo 'All done!'")
