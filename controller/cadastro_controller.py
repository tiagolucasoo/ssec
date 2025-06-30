#Aqui funções Controller de Cadastro (Categoria e Produtos)
from model import cadastro_model

#cadastro_controller.py

'''
input_codigo_categoria
inpút_desc_categoria


 CREATE TABLE cad_categorias(
        codigo_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao_produto VARCHAR(50) NOT NULL
    );
'''
class controller_cadastro:
    def __init__(self):
        self._model_db = cadastro_model
        self.view = None

    def set_view(self, view_instance):
        self.view = view_instance

    def cadastrarCategoria(self, descricao_categoria: str):
        print(f"cadastrar Categoria {descricao_categoria}")

        #Validação
        categorias_existentes = self._model_db.listarCategoriasModel()

        if not descricao_categoria.strip():
            if self.view:
                self.view.exibir_mensagem_erro("A descrição da categoria não pode ser vazia")
            return False
        if descricao_categoria in list(categorias_existentes):
            if self.view:
                self.view.exibir_mensagem_erro("Essa categoria já existe")
            return False

        #Chama o model
        if self._model_db.salvarCategorias(descricao_categoria.strip()):
            print("Controller: Categoria salva com sucesso via Model.")
            if self.view:
                self.view.exibir_mensagem_sucesso(f"Categoria '{descricao_categoria.strip()}' cadastrada!")
                self.view.limpar_campos_view() # Pede para a View limpar os campos
                #self.view.atualizar_combobox_categorias() # Atualiza o combobox na View
            return True
        else:
            print("Controller: Falha ao salvar categoria via Model (já existe ou erro).")
            return False

    def listarCategorias(self):
        return self._model_db.listarCategoriasModel()
    
    
    '''
    def limparCategoria(self):
        self.descricao_categoria.delete(0, 'end')
        print('Categoria Limpa')
    '''

    def cadastrarProduto(self, codigobarras: int, descricao_produto: str, marca: str, categoria: str, custo: float, venda: float, curva: int):
        print(f"Cadastrando Produto: {descricao_produto}")

        # --- Validações ---
        if not descricao_produto.strip() or not marca.strip() or not categoria.strip():
            if self.view:
                self.view.exibir_mensagem_erro("Preencha os Campos de 'Descrição', 'Marca' e 'Categoria' são obrigatórios.")
            return False

        if not isinstance(codigobarras, int) or codigobarras <= 0:
            if self.view:
                self.view.exibir_mensagem_erro("Código de Barras inválido.")
            return False
            
        if not isinstance(custo, (float, int)) or custo <= 0:
            if self.view:
                self.view.exibir_mensagem_erro("Custo inválido, preencha um valor")
            return False

        if not isinstance(venda, (float, int)) or venda <= 0:
            if self.view:
                self.view.exibir_mensagem_erro("Valor de Venda inválido, preencha um valor")
            return False
        
        if not isinstance(curva, (int)) or curva <= 1 or curva > 5:
            if self.view:
                self.view.exibir_mensagem_erro("Insira a curva de vendas do Produto")
            return False

        # Chama o Model para salvar
        if self._model_db.salvarProdutos(codigobarras, descricao_produto.strip(), marca.strip(), categoria.strip(), custo, venda, curva):
            print("Controller: Produto salvo com sucesso via Model.")
            if self.view:
                self.view.exibir_mensagem_sucesso(f"Produto '{descricao_produto.strip()}' cadastrado!")
                self.view.limpar_campos_view() # Pede para a View limpar os campos
            return True
        else:
            print("Controller: Falha ao salvar produto via Model.")
            return False