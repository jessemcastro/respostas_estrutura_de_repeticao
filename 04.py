#Faça um Programa que leia um vetor de 10 caracteres,
# e diga quantas consoantes foram lidas.
# Imprima as consoantes.

lista_letras = []
cont = 0
while cont < 10:
    atual = str(input("Digite uma letra"))
    lista_letras.append(atual)
    cont = cont + 1
print("Lista inicial: ",lista_letras)

def remove_vogal (lista):
    if 'a' in lista:
        lista.remove('a')
    if 'e' in lista_letras:
        lista.remove('e')
    if 'i' in lista_letras:
        lista.remove('i')
    if 'o' in lista_letras:
        lista.remove('o')
    if 'u' in lista_letras:
        lista.remove('u')
    return(lista)

print(remove_vogal(lista_letras))

tamanho_da_lista = len(lista_letras)
print("A nova lista possui:", tamanho_da_lista, "consoantes")