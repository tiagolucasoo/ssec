import customtkinter
from tkinter.filedialog import askopenfilename
from PIL import Image
import os

from controller.controller import controller_cadastro
import tkinter as tk

class view_importacao_produtos(customtkinter.CTkFrame):
    def __init__(self, parent, controller_instance):
        super().__init__(parent)

        self.controller = controller_instance

        # Rodapé
        info_ssec = customtkinter.CTkLabel(self, text="SSEC - Versão 1.0 | Desenvolvido por Tiago Lucas (GitHub: Tiagolucasoo)", fg_color="transparent")
        info_ssec.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)
        
        CONFIG_BOTOES1 = {"width":200, "height":50, "text_color":'#001F21'}
        CONFIG_BOTOES2 = {"width":600, "height":50, "text_color":'#ffffff'}
        #CONFIG_INPUTS1 = {"width":600, "height":50, "border_width":0} #Para 1 por Linha
        CONFIG_INPUTS2 = {"width":275, "height":50, "border_width":0} #Para 2 por Linha

        logo_ssec = customtkinter.CTkImage(light_image=Image.open("img/img_produtos_light.png"),
                                  dark_image=Image.open("img/img_produtos_dark.png"),
                                  size=(600, 165))
        logo = customtkinter.CTkLabel(self, image=logo_ssec, text="")
        logo.pack(pady=25)

        def selecionar_arquivo():
            rota = askopenfilename(
                title="Selecione um arquivo .txt",
                filetypes=(("Arquivos de Texto", "*txt"), ("Todos os arquivos", "*.*")))
            if rota:
                self.label.configure(text="VOCÊ SELECIONOU:")
                self.label.pack()
                self.caminho_arquivo.configure(text=rota)

                self.button1.pack(side="left", padx=20, pady=30)
                self.button2.pack(side="left", padx=20, pady=30)

            else:
                self.caminho_arquivo.configure(text="Nenhum arquivo selecionado!")
            return rota

        buscar_arquivo = customtkinter.CTkButton(self, **CONFIG_BOTOES2, text="Selecione o Arquivo", command=selecionar_arquivo, fg_color="#1a5a8f", hover_color="#12436A")
        buscar_arquivo.pack(pady=20)

        #Arquivo
        self.label = customtkinter.CTkLabel(self, text="", fg_color="transparent")
        self.label.pack()
        self.caminho_arquivo = customtkinter.CTkLabel(self, text="Nenhum arquivo selecionado", fg_color="transparent")
        self.caminho_arquivo.pack()

        container_botoes = customtkinter.CTkFrame(self, fg_color="transparent")
        container_botoes.pack(side="top")

        self.button1 = customtkinter.CTkButton(container_botoes, **CONFIG_BOTOES1, fg_color="#ffc107", hover_color="#e0a800", text="Limpar", command=self.limpar_dados)
        self.button2 = customtkinter.CTkButton(container_botoes, **CONFIG_BOTOES1, fg_color="#28a745", hover_color="#218838", text="Inserir Dados", command=self.salvar_dados)
        
    def salvar_dados(self):
            try:
                caminho_do_arquivo_p = self.caminho_arquivo.cget("text")

                if not caminho_do_arquivo_p or caminho_do_arquivo_p == "Nenhum arquivo selecionado":
                    print("Nenhum arquivo válido selecionado para processar.")
                    return
                self.controller.processarCaminhoProdutos(caminho_do_arquivo_p)
                
            except Exception as e:
                print(f"Erro na view ao salvar dados: {e}")

    def limpar_dados(self):
        self.caminho_arquivo.configure(text="")
        self.label.configure(text="Nenhum Arquivo Selecionado")
        self.button1.pack_forget()
        self.button2.pack_forget()
        os.system('cls')
        print("-- Terminal e demais campos limpos")