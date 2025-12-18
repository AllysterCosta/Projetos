# Sistema de login usando Flask

from flask import Flask
from flask import render_template, request, redirect, flash
import json
import os

app = Flask(__name__)

# Configuração da chave secreta para sessões e flash messages , usada chave exposta por razões didáticas
app.config['SECRET_KEY'] = 'PROJETOLOGINALLY'

# Ajustando o diretório de trabalho
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, 'usuarios.json')

# Criando rotas


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get('nome')
    senha = request.form.get('senha')

    with open(JSON_PATH, 'r') as tempuser:
        users = json.load(tempuser)

        cont = 0
        for user in users:
            cont += 1
            if user['nome'] == nome and user['senha'] == senha:
                return render_template('usuarios.html')
            if cont >= len(users):
                flash('Usuário ou senha incorretos. Tente novamente.')
                return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
