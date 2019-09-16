import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import re
import numpy as np
import MeCab
# import gensim
# from gensim import corpora

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
replyRe = re.compile(r'>>\d+', flags = re.A)
urlRe = re.compile(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', flags = re.A)

url = 'http://asahi.5ch.net/test/read.cgi/newsplus/1568417189/'
soup = BeautifulSoup(requests.get(url).text, 'lxml')

thread = soup.find('div', class_ = 'thread')
frequency = defaultdict(int)

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
	body = message
	if replyRe.match(message):
		print('This is reply')
		body = replyRe.sub('', body)
	urls = urlRe.findall(message)
	if len(urls) > 0:
		print('This is url', urls)
		body = urlRe.sub('', body)
	body = body.strip()

	words = []
	for info in mecab.parse(body).splitlines()[:-1]:
		(surface, feature) = info.split('\t')
		print(surface, feature)
		frequency[surface] += 1
		words.append(surface)
		# if feature.startswith('名詞'):
		# 	words.append(surface)
	print(i, name, date, uid)
	# print(words)
print(frequency)
# 	d.append({'name': name, 'date': date, 'uid': uid, 'message': message})