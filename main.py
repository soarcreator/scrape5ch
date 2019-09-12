import requests
from bs4 import BeautifulSoup
import re

url = 'http://asahi.5ch.net/test/read.cgi/newsplus/1568105477/'
soup = BeautifulSoup(requests.get(url).text, 'lxml')

thread = soup.find('div', class_ = 'thread')

d = []
for i in range(1, 1001):
	post = thread.find('div', id = str(i))
	name = post.find('span', class_ = 'name').string
	date = post.find('span', class_ = 'date').string
	uid = post.find('span', class_ = 'uid').string.replace('ID:', '')
	message = post.find('div', class_ = 'message').get_text('\n').strip()
	d.append({'name': name, 'date': date, 'uid': uid, 'message': message})