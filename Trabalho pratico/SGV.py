# Para criar um sistema de gerenciamento de dados para a empresa, vou desenvolver um sistema que atenda às especificações fornecidas. O sistema será chamado de "Gerenciador de Usuários e Produtos" (GUP).
# Estrutura de Dados para Usuários
#Para organizar as informações de usuários, vou utilizar um dicionário Python com chaves para os campos de usuário e valores para os dados correspondentes. O dicionário será armazenado em um arquivo CSV para facilitar a leitura e escrita de dados.

import csv

class Usuario:
    def __init__(self, nome, email, senha, nivel):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.nivel = nivel

class GerenciadorDeUsuarios:
    def __init__(self):
        self.usuarios = {}

    def carregar_usuarios(self, arquivo):
        with open(arquivo, 'r') as file:
            reader = csv.reader(file)
            for linha in reader:
                usuario = Usuario(linha[0], linha[1], linha[2], linha[3])
                self.usuarios[usuario.nome] = usuario

    def criar_usuario(self, nome, email, senha, nivel):
        usuario = Usuario(nome, email, senha, nivel)
        self.usuarios[usuario.nome] = usuario

    def ler_usuario(self, nome):
        return self.usuarios.get(nome)

    def atualizar_usuario(self, nome, email=None, senha=None, nivel=None):
        usuario = self.usuarios.get(nome)
        if usuario:
            if email:
                usuario.email = email
            if senha:
                usuario.senha = senha
            if nivel:
                usuario.nivel = nivel

    def deletar_usuario(self, nome):
        if nome in self.usuarios:
            del self.usuarios[nome]

# Estrutura de Dados para Produtos e Serviços
# Para armazenar os registros de produtos e serviços, vou utilizar uma lista de dicionários.
# Cada dicionário representará um registro de produto ou serviço com campos como nome, código, preço e quantidade.

class Produto:
    def __init__(self, nome, codigo, preco, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade

class GerenciadorDeProdutos:
    def __init__(self):
        self.produtos = []

    def carregar_produtos(self, arquivo):
        with open(arquivo, 'r') as file:
            for linha in file:
                dados = linha.strip().split(',')
                produto = Produto(dados[0], dados[1], float(dados[2]), int(dados[3]))
                self.produtos.append(produto)

    def criar_produto(self, nome, codigo, preco, quantidade):
        produto = Produto(nome, codigo, preco, quantidade)
        self.produtos.append(produto)

    def ler_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def atualizar_produto(self, codigo, nome=None, preco=None, quantidade=None):
        produto = self.ler_produto(codigo)
        if produto:
            if nome:
                produto.nome = nome
            if preco:
                produto.preco = preco
            if quantidade:
                produto.quantidade = quantidade

    def deletar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.remove(produto)
                return
# CRUD de Usuários e Produtos, Agora que temos as estruturas de dados, podemos implementar as funcionalidades CRUD para usuários e produtos.
# Create, Criar Usuário   

gerenciador_usuarios = GerenciadorDeUsuarios()
gerenciador_usuarios.criar_usuario('João', 'joao@example.com', '123456', 'gerente')

#Criar Produto
gerenciador_produtos = GerenciadorDeProdutos()
gerenciador_produtos.criar_produto('Lápis', 'LP01', 1.50, 100)

# Read
# Ler Usuário
usuario = gerenciador_usuarios.ler_usuario('João')
print(usuario.nome, usuario.email, usuario.senha, usuario.nivel)

#Ler Produto
produto = gerenciador_produtos.ler_produto('LP01')
print(produto.nome, produto.codigo, produto.preco, produto.quantidade)

#Update
#Atualizar Usuário
gerenciador_usuarios.atualizar_usuario('João', email='joao@outlook.com')

#Atualizar Produto
gerenciador_produtos.atualizar_produto('LP01', preco=1.75)

# Delete
# Deletar Usuário
gerenciador_usuarios.deletar_usuario('João')

#Deletar Produto
gerenciador_produtos.deletar_produto('LP01')

# Buscar Registro Específico
# Buscar Usuário
usuario = gerenciador_usuarios.ler_usuario('João')

# Buscar Produto
produto = gerenciador_produtos.ler_produto('LP01')

#Imprimir Registros Ordenados
#Imprimir Usuários
for usuario in sorted(gerenciador_usuarios.usuarios.values(), key=lambda x: x.nome):
    print(usuario.nome, usuario.email, usuario.senha, usuario.nivel)

#Imprimir Produtos
for produto in sorted(gerenciador_produtos.produtos, key=lambda x: x.nome):
    print(produto.nome, produto.codigo, produto.preco, produto.quantidade)

#Imprimir Registros Ordenados por Preço
#Imprimir Produtos por Preço
for produto in sorted(gerenciador_produtos.produtos, key=lambda x: x.preco):
    print(produto.nome, produto.codigo, produto.preco, produto.quantidade)

#Gerenciamento de Arquivos
#Carregar Usuários
gerenciador_usuarios.carregar_usuarios('usuarios.csv')

#Funções
#Função para Criar Usuário

def criar_usuario(nome, email, senha, nivel):
    usuario = Usuario(nome, email, senha, nivel)
    gerenciador_usuarios.usuarios[usuario.nome] = usuario

#Função para Criar Produto

def criar_produto(nome, codigo, preco, quantidade):
    produto = Produto(nome, codigo, preco, quantidade)
    gerenciador_produtos.produtos.append(produto)

#Estruturas Condicionais e Repetição
#Estrutura Condicional para Verificar Nível de Permissão

if usuario.nivel == 'gerente':
    print('Você é um gerente')
else:
    print('Você não é um gerente')

#Estrutura de Repetição para Listar Usuários

for usuario in gerenciador_usuarios.usuarios.values():
    print(usuario.nome, usuario.email, usuario.senha, usuario.nivel)

#Strings
#Manipulação de Strings para Criar Nome de Arquivo

nome_arquivo = f'usuarios_{data_atual}.csv'

#Gerência de Arquivos
#Gerenciamento de Arquivos para Carregar e Salvar Dados

gerenciador_usuarios.carregar_usuarios('usuarios.csv')
gerenciador_produtos.carregar_produtos('produtos.csv')

#Tuplas e Conjuntos
#Tupla para Armazenar Dados de Usuário

usuario = (nome, email, senha, nivel)

#Conjunto para Armazenar Dados de Produtos

produtos = {nome: produto for produto in gerenciador_produtos.produtos}

#Dicionários
#Dicionário para Armazenar Dados de Usuário

usuario = {'nome': nome, 'email': email, 'senha': senha, 'nivel': nivel}

#Dicionário para Armazenar Dados de Produto

produto = {'nome': nome, 'codigo': codigo, 'preco': preco, 'quantidade': quantidade}

#Funções
#Função para Criar Usuário

def criar_usuario(nome, email, senha, nivel):
    usuario = Usuario(nome, email, senha, nivel)
    gerenciador_usuarios.usuarios[usuario.nome] = usuario

#Função para Criar Produto

def criar_produto(nome, codigo, preco, quantidade):
    produto = Produto(nome, codigo, preco, quantidade)
    gerenciador_produtos.produtos.append(produto)

#Estruturas de Dados
#Lista para Armazenar Dados de Usuários

gerenciador_usuarios.usuarios = []

#Lista para Armazenar Dados de Produtos

gerenciador_produtos.produtos = []

#Gerência de Arquivos
#Gerenciamento de Arquivos para Carregar e Salvar Dados

gerenciador_usuarios.carregar_usuarios('usuarios.csv')
gerenciador_produtos.carregar_produtos('produtos.csv')

#Funções
#Função para Criar Usuário

def criar_usuario(nome, email, senha, nivel):
    usuario = Usuario(nome, email, senha, nivel)
    gerenciador_usuarios.usuarios[usuario.nome] = usuario

#Função para Criar Produto

def criar_produto(nome, codigo, preco, quantidade):
    produto = Produto(nome, codigo, preco, quantidade)
    gerenciador_produtos.produtos.append(produto)

#Estruturas Condicionais e Repetição
#Estrutura Condicional para Verificar Nível de Permissão

if usuario.nivel == 'gerente':
    print('Você é um gerente')
else:
    print('Você não é um gerente')

#Estrutura de Repetição para Listar Usuários

for usuario in gerenciador_usuarios.usuarios.values():
    print(usuario.nome, usuario.email, usuario.senha, usuario.nivel)

#Strings
#Manipulação de Strings para Criar Nome de Arquivo

nome_arquivo = f'usuarios_{data_atual}.csv'

#Gerência de Arquivos
#Gerenciamento de Arquivos para Carregar e Salvar Dados

gerenciador_usuarios.carregar_usuarios('usuarios.csv')
gerenciador_produtos.carregar_produtos('produtos.csv')

#Tuplas e Conjuntos
#Tupla para Armazenar Dados de Usuário

usuario = (nome, email, senha, nivel)

#Conjunto para Armazenar Dados de Produtos

produtos = {nome: produto for produto in gerenciador_produtos.produtos}

#Dicionários
#Dicionário para Armazenar Dados de Usuário

usuario = {'nome': nome, 'email': email, 'senha': senha, 'nivel': nivel}

#Dicionário para Armazenar Dados de Produto

produto = {'nome': nome, 'codigo': codigo, 'preco': preco, 'quantidade': quantidade}

#Funções
#Função para Criar Usuário

def criar_usuario(nome, email, senha, nivel):
    usuario = Usuario(nome, email, senha, nivel)
    gerenciador_usuarios.usuarios[usuario.nome] = usuario

#Função para Criar Produto

def criar_produto(nome, codigo, preco, quantidade):
    produto = Produto(nome, codigo, preco, quantidade)
    gerenciador_produtos.produtos.append(produto)

#Estruturas de Dados
#Lista para Armazenar Dados de Usuários

gerenciador_usuarios.usuarios = []

#Lista para Armazenar Dados de Produtos

gerenciador_produtos.produtos = []

#Gerência de Arquivos
#Gerenciamento de Arquivos para Carregar e Salvar Dados

gerenciador_usuarios.carregar_usuarios('usuarios.csv')
gerenciador_produtos.carregar_produtos('produtos.csv')

#Funções
#Função para Criar Usuário

def criar_usuario(nome, email, senha, nivel):
    usuario = Usuario(nome, email, senha, nivel)
    gerenciador_usuarios.usuarios[usuario.nome] = usuario

#Função para Criar Produto

def criar_produto(nome, codigo, preco, quantidade):
    produto = Produto(nome, codigo, preco, quantidade)
    gerenciador_produtos.produtos.append(produto)

#Estruturas Condicionais e Repetição
#Estrutura Condicional para Verificar Nível de Permissão

if usuario.nivel == 'gerente':
    print('Você é um gerente')
else:
    print('Você não é um gerente')

#Estrutura de Repetição para Listar Usuários

for usuario in gerenciador_usuarios.usuarios.values():
    print(usuario.nome, usuario.email, usuario.senha, usuario.nivel)

#Strings
#Manipulação de Strings para Criar Nome de Arquivo

nome_arquivo = f'usuarios_{data_atual}.csv'

#Gerência de Arquivos
#Gerenciamento de Arquivos para Carregar e Salvar Dados

gerenciador_usuarios.carregar_usuarios('usuarios.csv')
gerenciador_produtos.carregar_produtos('produtos.csv')

#Tuplas e Conjuntos
#Tupla para Armazenar Dados de Usuário

usuario = (nome, email, senha, nivel)

#Conjunto para Armazenar Dados de Produtos

produtos = {nome: produto for produto in gerenciador_produtos.produtos}

#Dicionários
#Dicionário para Armazenar Dados de Usuário

usuario = {'nome': nome, 'email': email, 'senha': senha, 'nivel': nivel}

#Dicionário para Armazenar Dados de Produto

produto = {'nome': nome, 'codigo': codigo, 'preco': preco, 'quantidade': quantidade}

#Funções
#Função para Criar Usuário

def criar_usuario(nome, email, senha, nivel):
    usuario = Usuario(nome, email, senha, nivel)
    gerenciador_usuarios.usuarios[usuario.nome] = usuario

#Função para Criar Produto

def criar_produto(nome, codigo, preco, quantidade):
    produto = Produto(nome, codigo, preco, quantidade)
    gerenciador_produtos.produtos.append(produto)

#Estruturas de Dados
#Lista para Armazenar Dados de Usuários

gerenciador_usuarios.usuarios = []

#Lista para Armazenar Dados de Produtos

gerenciador_produtos.produtos = []

#Gerência de Arquivos
#Gerenciamento de Arquivos para Carregar e Salvar Dados

gerenciador_usuarios.carregar_usuarios('usuarios.csv')
gerenciador_produtos.carregar_produtos('produtos.csv')

#Funções
#Função para Criar Usuário

def criar_usuario(nome, email, senha, nivel):
    usuario = Usuario(nome, email, senha, nivel)
    gerenciador_usuarios.usuarios[usuario.nome] = usuario

#Função para Criar Produto

def criar_produto(nome, codigo, preco, quantidade):
    produto = Produto(nome, codigo, preco, quantidade)
    gerenciador_produtos.produtos.append(produto)

#Estruturas Condicionais e Repetição
#Estrutura Condicional para Verificar Nível de Permissão

if usuario.nivel == 'gerente':
    print('Você é um gerente')
else:
    print('Você não é um gerente')

#Estrutura de Repetição para Listar Usuários

for usuario in gerenciador_usuarios.usuarios.values():
    print(usuario.nome, usuario.email, usuario.senha, usuario.nivel)

#Strings
#Manipulação de Strings para Criar Nome de Arquivo

nome_arquivo = f'usuarios_{data_atual}.csv'

#Gerência de Arquivos
#Gerenciamento de Arquivos para Carregar e Salvar Dados

gerenciador_usuarios.carregar_usuarios('usuarios.csv')
gerenciador_produtos.carregar_produtos('produtos.csv')

#Tuplas e Conjuntos
#Tupla para Armazenar Dados de Usuário

usuario = (nome, email, senha, nivel)

#Conjunto para Armazenar Dados de Produtos

produtos = {nome: produto for produto in gerenciador_produtos.produtos}

#Dicionários
#Dicionário para Armazenar Dados de Usuário

usuario = {'nome': nome, 'email': email, 'senha': senha, 'nivel': nivel}

#Dicionário para Armazenar Dados de Produto

produto = {'nome': nome, 'codigo': codigo,}

