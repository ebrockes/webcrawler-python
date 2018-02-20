import os.path
import json
import requests
from break_url import URL
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

# 1. Read file urls.json from break_url.py
url_string = ""
if os.path.exists("urls.json"):
	with open("urls.json", "r", encoding="utf-8") as u:
		url_string = u.read()

lista_u = []
if len(url_string) > 0:
	data = json.loads(url_string)
	for item in data:
		temp = URL(item["domain"], item["text"], item["url"])
		lista_u.append(temp)

# 2. Read file with words to be ignored
words = []
with open("ignore.txt", "r", encoding="utf-8") as w:
	for word in w:
		words.append(word.replace('\n',''))

#TODO
# 3. Retrieve sites to be ignored


# 4. Retrieve most common words used
terms = []
for item in lista_u:
	r = requests.get(item.url)

	# Get words from paragraphs
	soup = BeautifulSoup(r.content, "lxml")
	text_p = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
	c_p = Counter((x.rstrip(punctuation).lower() for y in text_p for x in y.split()))

	for text, count in c_p.most_common(200):
		if text not in words:
			terms.append(text)

#TODO
# 4. Save json file words.json: domain, text, url, dictionary of words and occurrencies

