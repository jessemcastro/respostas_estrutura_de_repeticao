#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


lista_notas = []
cont = 0
soma = 0
while cont<4:
    atual = float(input("Digite uma nota"))
    lista_notas.append(atual)
    soma = soma + atual
    cont = cont + 1
media = soma/cont
print ("As notas são: ",lista_notas)
print ("A média é", media)


