#Aqui funções Controller de Cadastro (Categoria e Produtos)
from model import model

class controller_cadastro:
    def __init__(self):
        self._model_db = model
        self.view = None

    def set_view(self, view_instance):
        self.view = view_instance

    def mostrar_erro(self, mensagem: str):
        if self.view:
            self.view.exibir_mensagem_erro(mensagem)
    def mostrar_sucesso(self, mensagem: str):
        if self.view:
            self.view.exibir_mensagem_sucesso(mensagem)
    def limpar_campos(self):
        if self.view:
            self.view.limpar_campos_view()

    def cadastrarCategoria(self, descricao_categoria):
        print(f"cadastrar Categoria {descricao_categoria}")

        if not self.validacao_cad_categoria(descricao_categoria):
            return False
        if self._model_db.salvarCategorias(descricao_categoria.strip()):
            print("Controller: Categoria salva com sucesso via Model.")
            self.mostrar_sucesso(f"Categoria '{descricao_categoria.strip()}' cadastrada!")
            self.limpar_campos()
            return True
        
        else:
            print("Controller: Falha ao salvar categoria via Model (já existe ou erro).")
            return False
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
            
            # Loop para ler cada linha do arquivo
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

                            # 3. AQUI É A PARTE CRUCIAL:
                            # Chame o método para salvar esta linha no banco de dados.
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
            print(f"Erro inesperado no Controller: {e}")
            self.mostrar_erro(f"Ocorreu um erro inesperado ao processar o arquivo.")




    def listarCategorias(self):
        return self._model_db.listarCategoriasModel()
    
    def validacao_cad_categoria(self, descricao_categoria: str):
        categorias_existentes = self._model_db.listarCategoriasModel()

        if not descricao_categoria.strip():
            self.mostrar_erro("A descrição da categoria não pode ser vazia")
            return False
        if descricao_categoria in list(categorias_existentes):
            self.mostrar_erro("Essa categoria já existe")
            return False
        
        return True
    def validacao_cad_produto(self, codigobarras: int, descricao_produto: str, marca: str, categoria: str, custo: float, venda: float, curva: int):
            if not descricao_produto.strip() or not marca.strip() or not categoria.strip():
                self.mostrar_erro("Preencha os Campos de 'Descrição', 'Marca' e 'Categoria' são obrigatórios.")
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
            
            if not isinstance(curva, (int)) or curva <= 1 or curva > 5:
                self.mostrar_erro("Insira a curva de vendas do Produto")
                return False
            
            return True
    
        # Dentro da sua classe de controller
    
    def obter_sugestao_de_compra(self, categoria, curva, periodo):
        print(f"Controller: Recebido pedido para Categoria={categoria}, Curva={curva}, Período={periodo}")

        # Repassa a responsabilidade para o Model
        # (Você precisará criar esta função no model)
        resultados_do_banco = self._model_db.gerarSugestao(categoria, curva, periodo)

        return resultados_do_banco