import customtkinter
from tkinter.filedialog import askopenfilename

from controller.controller import controller_cadastro
import tkinter as tk

class view_importacao_lote(customtkinter.CTkFrame):
    def __init__(self, parent, controller_instance):
        super().__init__(parent)

        self.controller = controller_instance
        self.controller.set_view(self)

        CONFIG_BOTOES = {"width":200, "height":50, "border_width":2, "border_color":'#000', "text_color":'#001F21'}
        #CONFIG_INPUTS1 = {"width":600, "height":50, "border_width":0} #Para 1 por Linha
        CONFIG_INPUTS2 = {"width":275, "height":50, "border_width":0} #Para 2 por Linha

        def selecionar_arquivo():
            rota = askopenfilename(
                title="Selecione um arquivo .txt",
                filetypes=(("Arquivos de Texto", "*txt"), ("Todos os arquivos", "*.*")))
            if rota:
                self.label.configure(text="VOCÊ SELECIONOU:")
                self.label.pack()
                self.caminho_arquivo.configure(text=rota)

                button1.pack()
                button2.pack()
            else:
                self.caminho_arquivo.configure(text="Nenhum arquivo selecionado!")
            return rota
        info0 = str("Como Importar o Arquivo de Vendas?")
        info1 = str("""
            1º Crie um arquivo de texto (.txt)
                    
            2º Utilize a sequência: Código de Produto, Quantidade Vendida, Período de Vendas (Dias)
                    
            3º Para cada produto digitado finalize a linha com duas vírgulas, faça o mesmo nas linhas seguintes.

            Observação: É necessário que o produto esteja cadastrado no sistema para fazer a importação!
                    
            Exemplo:
            10,30,30,,
            20,30,30,,
        """)

        descricao_label1 = customtkinter.CTkLabel(self, text=info0, fg_color="transparent", width=600, height=50)
        descricao_label2 = customtkinter.CTkLabel(self, text=info1, fg_color="transparent", width=600)

        descricao_label1.pack()
        descricao_label2.pack()

        buscar_arquivo = customtkinter.CTkButton(self, **CONFIG_BOTOES, text="Selecione o Arquivo", command=selecionar_arquivo)
        buscar_arquivo.pack()

        #Arquivo
        self.label = customtkinter.CTkLabel(self, text="", fg_color="transparent")
        self.label.pack()
        self.caminho_arquivo = customtkinter.CTkLabel(self, text="Nenhum arquivo selecionado", fg_color="transparent")
        self.caminho_arquivo.pack()

        button1 = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#ECC039", text="Limpar", command="")
        button2 = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#DE4F15", text="Salvar", command=self.salvar_dados)
        
    def salvar_dados(self):
            try:
                caminho_do_arquivo = self.caminho_arquivo.cget("text")

                if not caminho_do_arquivo or caminho_do_arquivo == "Nenhum arquivo selecionado":
                    print("Nenhum arquivo válido selecionado para processar.")
                    return
                self.controller.processarCaminho(caminho_do_arquivo)
                
            except Exception as e:
                print(f"Erro na view ao salvar dados: {e}")
