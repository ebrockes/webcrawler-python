import os.path
import json
from urllib.parse import urlparse
from model import Domain, URL, Site

# 1. Read json file data.json
json_string = ""
lista_s = []
if os.path.exists("data.json"):
	with open("data.json", "r", encoding="utf-8") as f:
		json_string = f.read()

if len(json_string) > 0:
	data = json.loads(json_string)
	for item in data:
		temp = Site(item["url"], item["titulo"], item["texto"])
		lista_s.append(temp)


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

for site in lista_s:
	url = site.url
	domain = urlparse(url).netloc
	domains.add(domain)

lista_d = []
for domain in domains:
	if domain.strip() != "":
		temp = Domain(domain)
		lista_d.append(temp)

json_string = json.dumps([ob.__dict__ for ob in lista_d])

with open("domains.json", "w") as d:
	d.write(json_string)


# 3. Create json file with domain, text, url, title
urls_string = ""
lista_u = []
if os.path.exists("urls.json"):
	with open("urls.json", "r", encoding="utf-8") as u:
		urls_string = u.read()

if len(urls_string) > 0:
	data = json.loads(urls_string)
	for item in data:
		temp = URL(item["domain"], item["text"], item["url"], item["title"])
		lista_u.append(temp)

for item in lista_s:
	url = item.url
	domain = urlparse(url).netloc
	if domain != '':
		temp = URL(domain, item.texto, item.url, item.titulo)
		lista_u.append(temp)

urls_string = json.dumps([ob.__dict__ for ob in lista_u])

with open("urls.json", "w", encoding="utf-8") as u:
	u.write(urls_string)

open("data.json", "w").close()
