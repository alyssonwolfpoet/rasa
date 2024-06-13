import requests

request = requests.get('https://v2.jokeapi.dev/joke/Any?lang=pt').json()  # make an api call
pergunta = request['setup']
resposta = request['delivery']
print(request)
print(pergunta)
print(resposta)
