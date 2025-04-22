from flask import Flask, render_template, request, redirect, url_for, flash, session
import json
from backend.usuario import salvar_usuario, verificar_login

app = Flask(__name__)
app.secret_key = 'segredo'

@app.route('/')
def index():
    return render_template('index.html')

def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        idade = request.form['idade']
        email = request.form['email']

        salvar_usuario(nome, senha, int(idade), email)  # sem try
        flash('Cadastro realizado com sucesso! Faça login.')
        return redirect(url_for('login'))

    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        if verificar_login(nome, senha):
            session['usuario'] = nome
            flash('Login bem-sucedido!')
            return redirect(url_for('home'))
        else:
            flash('Nome de usuário ou senha incorretos.')
    return render_template('login.html')

@app.route('/home')
def home():
    usuario = session.get('usuario')
    dados_usuario = None
    print(f'Usuário logado: {usuario}')  # <-- veja isso no terminal

    if usuario:
        with open("dados.json", "r") as f:
            dados = json.load(f)
            dados_usuario = dados.get(usuario)
            print(f'Dados do usuário: {dados_usuario}')  # <-- veja isso também

    return render_template('home.html', usuario=usuario, dados=dados_usuario)

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Você saiu com sucesso.')
    return redirect(url_for('login'))

from random import randint

@app.route('/maquina', methods=['GET', 'POST'])
def caca_niquel():
    resultado = None
    if request.method == 'POST':
        numeros = [randint(1, 8), randint(1, 8), randint(1, 8)]
        if numeros[0] == numeros[1] == numeros[2]:
            resultado = f"Você encontrou o niquel! Números: {numeros}"
        else:
            resultado = f"Você não encontrou o niquel. Números: {numeros}"
    return render_template('caca_niquel.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
