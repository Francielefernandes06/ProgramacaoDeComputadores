# Faça um programa que inicialize uma lista vazia, depois disso
# solicite 5 nomes diferentes ao usuário (utilize laço de repetição)
# – Cada nome digitado deve ser adicionado à lista e por fim, todos os
# nomes devem ser escritos no console
# – Utilize uma função para solicitar e retornar o nome digitado, uma
# função para adicionar o nome à lista (passando o nome e a lista por
# parâmetro) e outra função para escrever todos os nomes no
# console

lista = []
def solicitarNome():
    nome = input("Digite um nome: ")
    return nome

def adicionarNome(nome, lista):
    lista.append(nome)

def escreverNomes(lista):
    for nome in lista:
        print(nome)

for i in range(5):
    nome = solicitarNome()
    adicionarNome(nome, lista)

escreverNomes(lista)



