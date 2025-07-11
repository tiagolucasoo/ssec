#Aqui funções Model de Cadastro (Categoria e Produtos)
# Salvar informações - Buscar a lista de categorias
# Calcular o custo de um pedido

import sqlite3
import os

#1) Reaproveitamento da Rota do BD
def rota_banco():
    caminho_banco = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'banco.db'))
    conn = sqlite3.connect(caminho_banco)
    return conn

#2) Criação das Tabelas
def BD_cad_produtos():
    conn = rota_banco()
    cursor = conn.cursor()

    #cursor.execute("INSERT INTO categorias VALUES (?, ?, ?)", (codigo, descricao))
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cad_produtos(
            codigo_produto INTEGER PRIMARY KEY,
            codigobarras INT(30) NOT NULL,
            descricao_produto VARCHAR(50) NOT NULL,
            marca VARCHAR(20) NOT NULL,
            categoria VARCHAR(40) NOT NULL,
            curva INT NOT NULL,
            custo DECIMAL(8,2) NOT NULL,
            venda DECIMAL(8,2) NOT NULL,
                   
            FOREIGN KEY (categoria) REFERENCES cad_categorias(descricao_categoria )
        )
    ''')
    print("Tabela de Produtos conectada\n")
    conn.commit()
    conn.close()
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
    print("Tabela de Categorias conectada\n")

    conn.commit() #Confirma as alterações
    conn.close() #Encerra o BD
def BD_cad_vendas():
    conn = rota_banco()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cad_vendas (
            codigo_venda INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo_produto INTEGER NOT NULL,
            quantidade_vendida INT(5) NOT NULL,
            periodo_vendas INT(3) NOT NULL,
            FOREIGN KEY (codigo_produto) REFERENCES cad_produtos(codigo_produto)
        )
    ''')
    print("Tabela de Vendas conectada\n")
    conn.commit()
    conn.close()

#BD_cad_vendas()
#BD_cad_produtos()
#BD_cad_categorias()

#3) Salvar Tabelas
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
def salvarProdutos(codigo_produto: int, codigobarras: int, descricao_produto: str, marca: str, categoria: str, custo: float, venda: float, curva: int):
    conn = rota_banco()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO cad_produtos (codigo_produto, codigobarras, descricao_produto, marca, categoria, custo, venda, curva)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (codigo_produto, codigobarras, descricao_produto, marca, categoria, custo, venda, curva))
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
def salvarVendas(codigo_produto: int, quantidade_vendida: int, periodo_vendas: int):
    conn = rota_banco()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO cad_vendas (codigo_produto, quantidade_vendida, periodo_vendas)
            VALUES (?, ?, ?)""",
            (codigo_produto, quantidade_vendida, periodo_vendas))
        conn.commit()
        print(f"Model: Dados de Vendas inseridos com sucesso! - Produto {codigo_produto}, {quantidade_vendida} em {periodo_vendas} dias.")
        return True
    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade ao salvar os dados de venda: {e}")
        return False
    except Exception as e:
        print(f"Erro geral ao salvar a venda: {e}")
        return False
    finally:
        conn.close()

def listarCategoriasModel():

    conn = rota_banco()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT descricao_categoria FROM cad_categorias")
        categorias = [row[0] for row in cursor.fetchall()]
        return categorias
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
def listarCodigoProdutosModel():
    conn = rota_banco()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT codigo_produto, descricao_produto FROM cad_produtos")
        codigo_pro = cursor.fetchall()
        return codigo_pro
    finally:
        conn.close()

def gerarSugestao(categoria, curva, periodo_reposicao):
    print(f"--- MODEL --- \nCategoria: '{categoria}' (Tipo: {type(categoria)}) \nCurva: '{curva}' (Tipo: {type(curva)}) \nPeríodo: '{periodo_reposicao}' (Tipo: {type(periodo_reposicao)}) \n")
    conn = rota_banco()
    cursor = conn.cursor()
    query = """
        SELECT p.codigo_produto, p.descricao_produto, c.descricao_categoria, p.custo, p.venda, v.quantidade_vendida, v.periodo_vendas
        FROM cad_vendas as v
        INNER JOIN
            cad_produtos AS p ON v.codigo_produto = p.codigo_produto
        INNER JOIN
            cad_categorias AS c ON p.categoria = c.descricao_categoria
        WHERE 1=1           
        """
    parametros = []

    if categoria != "Selecione a Categoria":
        query += " AND c.descricao_categoria = ?"
        parametros.append(categoria)
    
    if curva != 0:
        query += " AND p.curva = ?"
        parametros.append(curva)
    
    cursor.execute(query, tuple(parametros))
    dados_sugestao = cursor.fetchall()

    sugestao = []
    for linha in dados_sugestao:
        cod, desc, cat, custo, venda, qtd_vendida, periodo_venda = linha

        if periodo_venda == 0:
            continue
        
        try:
            custo_str = str(custo).replace(',', '.')
            venda_str = str(venda).replace(',', '.')
            custo_float = float(custo_str)
            venda_float = float(venda_str)
        except (ValueError, TypeError):
            print(f"Aviso: Ignorando linha com valor de custo/venda inválido. Custo: {custo_str}, Venda: {venda_str}")
            continue

        quantidade_sugerida = round((qtd_vendida / periodo_venda) * periodo_reposicao)
        custo_total = quantidade_sugerida * custo_float
        venda_total = quantidade_sugerida * venda_float

        if venda_float > 0:
            lucro = venda_float - custo_float
            margem = (lucro / venda_float) * 100
        else:
            lucro = -custo_float
            margem = -float('inf')

        sugestao.append(
            (cod, desc, cat, f"R$ {custo_float:.2f}", f"R$ {venda_float:.2f}", f"{margem:.2f}%",
            int(quantidade_sugerida), f"R${custo_total:.2f}", f"R${venda_total:.2f}"))
    
    return sugestao
