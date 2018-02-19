from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import re
import json
import os.path

class Site:
	def __init__(self, url, titulo, especie):
		self.url = url
		self.titulo = titulo
		self.especie = especie


with open("lista.txt", "r") as texts:
	for text in texts:
		texto = text
		html = "https://www.google.com.br/search?dcr=0&source=hp&q="

		pagina = 0
		url = html + texto
		url = url.replace(' ', '+')

		req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		soup = BeautifulSoup(urlopen(req).read(),"html.parser")

		#regex
		reg = re.compile(".*&sa=")

		#lista de objetos
		lista = []

		#Parsing web urls
		for item in soup.find_all('h3', attrs={'class': 'r'}):
			line = (reg.match(item.a['href'][7:]).group())
			temp = Site(line, item.a.text, text)
			lista.append(temp)

		json_string = ""
		if os.path.exists("data.json"):
			with open("data.json", "r") as f:
				json_string = f.read()

		if len(json_string) > 0:
			data = json.loads(json_string)
			for item in data:
				temp = Site(item["url"], item["titulo"], especie)
				lista.append(temp)

		json_string = json.dumps([ob.__dict__ for ob in lista])

		with open("data.json", "w") as f:
			f.write(json_string)
