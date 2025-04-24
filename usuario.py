import json
import os

def salvar_usuario(nome, senha, idade, email):
    # Garante que o arquivo existe
    if not os.path.exists('dados.json') or os.stat('dados.json').st_size == 0:
        with open('dados.json', "w") as f:
            json.dump({}, f)  # Se o arquivo não existir, cria um arquivo vazio

    # Lê os dados do arquivo
    with open('dados.json', "r") as f:
        dados = json.load(f)

    # Verifica se o usuário já existe
    if nome in dados:
        return False

    # Adiciona o novo usuário
    dados[nome] = {
        "senha": senha,
        "idade": idade,
        "email": email
    }

    # Grava de volta no arquivo
    with open('dados.json', "w") as f:
        json.dump(dados, f, indent=4)
        
    return True

def verificar_login(nome, senha):
    # Lê os dados do arquivo
    with open('dados.json', "r") as f:
        dados = json.load(f)

    # Verifica se o usuário existe e se a senha bate
    if nome in dados and dados[nome]['senha'] == senha:
        return True
    return False
