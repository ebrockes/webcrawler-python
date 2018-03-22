from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import re
import json
import os.path
from model import Site
import time
import random

contador = 0
limite = contador + 1500

with open("lista.txt", "r", encoding="utf-8") as texts:
	for text in texts:
		for i in range(contador, limite, 10):
			word = text.strip()

			texto = text.strip()
			texto = '"' + texto.replace(" ", "+") + '"' + '+"venda"'
			html = "https://www.google.com.br/search?dcr=0&source=hp&start="+str(i)+"&q="
			url = html + texto
			print(url)


			tempo = 0
			if i > contador:
				tempo = 1800 # 30 min
				tempo = tempo + (random.random() * 120)
			time.sleep(tempo)
			print("dorme " + str(tempo/60) + " min")


			print("realiza web crawling")
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
			print("web crawl registros: " + str(len(lista)))

			if len(lista) == 0:
				print("fim")
				break

			json_string = ""
			if os.path.exists("data.json"):
				with open("data.json", "r", encoding="utf-8") as f:
					json_string = f.read()

			if len(json_string) > 0:
				data = json.loads(json_string)
				for item in data:
					temp = Site(item["url"], item["titulo"], item["texto"])
					lista.append(temp)
				print("total registros " + str(len(lista)))

			json_string = json.dumps([ob.__dict__ for ob in lista])
			print("json string len " + str(len(json_string)))

			with open("data.json", "w", encoding="utf-8") as f:
				f.write(json_string)

			print("finaliza")
