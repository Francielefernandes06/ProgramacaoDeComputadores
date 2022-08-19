# Utilizando funções, crie a função de nome leitura que será
# responsável por receber do usuário um valor do tipo inteiro
# • Após a leitura, crie uma segunda função de nome palindromo
# que verificará e informará se o número informado pelo usuário
# é um palíndromo:
# – ex.: “x é um palíndromo” || “x não é um palíndromo”
# • A função leitura e palíndromo deve ser executada na função
# de nome principal
# – Palíndromo é uma palavra, frase ou número que permanece igual
# quando lida de trás para diante

valor = int(input("Digite um valor: "))
value = str(valor)

def leitura():
    print(valor)

def palindromo():
    if value == value[::-1]:
        print(f"{valor} é palindromo")
    else:
        print(f" {valor} não é palindromo")
        
def principal():
    leitura()
    palindromo()
principal()



        








