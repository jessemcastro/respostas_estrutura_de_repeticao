#Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

lista_numeros =[]
cont =0
for cont in range(10):
    atual = int(input("Digite um numero"))
    lista_numeros.append(atual)

def soma_quadrado_lista (lista):
    soma = 0
    for item in lista:
        soma = soma + (item*item)
    return soma

print(soma_quadrado_lista(lista_numeros))
