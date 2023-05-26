#1- (Dados Aglomerados) Desenvolva um programa em Python que cadastre informações de várias
#pessoas (nome, idade e CPF) e depois coloque em um dicionário. Depois remova todas as
#pessoas menores de 18 anos do dicionário e coloque em outro dicionário

registroCadastros = {}               
registroCadastrosMaior18 = {}
registroCadastrosMenor18 = {}

while True:
    print(".:: Menu Cadastro ::.")
    print("1 - Cadastrar Usuário(a)")
    print("2 - Listar Cadastrados(as) Maiores de 18 anos")
    print("3 - Listar Cadastrados(as) Menores de 18 anos")
    print("0 - Sair")
    
    menu = input("Digite a opção desejada: ")
    if (menu == "1"):
        nome = str(input("Digite o nome do usuário(a)....: "))
        idade = int(input("Digite a idade da pessoa..: "))
        cpf = int(input("Digite o CPF do usuário(a)......: "))

        usuario = {"nome": nome, "idade": idade, "cpf": cpf}
        registroCadastros[cpf] = usuario
        
        if(idade < 18):
            registroCadastrosMenor18[cpf] = usuario
        else:
            registroCadastrosMaior18[cpf] = usuario
            
        print("Usuário(a) cadastrado(a) com sucesso!")
        

    elif (menu == "2"):
        print("::.Lista de Cadastrados(as) Maiores de 18 anos.::")
        for cpf, pessoa in registroCadastrosMaior18.items():
            print(f"CPF: {cpf}")
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")
            print("--------------------------")
            

    elif (menu == "3"):
        print("::.Lista de Cadastrados(as) Menores de 18 anos.::")
        for cpf, pessoa in registroCadastrosMenor18.items():
            print(f"CPF: {cpf}")
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")
            print("--------------------------")
            
    
    elif (menu == "0"):
        print("Menu Finalizado!")
        break
    
    else:
        print("Opção inválida!")
