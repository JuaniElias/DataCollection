from bs4 import BeautifulSoup
import requests

url = "https://www.argenprop.com/departamento-alquiler-partido-rosario"
# Manda la GET request
f = requests.get(url=url)
# Parsing
doc = BeautifulSoup(f.text, "html.parser")
# FindAll
precios = doc.findAll("span", {"class": "card__currency"})
print("Precios:")
for precio in precios:
    print(precio.nextSibling.text.strip())
