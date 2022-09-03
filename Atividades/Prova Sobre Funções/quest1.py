# Questão 1. Construa um script em Python que recebe valores inteiros do usuário e 
# armazena em uma matriz de tamanho 3x3.
# 
# Feito isto, utilize uma estrutura de repetição para percorrer a matriz e encontrar o 
# maior e o menor valor da matriz.

# Verifique se os valores encontrados (maior e menor) são pares ou ímpares! Se for par, 
# o valor deve ser dobrado, caso contrário, deve ser subtraído por 1.
# No final, a sua solução deve exibir o valor processado. [30]
# Para isto, crie uma três funções específicas:
# Função "ler_valores": responsável por fazer a leitura dos dados na matriz
# Função "verifica_maior": responsável por encontrar o maior valor da matriz
# Função "verifica_menor": responsável por encontrar o menor valor da matriz
# Função "parEimpar": responsável por fazer as operações para o valor par e ímpar 
# (se for par, o valor deve ser dobrado, se for ímpar, subtraído por 1)
# Função "principal": responsável por chamar todas as funções e imprimir os valores 
# com as respectivas operações realizadas na etapa anterior.
# 

m = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("Digite um valor: ")))

    m.append(linha)
def ler_valores():
    return m

def verifica_maior():    
    maior = m[0][0]
    for l in range(3):
        for c in range(3):
            if maior < m[l][c]:
                maior = m[l][c]

    
    return maior


def verifica_menor():    
    menor = m[0][0]
    for l in range(3):
        for c in range(3):
            if menor > m[l][c]:
                menor = m[l][c]
                

    return menor


def parEimpar():
    if verifica_maior() % 2 == 0:
        print(verifica_maior() *2)
    else:
        print(verifica_maior()-1)
    if verifica_menor() % 2 ==0:
        print(verifica_menor() * 2)
    else:
        print(verifica_menor()-1)

def principal():
    print(f"O maior valor foi: {verifica_maior()}")
    print(f"O menor valor foi: {verifica_menor()}")
    print(parEimpar())
principal()




     