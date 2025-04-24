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
        "email": email,
        "saldo": 100
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

def adicionar_dinheiro(nome, valor):
    with open('dados.json', "r") as f:
        dados = json.load(f)

    if nome in dados:
        dados[nome]['saldo'] += valor
        with open('dados.json', "w") as f:
            json.dump(dados, f, indent=4)
        return True
    return False

def apostar(nome, valor_aposta):
    with open('dados.json', "r") as f:
        dados = json.load(f)

    if nome in dados:
        saldo = dados[nome]['saldo']
        if saldo >= valor_aposta:
            # Subtrai a aposta
            dados[nome]['saldo'] -= valor_aposta

            # Gera o resultado do jogo
            resultado = [randint(1, 8), randint(1, 8), randint(1, 8)]
            if resultado[0] == resultado[1] == resultado[2]:  # Vitória
                # Dobra o valor apostado
                dados[nome]['saldo'] += valor_aposta * 2
                resultado_texto = f"Você ganhou! Números: {resultado}, seu saldo é {dados[nome]['saldo']}."
            else:  # Perda
                resultado_texto = f"Você perdeu. Números: {resultado}, seu saldo é {dados[nome]['saldo']}."

            # Salva as alterações no arquivo
            with open('dados.json', "w") as f:
                json.dump(dados, f, indent=4)

            return resultado_texto
        else:
            return "Saldo insuficiente para apostar."
    return "Usuário não encontrado."

