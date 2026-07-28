import requests

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
resposta = requests.get(url, timeout=10)
print("Status:", resposta.status_code) # passo 1: rodar e ver 200

estados = resposta.json() # passo 2: converter
print("Tipo:", type(estados)) # <class 'list'>
print("Quantos estados?", len(estados)) #27
print(estados[0])

for estado in estados:
    if estado["regiao"]["sigla"] == "N":
        print(f' {estado["sigla"]} - {estado["nome"]}')