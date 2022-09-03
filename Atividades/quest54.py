def lerNumero():
    num = int(input("Digite um número: "))
    numer = str(num)
    return numer



def palindromo (num):
    if num == num[::-1]:
        print("É um palindromo!")

    else:
        print("Não é um palindromo!")

def principal(num):
    return num
principal (palindromo (lerNumero()))

