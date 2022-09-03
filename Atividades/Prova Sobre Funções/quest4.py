valor =float(input("Digite o valor do seu salário: "))
reaj= valor
def salario():
    return valor

def reajuste():
    if valor > 1250.00:
        valor1= valor * 0.1
        return valor1
    else:
        valor2 = valor * 0.15
        return valor2

def principal():
    valor_total = salario() + reajuste()
    print(f"Seu salário foi: {salario()}R$")
    print(f"Você recebeu um reajuste de: {reajuste()}R$")
    print(f"Então seu salario agora é: {valor_total}R$")
principal()



