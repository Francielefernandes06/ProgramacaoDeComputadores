# Questão 2: Crie uma tupla que recebe 6 valores do tipo inteiro do usuário. Agora solicite do usuário um segundo número inteiro. Copie os elementos a partir do segundo valor que o usuário digitou para uma nova tupla.


contador=0
tupla=()
while contador != 6:
    n=int(input("Digite um número: "))
    contador+=1
    tupla=tupla + tuple([n])
print(tupla)
n1 = int(input('Digite o segundo número: '))
if n1 > 6:
    print('Número inválido')
else:
    nova_tupla = tuple(tupla[n1:])
print(nova_tupla)