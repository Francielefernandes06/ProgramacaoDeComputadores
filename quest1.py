n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
calc1= n1 % 2
calc2 = n2 % 2
soma = (2*n1) + n1
soma2 =n2+n1*2

if n1 < 0 or n2 < 0:
    print('Não é possível calcular, coloque apenas números positivos')

elif calc1 == 0 and calc2 == 0 or calc1 != 0 and calc2 != 0 : 
    value= sum(range(n2, soma2, +2))
    print(value)

elif calc1 != 0 and calc2 == 0:
    value2 = sum (range(n2+1, soma2+1, +2))
    print(value2)

elif calc1 == 0 and calc2 != 0:
    value3= sum (range(n2+1, soma2+1, +2))
    print(value3)

else:
    print('Não sei')

#Descrição da atividade
# Você construirá um programa que receba 2 números inteiros. O número primeiro representará a quantidade de números que serão somados e indicará se os números serão pares ou os ímpares. Já o segundo número, representará o primeiro termo da sequência que será somada. O seu programa deve verificar se o primeiro termo é par ou ímpar para, então, realizar a soma corretamente. Se o primeiro termo for par, o programa soma os números pares; se o primeiro termo for ímpar, a soma será dos números ímpares. Ao final, imprima apenas o resultado da soma.

# Exemplo 1: para
# a entrada 4 e 5, o programa somará 4 termos pares a partir do número 5, portanto, a soma será 6+8+10+12.
# Exemplo 2: para a entrada 5 e 11, o programa somará 5 termos ímpares a partir do número 11, portanto, a soma será 11+13+15+17+19.



        
   