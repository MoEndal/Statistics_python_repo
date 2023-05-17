import requests

list = []
counter = 0
while counter <5:
    response = requests.get('https://catfact.ninja/fact')
    list.append(response.json())
    counter+=1

print(list)





