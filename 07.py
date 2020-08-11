#Faça um Programa que leia um vetor de 5 números inteiros,
# mostre a soma, a multiplicação e os números.
lista_numeros = [4,5,4,6,3]

def soma_lista (lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

def mult_list (lista):
    mult = 1
    for item in lista:
        mult = mult * item
    return mult

print(soma_lista(lista_numeros))
print(mult_list(lista_numeros))
print(lista_numeros)