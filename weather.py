import requests
api_key = '2a1ac38a32354cb7b19133643251408'
cidade = input('Digite o nome da cidade: ').strip()
url= f'https://api.weatherapi.com/v1/current.json'

parametros ={
    'key':api_key,
    'q':cidade,
    'lang':'pt'
}

resposta = requests.get(url, params=parametros)

if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados['current']['temp_c']
    descricao = dados['current']['condition']['text']
    print(f'Temperatura na cidade {cidade} é {temperatura}ºC.')
    print(f'Descrição: {descricao}')
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)

