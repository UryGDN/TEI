import os

sum = 0
resposta = 1
n_ma = 0
n_me = 100000


def limpar_tela():
    os.system('cls')

def inserir_numero():
    while True:
        try:
            return int(input("Insira um numero: "))
        except ValueError:
            print("Isso não é um número tente novamente")


def num_media(*valor):
    for n in valor[]:
        sum = sum + valor[n]

def num_pares(*valor):

def num_impares(*valor):

def num_maior(*valor):

def num_maior(*valor):


limpar_tela()
while True:
    inserir_numero()
    try:
        resposta = int(input("Deseja Continuar? (S = 1 N = 0) "))
    except ValueError:
        print("Tente novamente")
    if resposta == 1:
        continue
    elif resposta == 0:
        break

