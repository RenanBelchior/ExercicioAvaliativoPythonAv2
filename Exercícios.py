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
        
--------------------------------------------------------------------------------
#2. (Dados Aglomerados) Considere um sistema Python onde os dados são armazenados em
#dicionários. Nesse sistema existe um dicionario principal e o dicionário de backup. Cada vez
#que o dicionário principal atinge tamanho 5, ele imprime os dados na tela e apaga o seu conteúdo.
#Crie um programa que insira dados em um dicionário, realizando o backup a cada dado e
#excluindo os dados do dicionário principal quando ele atingir tamanho 5.

dicionarioPrincipal = {}
dicionarioBackup = {}

while True:
    print("Digite nome ou 'sair'")
    nome = input("Digite um nome: ")
    dados = int(input("Digite o ID para o nome: "))
    
    if(nome.lower()) == "sair":
        break

    dicionarioPrincipal[nome] = dados
    dicionarioBackup[nome] = dados  

    if len(dicionarioPrincipal) == 5:
        print("Dicionário principal chegou ao limite!")
        print(dicionarioPrincipal)
        dicionarioPrincipal = {}  

print("Dicionário de backup: ")
print(dicionarioBackup)

--------------------------------------------------------------------------------
#3. (Prog. Orientado Objetos) Elabore um programa em Python que Crie a classe “Automóvel” e
#derive (Herança) as 4 subclasses abaixo. Seu programa deve ter no mínimo 2 atributos e no
#mínimo 2 métodos (e garantir o Polimorfismo)

class Automovel():
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
class Carro(Automovel):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def rodas(self):
        print("Possui 4 rodas")
    
    def tracao(self):
        print("Tração 4x2 traseiro")


class Caminhao(Automovel):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def rodas(self):
        print("Possui 10 rodas")
    
    def tracao(self):
        print("Tração 10x4 traseiro")


class Caminhonete(Automovel):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def rodas(self):
        print("Possui 6 rodas")
    
    def tracao(self):
        print("Tração 6x4 traseiro")


class Moto(Automovel):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def rodas(self):
        print("Possui 2 rodas")
    
    def tracao(self):
        print("Tração 2x1 traseira")

Automovel = Moto("Harley Davidson", "Low Rider S")
print(Automovel.marca, Automovel.modelo)
Automovel.rodas()
Automovel.tracao()

--------------------------------------------------------------------------------
#4. (Prog. Orientado Objetos) Elabore um programa em Python que Crie a classe “Produto” e derive
#(Herança) as 3 subclasses abaixo. Seu programa deve ter no mínimo 3 atributos e no mínimo 2
#métodos (e garantir o Polimorfismo). O programa deve ter um menu que escolha qual classe o
#usuário quer instanciar

class Produto(object):
    def __init__(self, nome, autor, ano):
        self.nome = nome
        self.autor = autor
        self.ano = ano
    
class Livro(Produto):
    def __init__(self, nome, autor, ano):
        super().__init__(nome, autor, ano)
    
    def Ler(self):
        print("lendo um livro")
    
    def Estado(self):
        print("Na poltrona da sala")


class Cd(Produto):
    def __init__(self, nome, autor, ano):
        super().__init__(nome, autor, ano)
    
    def Ouvir(self):
        print("Ouvindo um CD")
    
    def Estado(self):
        print("Cadeira da varanda")


class DVD(Produto):
    def __init__(self, nome, autor, ano):
        super().__init__(nome, autor, ano)
    
    def Assistir(self):
        print("Vendo um DVD")
    
    def Estado(self):
        print("No sofá da sala")


Produto = DVD("Interestelar", "Hans Zimmer", 2015)
print(Produto.nome, Produto.autor, Produto.ano)
Produto.Assistir()
Produto.Estado()
