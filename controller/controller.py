#Aqui funções Controller de Cadastro (Categoria e Produtos)
from model import model
import re

#Categoria - 100% OK

class controller_cadastro:
    def __init__(self):
        self._model_db = model
        self.view = None
        self.app = None

    def set_view(self, view_instance):
        self.view = view_instance
    
    def set_app(self, app_instance):
        self.app = app_instance

    def mostrar_erro(self, mensagem: str):
        if self.app:
            self.app.exibir_mensagem_erro(mensagem)

    def mostrar_sucesso(self, mensagem: str):
        if self.app:
            self.app.exibir_mensagem_sucesso(mensagem)

    def limpar_campos(self):
        if self.app:
            self.app.limpar_campos_view()

    def cadastrarCategoria(self, descricao_categoria):           
        if not self.validacao_cad_categoria(descricao_categoria):
            return False
        
        if self._model_db.salvarCategorias(descricao_categoria.strip()):
            print("Controller: Categoria salva com sucesso via Model.")
            self.mostrar_sucesso(f"Categoria '{descricao_categoria.strip()}' cadastrada!")
            return True  
                
        else:
            validacao_cat_2 = f"Categoria {descricao_categoria} cadastrada com sucesso!"
            print(validacao_cat_2)
            self.mostrar_sucesso(validacao_cat_2)

    def cadastrarProduto(self, codigobarras: int, descricao_produto: str, marca: str, categoria: str, custo: float, venda: float, curva: int):
        print(f"Cadastrando Produto: {descricao_produto}")

        if not self.validacao_cad_produto(codigobarras, descricao_produto, marca, categoria, custo, venda, curva):
            return False
        
        if self._model_db.salvarProdutos(codigobarras, descricao_produto.strip(), marca.strip(), categoria.strip(), custo, venda, curva):
            print("Controller: Produto salvo com sucesso via Model.")
            self.mostrar_sucesso(f"Produto '{descricao_produto.strip()}' cadastrado!")
            self.limpar_campos()# Pede para a View limpar os campos
            return True
        else:
            print("Controller: Falha ao salvar produto via Model.")
            return False
    def cadastrarVenda(self, codigo_produto, quantidade_vendida, periodo_vendas):
        if self._model_db.salvarVendas(codigo_produto, quantidade_vendida, periodo_vendas):
            return True
        else:
            return False
        
    def processarCaminho(self, arquivo_importado):
        if not arquivo_importado:
            print("Controller: Nenhum arquivo")
            return

        try:
            with open(arquivo_importado, mode='r', encoding='utf-8') as f:
            
                for numero_linha, linha_de_texto in enumerate(f, 1):
                    linha_limpa = linha_de_texto.strip()
                    if not linha_limpa:
                        continue

                    partes = linha_limpa.split(',')
                    
                    try:
                        if len(partes) >= 3:
                            codigo_produto = int(partes[0])
                            qtde_vendida = int(partes[1])
                            periodo = int(partes[2])

                            self.cadastrarVenda(codigo_produto, qtde_vendida, periodo)
                        else:
                            print(f"Aviso: Linha {numero_linha} ignorada. Formato inválido: {linha_limpa}")
                    except ValueError:
                        print(f"Aviso: Linha {numero_linha} ignorada. Contém dados não numéricos: {linha_limpa}")
            
                        self.mostrar_sucesso("Arquivo importado e vendas cadastradas com sucesso!")

        except FileNotFoundError:
            print(f"Erro no Controller: Arquivo não encontrado em '{arquivo_importado}'")
            self.mostrar_erro(f"Arquivo não encontrado no caminho especificado.")
        except Exception as e:
            print(f"Erro no Controller: {e}")
            self.mostrar_erro(f"Ocorreu um erro ao processar o arquivo.")

    def listarCategorias(self):
        return self._model_db.listarCategoriasModel()
    
    def validacao_cad_categoria(self, descricao_categoria: str):
        categorias_existentes = self._model_db.listarCategoriasModel()
        lista_formatada = [cat.lower() for cat in categorias_existentes]
        lista_limpa = descricao_categoria.strip()
        
        if not lista_limpa:
            validacao_cat_1 = "A descrição da categoria não pode ser vazia!"
            print(validacao_cat_1)
            self.mostrar_erro(validacao_cat_1)
            return False
        
        if descricao_categoria.lower() in list(lista_formatada):
            validacao_cat_3 = f"A categoria {descricao_categoria} já está cadastrada no banco!"
            print(validacao_cat_3)
            self.mostrar_erro(validacao_cat_3)
            return False
        
        if descricao_categoria.isdigit():
            validacao_cat_4 = f"Você digitou {descricao_categoria}, apenas números não são aceitos como nome de categorias, digite um nome válido!"
            print(validacao_cat_4)
            self.mostrar_erro(validacao_cat_4)
            return False
        if not re.search(r"[a-zA-Z0-9]", lista_limpa):
            validacao_cat_5 = "A categoria não pode ser composta apenas de caracteres especiais!"
            print(validacao_cat_5)
            self.mostrar_erro(validacao_cat_5)
        else:
            return True
    def validacao_cad_produto(self, codigobarras: int, descricao_produto: str, marca: str, categoria: str, custo: float, venda: float, curva: int):
            if not descricao_produto.strip() or not marca.strip() or not categoria.strip():
                self.mostrar_erro("Confira os campos descrição, marca e categoria!")
                return False

            if not isinstance(codigobarras, int) or codigobarras <= 0:
                self.mostrar_erro("Código de Barras inválido.")
                return False
                
            if not isinstance(custo, (float, int)) or custo <= 0:
                self.mostrar_erro("Custo inválido, preencha um valor")
                return False

            if not isinstance(venda, (float, int)) or venda <= 0:
                self.mostrar_erro("Valor de Venda inválido, preencha um valor")
                return False
            
            if not isinstance(curva, (int)) or curva <= 0 or curva > 5:
                self.mostrar_erro("Insira a curva de vendas do Produto")
                return False
            
            return True
    
    
    def obter_sugestao_de_compra(self, categoria, curva, periodo):
        print(f"Controller: Recebido pedido para Categoria={categoria}, Curva={curva}, Período={periodo}")
        resultados_do_banco = self._model_db.gerarSugestao(categoria, curva, periodo)

        return resultados_do_banco