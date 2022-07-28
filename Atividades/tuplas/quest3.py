# Questão 3: Dada a seguinte tupla: (32, [5, 69, 4], 3, 12, 0), use a indexação para localizar o item de valor 5 e modificá-lo para 543, usando o operador de atribuição.

tupla = (32, [5, 69, 4], 3, 12, 0)
print(tupla[1][0])
tupla[1][0] = 543
print(tupla)