#Aqui funções Model de Cadastro (Categoria e Produtos)

import sqlite3

#Cria o Banco de Dados de Cadastro de Produtos
def BD_cad_produtos():
    conn = sqlite3.connect("../banco.db")
    cursor = conn.cursor()
    print("Banco conectado!")

    #cursor.execute("INSERT INTO categorias VALUES (?, ?, ?)", (codigo, descricao))
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cad_produtos(
            codigo_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            codigobarras INT(30),
            descricao_produto VARCHAR(50) NOT NULL,
            marca VARCHAR(20) NOT NULL,
            categoria VARCHAR(40) NOT NULL,
            custo DECIMAL(8,2) NOT NULL,
            venda DECIMAL(8,2) NOT NULL
        )
    ''')
    print("Tabela cad_produtos já existe ou foi criada!\n")
    
#Cria o Banco de Dados de Cadastro de Categorias
def BD_cad_categorias():
    conn = sqlite3.connect("../banco.db")
    cursor = conn.cursor()
    print("Banco conectado!")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cad_categorias(
            codigo_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao_produto VARCHAR(50) NOT NULL
        )          
    ''')
    print("Tabela cad_categorias já existe ou foi criada!\n")

    conn.commit() #Confirma as alterações
    conn.close() #Encerra o BD

#Chamada de Criação do Banco de Cadastro
chamadaBD = BD_cad_categorias(), BD_cad_produtos()