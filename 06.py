#Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

notas = 0
soma = 0
media = 0
alunos = 0
cont= 1
aprovados = 0
lista_medias = []
for alunos in range(2):
    print("Inserindo notas do aluno numero:",cont)
    for notas in range (4):
        atual = float(input("Digite a notas"))
        soma = soma + atual
        print("nota armazenada")

    cont = cont + 1
    media = soma/4
    print("A media desse aluno é: ",media)
    if media>=7 :
        aprovados = aprovados+1
    lista_medias.append(media)
    media = 0
    soma = 0

print("As média lançadas são: ",lista_medias)
print("O numero de alunos com nota maior ou igual a 7 é:",aprovados)
