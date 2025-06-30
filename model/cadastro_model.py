#Aqui funções Model de Cadastro (Categoria e Produtos)
# Salvar informações - Buscar a lista de categorias
# Calcular o custo de um pedido
# cadastro_model.py

import sqlite3
import os

#Cria o Banco de Dados de Cadastro de Produtos

def rota_banco():
    caminho_banco = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'banco.db'))
    conn = sqlite3.connect(caminho_banco)
    print("Banco conectado!")
    return conn

def BD_cad_produtos():
    conn = rota_banco()
    cursor = conn.cursor()

    #cursor.execute("INSERT INTO categorias VALUES (?, ?, ?)", (codigo, descricao))
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cad_produtos(
            codigo_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            codigobarras INT(30) UNIQUE,
            descricao_produto VARCHAR(50) NOT NULL,
            marca VARCHAR(20) NOT NULL,
            categoria VARCHAR(40) NOT NULL,
            curva INT NOT NULL,
            custo DECIMAL(8,2) NOT NULL,
            venda DECIMAL(8,2) NOT NULL
        )
    ''')
    print("Tabela cad_produtos já existe ou foi criada!\n")
    conn.commit()
    conn.close()

BD_cad_produtos()
#Cria o Banco de Dados de Cadastro de Categorias
def BD_cad_categorias():
    #caminho_banco = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'banco.db'))
    #conn = sqlite3.connect(caminho_banco)
    #cursor = conn.cursor()
    #print("Banco conectado!")

    conn = rota_banco()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cad_categorias (
            codigo_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao_categoria VARCHAR(50) NOT NULL
        )          
    ''')
    print("Tabela cad_categorias já existe ou foi criada!\n")

    conn.commit() #Confirma as alterações
    conn.close() #Encerra o BD

BD_cad_categorias()

def salvarCategorias(descricao_categoria,):
    caminho_banco = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'banco.db'))
    conn = sqlite3.connect(caminho_banco)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO cad_categorias (descricao_categoria) VALUES (?)", (descricao_categoria,))
        conn.commit()
        print(f"Model: Categoria {descricao_categoria} salva no banco")
        return True
    except sqlite3.IntegrityError as e:
        print("Erro de integrridade: ", e)
        return False
    except Exception as e:
        print("Erro geral ao salvar: ", e)
    finally:
        conn.close()

def listarCategoriasModel():
    #caminho_banco = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'banco.db'))
    #conn = sqlite3.connect(caminho_banco)
    #cursor = conn.cursor()
    #print("Banco conectado!")

    conn = rota_banco()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT descricao_categoria FROM cad_categorias")
        categorias = [row[0] for row in cursor.fetchall()]
        return categorias
    finally:
        conn.close()

'''
def listarCodigoCategoriaModel():
    #caminho_banco = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'banco.db'))
    #conn = sqlite3.connect(caminho_banco)
    #cursor = conn.cursor()
    #print("Banco conectado!")

    conn = rota_banco()
    cursor = conn.cursor()

    try:
        cursor.execute(
            SELECT codigo_categoria FROM cad_categorias
            WHERE codigo_categoria = (?) {descricao})
        codigo_cat = cursor.fetchall()
        return codigo_cat
    finally:
        conn.close()
'''

# Aqui Código do salvar produto

def salvarProdutos(codigobarras: int, descricao_produto: str, marca: str, categoria: str, custo: float, venda: float, curva: int):
    conn = rota_banco()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO cad_produtos (codigobarras, descricao_produto, marca, categoria, custo, venda, curva)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (codigobarras, descricao_produto, marca, categoria, custo, venda, curva))
        conn.commit()
        print(f"Model: Produto '{descricao_produto}' salvo no banco.")
        return True
    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade ao salvar produto: {e}")
        return False
    except Exception as e:
        print(f"Erro geral ao salvar produto: {e}")
        return False
    finally:
        conn.close()

def listarProdutosModel():
    conn = rota_banco()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT descricao_produto, codigobarras FROM cad_produtos")
        produtos = cursor.fetchall() 
        return produtos
    finally:
        conn.close()