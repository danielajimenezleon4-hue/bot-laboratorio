from flask import Flask, request, jsonify

app = Flask(__name__)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response
pedidos = {}

@app.route('/')
def home():
    return "Servidor funcionando"

@app.route('/pedido', methods=['POST'])
def crear_pedido():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400

        nombre = data.get('nombre')
        medicamento = data.get('medicamento')
        cantidad = data.get('cantidad')
        direccion = data.get('direccion')

        pedido_id = len(pedidos) + 1

        pedidos[pedido_id] = {
            "estado": "En proceso",
            "nombre": nombre,
            "medicamento": medicamento,
            "cantidad": cantidad,
            "direccion": direccion
        }

        print("Pedido recibido:", pedidos[pedido_id])

        return jsonify({
            "mensaje": "Pedido creado correctamente",
            "id_pedido": pedido_id
        }), 200

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
