# 1) Grande parte das soluções web precisam de um sistema de autenticação de clientes e uma das metodologias mais tradicionais de segurança é manter o controle de usuários através de login e senha. Porém, há regras de segurança que devem ser mantidas:
# O login deve ser um identificador único; ou seja, nenhum outro usuário deve ter o mesmo login
# A senha deve conter pelo menos 6 caracteres
# Com base nos conhecimentos acima, construa um dicionário que recebe do usuário o login e senha de 10 pessoas (leve em consideração as regras de segurança)

contador= 0
dicionario = {}


while contador < 3:
    login = input("Digite o login: ")
    senha = int(input("Digite a senha: "))
    if login in dicionario:
        print("Login já existe")
    elif len(senha) < 6:
        print("Senha muito curta")
    else:
        dicionario[login] = senha
        contador += 1
        print("Login cadastrado com sucesso")
print(dicionario)








    

