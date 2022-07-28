#Questão 4: Crie um programa que deve ler dados indefinidos que serão armazenados em uma tupla.Quando o programa receber 0, a leitura indeterminada deverá ser encerrada. Após o encerramento das leituras indeterminadas, solicite ao usuário um valor do tipo inteiro e exiba a quantidade de ocorrências presentes na tupla referente ao número informado.

tupla = ()
while True:
    n = input('Digite algo: ')
    if n == '0':
        break
    tupla += (n,)   
print(f'A tupla criada foi: {tupla}')
n1 = int(input('Digite um número inteiro: '))
n2 = str(n1)
print(f'O número {n2} aparece {tupla.count(n2)} vezes na tupla.')

