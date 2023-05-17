import requests

lista = []
laskuri = 0
while laskuri <5:
    response = requests.get('https://catfact.ninja/fact')
    lista.append(response.json())
    laskuri+=1

print(lista)





