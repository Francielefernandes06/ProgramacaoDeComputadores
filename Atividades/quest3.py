# Soma de X até Y de ordem decrescente 
# Utilizando o comando for, construa um algoritmo que recebe dois números inteiros decrescentes X e Ye que imprima a soma de todos os números de X até Y. Se for recebido como entrada números crescentes, deverá ser exibido para o usuário a frase "Insira uma dupla de ordem decrescente".
# Exemplo 1: se os números informados foram 5 e 3, o programa deve somar 5+4+3 e exibir o resultado 12. Exemplo 2: se os números informados foram 6 e 9, o seu programa deve exibir a frase "Insira uma dupla de ordem decrescente".

v1= int(input('Digite um o primeiro número: '))
v2= int(input('Digite um o segundo número: '))

if v1 > v2:
    value= sum (range(v1, v2-1 , -1))
    print(value)
else:
    print('Insira uma dupla de ordem decrescente')
   