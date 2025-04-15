import json
import os

dados_iniciais = {}

nome_arquivo = "dados.json"
with open(nome_arquivo, "w") as arquivo:
    json.dump(dados_iniciais, arquivo, indent=4)

    #Atualizando
def atualizar(novos_dados):
  with open("dados.json", "r") as arquivo:
      dados_existentes = json.load(arquivo)

  dados_existentes.update(novos_dados)

  with open(nome_arquivo, "w") as arquivo:
      json.dump(dados_existentes, arquivo, indent=4)

  print("Arquivo JSON atualizado com sucesso!")

arquivo_dados = "dados.json"

# Garante que o arquivo existe
if not os.path.exists(arquivo_dados):
    with open(arquivo_dados, "w") as f:
        json.dump({}, f)

def salvar_usuario(nome, senha, idade, email):
    with open(arquivo_dados, "r") as f:
        dados = json.load(f)
    dados[nome] = {
        "senha": senha,
        "idade": idade,
        "email": email
    }
    with open(arquivo_dados, "w") as f:
        json.dump(dados, f, indent=4)

def verificar_login(nome, senha):
    with open(arquivo_dados, "r") as f:
        dados = json.load(f)
    return nome in dados and dados[nome]["senha"] == senha
      
      #Caça niquel
from random import randint

def caca_niquel():
  print("Bem-vindo ao jogo de caça de niquel!")
  numeros = [randint(1,8), randint(1,8), randint(1,8)]
  print("Números gerados:", numeros)
  if numeros[0] == numeros[1] == numeros[2]:
    print("Você encontrou o niquel!")
    return True
  else:
    print("Você não encontrou o niquel.")
    return False

