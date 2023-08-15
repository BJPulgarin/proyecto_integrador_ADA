import os
import readchar

numero = 0
os.system('cls' if os.name == 'nt' else 'clear')
print(numero)


def imprimir(n):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(n)


while True:
    k = readchar.readkey()
    if k == "n" or k == "N":
        numero += 1
        imprimir(numero)
        if numero == 50:
            break
    