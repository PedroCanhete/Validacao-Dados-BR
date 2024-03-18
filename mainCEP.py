import requests
from ClasseCEP import CEP

cep = "38408218"
teste = CEP(cep)
print(teste.acessa_via_cep())

