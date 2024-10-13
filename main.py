import requests

# Método encode_params solo disponible en versiones antiguas (pre-2.3.0)
params = {'key1': 'value1', 'key2': 'value2'}

# En las versiones antiguas de requests, encode_params era público
encoded_params = requests.request.encode_params(params)

# Utilizando los parámetros codificados en una solicitud GET
url = "http://httpbin.org/get?" + encoded_params
response = requests.get(url)

# Mostrando la respuesta
print("URL con parámetros codificados:", url)
print("Respuesta del servidor:", response.json())
