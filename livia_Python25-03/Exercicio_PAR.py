import time
def verificar_par(numero):
    if numero > 0:
        if numero % 2 == 0:
            print('"P-A-R"')
        else:
            print("tente outra vez!")
    else:
         print("O número não é inteiro positivo")

numero = int(input("Digite um número inteiro positivo: "))
verificar_par(numero)