import os.path
import json
from model import Word, URL
from bs4 import BeautifulSoup
import requests

def count_words(url, word):
	try:
		r = requests.get(url, allow_redirects=False)
	except requests.exceptions.Timeout:
		return None
	except requests.exceptions.RequestException as e:
		return None
	soup = BeautifulSoup(r.content, 'lxml')
	words = soup.find(text=lambda text: text and word in text)
	if words:
		return len(words)
	else:
		return 0


# Read words.json
word_string = ""
if os.path.exists("url_words.json"):
	with open("url_words.json", "r", encoding="utf-8") as w:
		word_string = w.read()

lista_w = []
if len(word_string) > 0:
	data = json.loads(word_string)
	for item in data:
		temp = Word(item["url"], item["lista_ok"], item["lista_notok"])
		lista_w.append(temp)

# Read urls.json
url_string = ""
with open("urls.json", "r", encoding="utf-8") as u:
	url_string = u.read()

if len(url_string) > 0:
	data = json.loads(url_string)
	for item in data:
		url = URL(item["domain"], item["text"], item["url"], item["title"])

		# Read words.txt -> get words related and not related
		ok = ""
		notok = ""
		word = ""
		with open("words.txt", "r", encoding="utf-8") as words:
			for text in words:
				temp = text.split(":")
				word = temp[0].strip()
				if word == item["text"]:
					ok = temp[1].strip()
					notok = temp[2].strip()
					break


		lista_ok = []
		lista_notok = []
		if len(ok) > 0:
			temp = ok.split(",")
			for item in temp:
				lista_ok.append(item.strip())
			temp = notok.split(",")
			for item in temp:
				lista_notok.append(item.strip())


		result_ok = []
		for word in lista_ok:
			number = count_words(url.url, word)
			tuple = (word, number)
			result_ok.append(tuple)

		result_notok = []
		for word in lista_notok:
			number = count_words(url.url, item)
			tuple = (word, number)
			result_notok.append(tuple)


		temp = Word(url.url, result_ok, result_notok)
		lista_w.append(temp)

json_string = json.dumps([ob.__dict__ for ob in lista_w])

with open("words.json", "w", encoding="utf-8") as f:
	f.write(json_string)
