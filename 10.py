#Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão
# ser compostos pelos elementos intercalados dos dois outros vetores.

lista_numeros_1=[1,1,1,1,1,1,1,1,1,1]
lista_numeros_2 = [2,2,2,2,2,2,2,2,2,2,2]
lista_nova = []

for n in lista_numeros_1:
    lista_nova.append(n)
    for n in lista_numeros_2:
        lista_nova.append(n)
        break



print(lista_nova)