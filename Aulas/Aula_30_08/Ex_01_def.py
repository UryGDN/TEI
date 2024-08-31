import os

def limpar_tela():
    os.system('cls')

def ler_numero():
    while True:
        try:
            return int(input("Informe um valor: "))
        except ValueError:
            print("O cabeça de pica isso é um número pra vc?")

def soma(n1, n2):
    return n1+n2

def main():
    limpar_tela()
    n1 = ler_numero()
    n2 = ler_numero()
    print(soma(n1,n2))

main()