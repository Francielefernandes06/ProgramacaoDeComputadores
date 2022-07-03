v1 = int(input('Digite um o primeiro número: '))
v2 = int(input('Digite um o segundo número: '))

if v1 > v2:
    for cont in range(v1, v2-1 , -1):
        print(cont)
        for cont2 in range(0, 10+1, 1):
            print(f'{cont} x {cont2} = {cont*cont2}')
elif v1< v2:
    for cont in range(v1, v2+1 , 1):
        print(cont)
        for cont2 in range(0, 10+1, 1):
            print(f'{cont} x {cont2} = {cont*cont2}')
else:
    print('Não é possível calcular')
            


# Utilizando estruturas de repetição, construa um programa que recebe uma quantidade Indeterminada de duplas de valores inteiros X e Y. Para cada par de valores X e Y, o programa deve verificar se esses valores foram digitados de ordem crescente ou decrescente. Se o par de números informados forem crescente, o seu programa deve exibir a tabela com a multiplicação de ordem crescente de X à Y Se o par de números informados forem decrescentes, o seu programa deve exibir a tabela com à a multiplicação de ordem decrescente de X à Y Se os pares digitados forem iguals, o seu programa deve encerrar a leitura de valores indeterminadas e parar.