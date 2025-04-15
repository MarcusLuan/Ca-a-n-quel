from flask import Flask, render_template, request, redirect, url_for, flash
from backend.usuario import salvar_usuario, verificar_login

app = Flask(__name__)
app.secret_key = 'segredo'  # Necessário pro flash funcionar

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        idade = request.form['idade']
        email = request.form['email']
        salvar_usuario(nome, senha, int(idade), email)
        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('index'))
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        if verificar_login(nome, senha):
            flash('Login bem-sucedido!')
            return redirect(url_for('index'))
        else:
            flash('Nome de usuário ou senha incorretos.')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
