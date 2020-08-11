#Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

pessoas = 0
lista_idade =[]
lista_altura=[]

for pessoas in range(5):
    idade_atual = float(input("Digite sua idade"))
    lista_idade.append(idade_atual)
    altura_atual = float(input("Digite sua altura"))
    lista_altura.append(altura_atual)

lista_altura.reverse()
lista_idade.reverse()

print(lista_altura)
print(lista_idade)

