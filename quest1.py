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


        
   