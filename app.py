#Gerador de dados aleatorios

import random

#função para gerar nomes aleatorios
def gerar_nome():
    nomes = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    return random.choice(nomes)

#função para gerar telefones aleatorios
def gerar_telefones():
    telefones = ['55219854', '552154485', '55421156', '5521556', '55212525']
    return random.choice(telefones)

#função pra gerar cidades aleatorias
def gerar_cidades():
    cidades = ['rio de janeiro', 'olinda', 'varginha', 'bh', 'bs']
    return random.choice(cidades)

#funçaõ para gerar estados aleatorios
def gerar_estados():
    estados = ['RJ', 'PE', 'CE', 'BA', 'MG']
    return random.choice(estados)

#função para gerar emails aleatorios
def gerar_email():
    emails = ['caiovicenterj@gmail.com', 'oiasdoias@gmail.com', '22222222222@gmail.com', '3333333333333@gmail.com', '44444444444444@gmail.com']
    return random.choice(emails)

#dicionario para salvar as opçoes correspondestes
opcoes = {
    '1': gerar_nome,
    '2': gerar_telefones,
    '3': gerar_cidades,
    '4': gerar_estados,
    '5': gerar_email
}

#Váriavel para controlar se os dados devem ser salvos ou nao
salvar_arquivo = False

while True:
    print("Escolha uma opção:")
    print("1. Gerar nome")
    print("2. Gerar e-mail")
    print("3. Gerar telefone")
    print("4. Gerar cidade")
    print("5. Gerar estado")
    print("6. Parar")

    opcao_digitadas = input("Digite um numero da opção desejada: ")
    opcao_selecionada = opcao_digitadas.split(',')
    

    if '6' in opcao_selecionada:
        break


    with open('dados.txt', 'a') as arquivo:  # Abre o arquivo uma vez em modo de adição ('a')
        for opcao in opcao_selecionada:
            if opcao in opcoes:
                dado_gerado = opcoes[opcao]()
                print(f"Dado gerado: {dado_gerado}")
                arquivo.write(f"{dado_gerado}\n") 
                
if salvar_arquivo:
    print("Dados salvo em .txt")
