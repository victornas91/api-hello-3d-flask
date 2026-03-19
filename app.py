from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000', 'http://127.0.0.1:3000'])

@app.route('/')
def home():
    return 'API está funcionando! Acesse /api/feliz ou /api/triste'

@app.route('/api/feliz')
def rota_feliz():
    return jsonify({
        'status': 'feliz',
        'message': 'Estou feliz! 😊',
        'color': '#ffff00'
    })

@app.route('/api/triste')
def rota_triste():
    return jsonify({
        'status': 'triste',
        'message': 'Estou triste! 😢',
        'color': '#0000ff'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)