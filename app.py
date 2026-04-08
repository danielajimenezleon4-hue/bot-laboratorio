from flask import Flask, request, jsonify

app = Flask(__name__)

pedidos = {}

@app.route('/')
def home():
    return "Servidor funcionando"

@app.route('/pedido', methods=['POST'])
def crear_pedido():
    data = request.json
    pedido_id = len(pedidos) + 1
    pedidos[pedido_id] = {"estado": "En proceso", "data": data}
    return jsonify({"mensaje": "Pedido creado", "id_pedido": pedido_id})

@app.route('/estado/<int:pedido_id>', methods=['GET'])
def estado(pedido_id):
    if pedido_id in pedidos:
        return jsonify(pedidos[pedido_id])
    else:
        return jsonify({"error": "Pedido no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)