# As páginas web costumam trabalhar com formulários para cadastro de usuários. Utilizando dicionários para receber dados do usuário, informe os valores conforme a imagem "Formulário.jpg" (em anexo). No final, você deverá exibir os dados informados com a estrutura semelhante ao que é apresentado na imagem em anexo.


matricula = []
nome = []
sexo = []
idade = []
dicionario = {
    'matricula': matricula,
    'nome': nome,
    'sexo': sexo,
    'idade': idade
}

while True:
    matricula.append(int(input("Digite a matricula: ")))
    nome.append(input("Digite o nome: "))
    sexo.append(input("Digite o sexo: "))
    idade.append(int(input("Digite a idade: ")))
    sair= input("Digite 2 para sair ou 1 para continuar: ")
    if sair == '2':
        print ("{:<10} {:<10} {:<10} {:<10}".format('MATRICULA', 'NOME', 'SEXO' , 'IDADE'))
        for i in range(len(matricula)):
            print("{:<10} {:<10} {:<10} {:<10}".format(matricula[i], nome[i], sexo[i], idade[i]))
        break
    else:
        continue
print(dicionario)



    




