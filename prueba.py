print("Inicio")

import requests

print("Antes de enviar")

url = "http://127.0.0.1:5000/pedido"

data = {
    "nombre": "Ana",
    "telefono": "3001234567",
    "direccion": "Bogota",
    "producto": "Acetaminofen",
    "cantidad": 3
}

respuesta = requests.post(url, json=data)

print("Respuesta:")
print(respuesta.json())