class Site:
	def __init__(self, url, titulo, texto):
		self.url = url
		self.titulo = titulo
		self.texto = texto

class Domain:
	def __init__(self, domain):
		self.domain = domain

# text -> list of domain
# domain -> list of (url, title)
class URL:
	def __init__(self, text, domains):
		self.text = text
		self.domains = domains


class Word:
	def __init__(self, url, lista_ok, lista_notok):
		self.url = url
		self.lista_ok = lista_ok
		self.lista_notok = lista_notok
