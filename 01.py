#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
listanumeros = []
cont = 1

while cont<=5:
    atual = input("Digite um numero")
    listanumeros.append(atual)
    cont = cont + 1

print(listanumeros)