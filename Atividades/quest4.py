num= int(input('Digite um número inteiro: '))
soma= 0
for i in range(1, num, +1):
    if num % i==0:
        soma= soma + i
print(soma)

if soma == num:
    print('É um número perfeito')
else:
    print('Não é um número perfeito')

# Número perfeito

# Na matemática, um número perfeito é um número inteiro cuja soma de todos os seus divisores positivos próprios (excluindo ele mesmo) é igual ao próprio número. Por exemplo: o número 6 é perfeito, pois 1+2+3 é igual a 6.

# Construa um programa que recebe um número inteiro e que verifique se ele é um número perfeito. Caso o número seja perfeito, o programa deve imprimir "X é um número perfeito", onde X é o valor lido. Caso contrário, a mensagem " X não é um número perfeito" deve ser impresso.    

