import requests
from bs4 import BeautifulSoup
import re

url = 'http://asahi.5ch.net/test/read.cgi/newsplus/1568417189/'
soup = BeautifulSoup(requests.get(url).text, 'lxml')

thread = soup.find('div', class_ = 'thread')

for child in thread.children:
	if not 'id' in child.attrs:
		continue
	i = child['id']
	if not i.isdigit():
		continue
	name = child.find('span', class_ = 'name').string
	date = child.find('span', class_ = 'date').string
	uid = child.find('span', class_ = 'uid').string.replace('ID:', '')
	message = child.find('div', class_ = 'message').get_text('\n').strip()
	print(i, name, date, uid)
	print(message)

# 	d.append({'name': name, 'date': date, 'uid': uid, 'message': message})