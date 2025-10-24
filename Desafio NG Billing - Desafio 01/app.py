from flask import Flask, jsonify
import os

app = Flask(__name__)

WATCH_DIR = "/arquivos"

@app.route('/arquivos', methods=['GET'])
def listar_arquivos():
    try:
        if not os.path.exists(WATCH_DIR):
            return jsonify({"erro": f"Diretório '{WATCH_DIR}' não encontrado."}), 404
        
        arquivos = os.listdir(WATCH_DIR)
        return jsonify({"arquivos": arquivos})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)