from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# ===== FUNCIÓN PARA GUARDAR =====
def guardar_pedido(nombre, medicamento, cantidad, direccion):
    conn = sqlite3.connect('pedidos.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            medicamento TEXT,
            cantidad INTEGER,
            direccion TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO pedidos (nombre, medicamento, cantidad, direccion)
        VALUES (?, ?, ?, ?)
    ''', (nombre, medicamento, cantidad, direccion))

    conn.commit()
    pedido_id = cursor.lastrowid
    conn.close()

    return pedido_id

# ===== ENDPOINT PRINCIPAL =====
@app.route('/')
def home():
    return "Servidor funcionando"

# ===== ENDPOINT CREAR PEDIDO =====
@app.route('/pedido', methods=['POST'])
def crear_pedido():
    try:
        data = request.get_json(force=True)

        # 🔥 ARREGLO CLAVE DEL NOMBRE
        nombre_data = data.get('nombre')

        if isinstance(nombre_data, dict):
            nombre = nombre_data.get('first', '')
        else:
            nombre = nombre_data

        medicamento = data.get('medicamento')
        cantidad = data.get('cantidad')
        direccion = data.get('direccion')

        # Validación
        if not nombre or not medicamento or not direccion:
            return jsonify({"error": "Datos incompletos"}), 400

        # Guardar en BD
        pedido_id = guardar_pedido(nombre, medicamento, cantidad, direccion)

        return jsonify({
            "mensaje": "Pedido guardado correctamente",
            "id_pedido": pedido_id
        })

    except Exception as e:
        print("ERROR BACKEND:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
