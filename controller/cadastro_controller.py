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
        if descricao_categoria.lower() in categorias_existentes:
            if self.view:
                self.view.exibir_mensagem_erro("Ajá existe")
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
            # Mensagem de erro já deve ter sido exibida pelo Model ou View
            return False

    def listarCategorias(self):
        return self._model_db.listarCategoriasModel()
    
    
'''
def limparCategoria(self):
    self.descricao_categoria.delete(0, 'end')
    print('Categoria Limpa')
'''