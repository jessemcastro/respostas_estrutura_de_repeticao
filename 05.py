#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.


lista_numeros = []
lista_numeros_pares = []
lista_numeros_impares = []

cont = 0
while cont < 10:
    atual = int(input("Digite algum numero inteiro"))
    lista_numeros.append(atual)
    if atual % 2 ==0:
        lista_numeros_pares.append(atual)
    else:
        lista_numeros_impares.append(atual)
    cont = cont + 1

print(lista_numeros)
print(lista_numeros_pares)
print(lista_numeros_impares)