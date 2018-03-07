import os.path
import json
from model import Word, URL
from bs4 import BeautifulSoup
import requests
import urllib
import re

# Read words.json
word_string = ""
if os.path.exists("words.json"):
	with open("words.json", "r", encoding="utf-8") as w:
		word_string = w.read()

lista_w = []
if len(word_string) > 0:
	data = json.loads(word_string)
	for item in data:
		temp = Word(item["url"], item["lista_ok"], item["lista_notok"])
		lista_w.append(temp)


# Read urls.json
url_string = ""
with open("data.json", "r", encoding="utf-8") as u:
	data_string = u.read()

if len(data_string) > 0:
	data = json.loads(data_string)
	for item in data:
		url = item["url"]

		if url.startswith('http'):

			# Read words.txt -> get words related and not related
			ok = ""
			notok = ""
			word = ""
			with open("words.txt", "r", encoding="utf-8") as words:
				for text in words:
					temp = text.split(":")
					word = temp[0].strip()
					if word == item["texto"]:
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


			#count ocurrences of words
			result_ok = []
			r = requests.get(urllib.parse.unquote(url))
			if r.status_code == requests.codes.ok:
				soup = BeautifulSoup(r.content, 'lxml')
				for word in lista_ok:
					number = len(soup(text=re.compile(word)))
					tuple = (word, number)
					result_ok.append(tuple)

				result_notok = []
				for word in lista_notok:
					number = len(soup(text=re.compile(word)))
					tuple = (word, number)
					result_notok.append(tuple)

			temp = Word(url, result_ok, result_notok)
			lista_w.append(temp)

json_string = json.dumps([ob.__dict__ for ob in lista_w])

with open("words.json", "w", encoding="utf-8") as f:
	f.write(json_string)
