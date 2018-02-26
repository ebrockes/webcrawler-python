class Site:
	def __init__(self, url, titulo, texto):
		self.url = url
		self.titulo = titulo
		self.texto = texto

class Domain:
	def __init__(self, domain):
		self.domain = domain

class URL:
	def __init__(self, domain, text, url, title):
		self.domain = domain
		self.text = text
		self.url = url
		self.title = title


class Word:
	def __init__(self, url, lista_ok, lista_notok):
		self.url = url
		self.lista_ok = lista_ok
		self.lista_notok = lista_notok
