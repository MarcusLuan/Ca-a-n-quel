from flask import Flask, render_template, request, redirect, url_for, flash, session
import json, os
from usuario import salvar_usuario, verificar_login, adicionar_dinheiro, apostar

app = Flask(__name__)
app.secret_key = 'segredo'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=["GET","POST"])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        idade = request.form['idade']
        email = request.form['email']

        autenticado = salvar_usuario(nome, senha, int(idade), email)  # sem try
        if autenticado:
            flash('Cadastro realizado com sucesso! Faça login.')
            return redirect(url_for('login'))
        else:
            flash('Usuário já existe! Tente um nome diferente.')
    
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

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('usuario', None)
    flash('Você saiu com sucesso.')
    return redirect(url_for('login'))

from random import randint

@app.route('/maquina', methods=['GET', 'POST'])
def caca_niquel():
    resultado = None
    usuario = session.get('usuario')

    if request.method == 'POST':
        valor_aposta = float(request.form['aposta'])
        
        if usuario:
            resultado = apostar(usuario, valor_aposta)

    with open('dados.json', "r") as f:
        dados = json.load(f)
    
    return render_template('maquina.html', resultado=resultado, dados=dados.get(usuario))

@app.route('/adicionar_dinheiro', methods=['POST'])
def adicionar_dinheiro_route():
    valor = float(request.form['valor'])
    usuario = session.get('usuario')
    
    if usuario and valor > 0:
        if adicionar_dinheiro(usuario, valor):
            flash(f"Você adicionou R${valor} ao seu saldo.")
        else:
            flash("Erro ao adicionar dinheiro.")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
