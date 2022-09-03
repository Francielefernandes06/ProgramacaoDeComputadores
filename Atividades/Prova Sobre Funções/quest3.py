# Crie um programa que pergunte a velocidade do carro de um usuário e diga se este foi ou 
# não multado. [10]
# Construa um programa que pergunta a velocidade do carro de um usuário. Após a leitura da 
# velocidade, construa uma função chamada "multa" que verifica se o carro ultrapassou o limite
#  de velocidade da via de 60 km/h. Se a velocidade for superior a 60, exiba uma mensagem dizendo 
# que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 
# 60 km/h.

# O cálculo da multa é dado através de:
# multa = (velocidade - 60) * 5

# 
velocidade = float(input("Digite a velocidade do carro: "))
multa1 = (velocidade - 60) * 5
def multa():
    if velocidade > 60:
        print("Você ultrapassou o limite")
        return multa1
    else:
        print("Você não foi multado")

print(f"o valor da multa é: {multa()} R$")


