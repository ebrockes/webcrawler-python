from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import re
import json
import os.path
from model import Site

with open("lista.txt", "r", encoding="utf-8") as texts:
	for text in texts:
		word = text.strip()

		texto = text.strip()
		texto = '"' + texto.replace(" ", "+") + '"' + '+"venda"'
		html = "https://www.google.com.br/search?dcr=0&source=hp&q="
		pagina = 0
		url = html + texto

		req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		soup = BeautifulSoup(urlopen(req).read(),"html.parser")

		#regex
		reg = re.compile(".*&sa=")

		#Parsing web urls
		lista = []
		for item in soup.find_all('h3', attrs={'class': 'r'}):
			line = (reg.match(item.a['href'][7:]).group())
			temp = Site(line, item.a.text, word)
			lista.append(temp)

		json_string = ""
		if os.path.exists("data.json"):
			with open("data.json", "r", encoding="utf-8") as f:
				json_string = f.read()

		if len(json_string) > 0:
			data = json.loads(json_string)
			for item in data:
				temp = Site(item["url"], item["titulo"], item["texto"])
				lista.append(temp)

		json_string = json.dumps([ob.__dict__ for ob in lista])

		with open("data.json", "w", encoding="utf-8") as f:
			f.write(json_string)
