import customtkinter
from tkinter.filedialog import askopenfilename

from controller.controller import controller_cadastro

from tkinter import Menu

import subprocess
import sys
import os

'''
Código Produto - Código de Barras
Descrição do Produto
Marca - Categoria[]
Custo - Marcação - Venda
'''

class view_importacao_lote(customtkinter.CTkFrame):
    def __init__(self):
        super().__init__()

        self.geometry("1000x800")
        self.title("SSEC - Importar Produtos em Lote")
        self.controller = controller_cadastro()
        self.controller.set_view(self)

        # ----- ÍNICIO DO MENU -----
        def ALTERAR_TELA(link):
            executavel = sys.executable
            diretorio = os.path.dirname(__file__)
            exibir_tela = os.path.join(diretorio, link)
            subprocess.Popen([executavel, exibir_tela])
            self.destroy()

        def temaSystem():
            return customtkinter.set_appearance_mode("system")
        def temaDark():
            return customtkinter.set_appearance_mode("dark")
        
        def exibirMenu():
            barra_menu = Menu(self)

            menu_1 = Menu(barra_menu, tearoff=0)
            menu_1.add_command(label="Página Inicial", command=lambda: ALTERAR_TELA("main.py"))
            menu_1.add_separator()
            menu_1.add_command(label="Sair", command=self.quit)
            barra_menu.add_cascade(label="Página Inicial", menu=menu_1)

            menu_2 = Menu(barra_menu, tearoff=0)
            menu_2.add_command(label="Produtos", command=lambda: ALTERAR_TELA("cadastro_produtos_view.py"))
            menu_2.add_command(label="Categorias", command=lambda: ALTERAR_TELA("cadastro_categorias_view.py"))
            menu_2.add_command(label="Vendas", command=lambda: ALTERAR_TELA("importacao_manual_view.py"))
            barra_menu.add_cascade(label="Cadastro", menu=menu_2)

            menu_3 = Menu(barra_menu, tearoff=0)
            menu_3.add_command(label="Produtos em lote", command=lambda: ALTERAR_TELA("importacao_produtos_view.py"))
            menu_3.add_command(label="Relatório de Vendas", command=lambda: ALTERAR_TELA("importacao_lote_view.py"))
            barra_menu.add_cascade(label="Importar", menu=menu_3)

            menu_4 = Menu(barra_menu, tearoff=0)
            menu_4.add_command(label="Sugestão de Compras", command=lambda: ALTERAR_TELA("sugestao_compras_view.py"))
            barra_menu.add_cascade(label="Compras", menu=menu_4)

            menu_5 = Menu(barra_menu, tearoff=0)
            menu_5.add_command(label="Modo Escuro", command=temaDark)
            menu_5.add_command(label="Modo Claro", command=temaSystem)
            barra_menu.add_cascade(label="Aparência", menu=menu_5)

            self.config(menu=barra_menu)
        
        exibirMenu()
        # ----- FIM DO MENU ----- #

        CONFIG_BOTOES = {"width":200, "height":50, "border_width":2, "border_color":'#000', "text_color":'#001F21'}
        #CONFIG_INPUTS1 = {"width":600, "height":50, "border_width":0} #Para 1 por Linha
        CONFIG_INPUTS2 = {"width":275, "height":50, "border_width":0} #Para 2 por Linha

        def selecionar_arquivo():
            rota = askopenfilename(
                title="Selecione um arquivo .txt",
                filetypes=(("Arquivos de Texto", "*txt"), ("Todos os arquivos", "*.*"))
            )
            if rota:
                self.label.configure(text="VOCÊ SELECIONOU:")
                self.label.pack()
                self.caminho_arquivo.configure(text=rota)

                button1.pack()
                button2.pack()
            else:
                self.caminho_arquivo.configure(text="Nenhum arquivo selecionado!")
            return rota
        info0 = str("Como cadastrar Produtos em Lote?")
        info1 = str("""
            1º Crie um arquivo de texto (.txt)
                    
            2º Utilize a sequência: Código de Produto, Descrição, Marca, Categoria, Custo, Venda
                    
            3º Para cada produto digitado finalize a linha com duas vírgulas, faça o mesmo nas linhas seguintes.
                    
            Exemplo:
            1010, Energético Furioso 250ml Tradicional, Furioso,2,(1.49),(3.49),,
            1011, Energético Furioso 250ml Citrus, Furioso,2,(1.49),(3.49),, 
        """)

        descricao_label1 = customtkinter.CTkLabel(self, text=info0, fg_color="transparent", width=600, height=50)
        descricao_label2 = customtkinter.CTkLabel(self, text=info1, fg_color="transparent", width=600)

        descricao_label1.pack()
        descricao_label2.pack()

        buscar_arquivo = customtkinter.CTkButton(self, **CONFIG_BOTOES, text="teste", command=selecionar_arquivo)
        buscar_arquivo.pack()

        #Descrição do Produto
        self.label = customtkinter.CTkLabel(self, text="", fg_color="transparent")
        self.label.pack()
        self.caminho_arquivo = customtkinter.CTkLabel(self, text="Nenhum arquivo selecionado", fg_color="transparent")
        self.caminho_arquivo.pack()

        button1 = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#ffff00", text="Limpar", command="")
        button2 = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#008000", text="Salvar", command=self.salvar_dados)
        

    def salvar_dados(self):
            try:
                # Pega o TEXTO de dentro da label
                caminho_do_arquivo = self.caminho_arquivo.cget("text")

                # Verificação de segurança: não processar se nenhum arquivo foi escolhido
                if not caminho_do_arquivo or caminho_do_arquivo == "Nenhum arquivo selecionado":
                    print("Nenhum arquivo válido selecionado para processar.")
                    # Você pode mostrar uma messagebox de erro aqui
                    return

                # Agora sim, passa a STRING com o caminho para o controller
                self.controller.processarCaminho(caminho_do_arquivo)

                
            except Exception as e:
                print(f"Erro na view ao salvar dados: {e}")
