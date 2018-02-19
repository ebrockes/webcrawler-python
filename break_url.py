import os.path
import json
from urllib.parse import urlparse

class Domain:
	def __init__(self, domain):
		self.domain = domain

class URL:
	def __init__(self, domain, text, url):
		self.domain = domain
		self.text = text
		self.url = url


# 1. Read json file data.json
json_string = ""

if os.path.exists("data.json"):
	with open("data.json", "r", encoding="utf-8") as f:
		json_string = f.read()

urls = []
especies = []
if len(json_string) > 0:
	data = json.loads(json_string)
	for item in data:
		urls.append(item["url"])
		especies.append(item["especie"])


# 2. Create json file domains.json
domains_string = ""
if os.path.exists("domains.json"):
	with open("domains.json", "r") as d:
		domains_string = d.read()

domains = set()
if len(domains_string) > 0:
	data = json.loads(domains_string)
	for item in data:
		domains.add(item["domain"])

for url in urls:
	domain = urlparse(url).netloc
	domains.add(domain)

lista_d = []
for domain in domains:
	temp = Domain(domain)
	lista_d.append(temp)

json_string = json.dumps([ob.__dict__ for ob in lista_d])

with open("domains.json", "w") as d:
	d.write(json_string)


# 3. Create json file urls_text.json
urls_string = ""
lista_u = []
if os.path.exists("urls.json"):
	with open("urls.json", "r", encoding="utf-8") as u:
		urls_string = u.read()

if len(urls_string) > 0:
	data = json.loads(urls_string)
	for item in data:
		temp = URL(item["domain"], item["text"], item["url"])
		lista_u.append(temp)

index = 0
for url in urls:
	domain = urlparse(url).netloc
	texto = especies[index]
	if domain != '':
		temp = URL(domain, texto, url)
		lista_u.append(temp)
	index = index + 1

urls_string = json.dumps([ob.__dict__ for ob in lista_u])

with open("urls.json", "w", encoding="utf-8") as u:
	u.write(urls_string)
