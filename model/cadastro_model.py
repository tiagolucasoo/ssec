#Aqui funções Model de Cadastro (Categoria e Produtos)

import sqlite3

def cadastro_categoria_M():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categorias VALUES (?, ?, ?)", (codigo, descricao))
    conn.commit()
    conn.close()