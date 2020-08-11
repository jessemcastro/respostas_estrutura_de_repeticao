#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

listanumeros = []
cont = 1

while cont<=10:
    atual = input("Digite um numero")
    listanumeros.append(atual)
    cont = cont + 1

listanumeros.reverse()
print(listanumeros)