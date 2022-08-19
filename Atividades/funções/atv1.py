# Faça um programa que solicite ao usuário três números
# diferentes e exiba o dobro do maior número
# • Para fazer isso separe seu código em duas funções
# diferentes:
# – Uma função para retornar o maior dos três números
# – E outra função para dobrar o número

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um segundo número: "))
n3= int(input("Digite um terceiro número: "))

def maiorNumero():
    if (n1>n2>n3):
        print(f"o primeiro número é maior ({n1})")
    elif (n2>n1>n3):
        print(f"o segundo número é maior ({n2})")
    else:
        print(f"o terceiro número é maior ({n3})")
maiorNumero()

def dobrarNum():
    if (n1>n2>n3):
        print(f"o dobro de {n1} é {var1}")
    elif (n2>n1>n3):
        print(f"o dobro de {n2} é {var2}")
    else:
        print(f"o dobro de {n3} é {var3}")

var1= n1 * 2
var2= n2 * 2
var3= n3 * 2

dobrarNum()