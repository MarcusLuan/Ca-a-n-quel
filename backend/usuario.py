import json
import os

# Caminho do arquivo de dados
arquivo_dados = "dados.json"

# Garante que o arquivo existe
if not os.path.exists(arquivo_dados):
    with open(arquivo_dados, "w") as f:
        json.dump({}, f)  # Se o arquivo não existir, cria um arquivo vazio

def salvar_usuario(nome, senha, idade, email):
    # Lê os dados do arquivo
    with open(arquivo_dados, "r") as f:
        dados = json.load(f)

    # Verifica se o usuário já existe
    if nome in dados:
        raise ValueError("Usuário já cadastrado.")

    # Adiciona o novo usuário
    dados[nome] = {
        "senha": senha,
        "idade": idade,
        "email": email
    }

    # Grava de volta no arquivo
    with open(arquivo_dados, "w") as f:
        json.dump(dados, f, indent=4)

    print(f"Usuário {nome} cadastrado com sucesso!")

def verificar_login(nome, senha):
    # Lê os dados do arquivo
    with open(arquivo_dados, "r") as f:
        dados = json.load(f)

    # Verifica se o usuário existe e se a senha bate
    if nome in dados and dados[nome]["senha"] == senha:
        return True
    return False
