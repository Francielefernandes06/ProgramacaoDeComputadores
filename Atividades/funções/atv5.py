# Escreva um programa que pergunte a quantidade de km
# percorridos por um carro alugado pelo usuário, assim como a
# quantidade de dias pelos quais o carro foi alugado
# • Calcule o preço a pagar, sabendo que o carro custa R$ 60,00
# por dia e R$ 0,15 por km rodado
# – Para isto crie uma função que será responsável calcular e retornar o
# valor a ser pago diante o consumo
# – Utilize a fórmula:
# • quilômetros * 0.15 + dias * 60

km = int(input("Digite a quntidade de km rodados: "))
dias = int(input("Quantos dias você alugou o carro: "))

def calc():
    return((km * 0.15 ) + (dias * 60))        

print(f"O total a pagar é de R${calc()}")
