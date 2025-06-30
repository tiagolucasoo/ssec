import customtkinter
import tkinter as tk
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

class view_importacao_manual(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x800")
        self.title("SSEC - Importação Manual")
        
        
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

        #Código de Barras
        label2 = customtkinter.CTkLabel(self, text="Código do Produto", fg_color="transparent")
        label2.pack()
        entry2 = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Digite aqui o valor")
        entry2.pack()

        #Categoria
        categorias = ("teste", "teste")
        label5 = customtkinter.CTkLabel(self, text="Categoria", fg_color="transparent")
        label5.pack()
        #Fazer uma função para esse check de categoria que reutilizo na sugestão de compras
        combobox = customtkinter.CTkComboBox(self, **CONFIG_INPUTS2, values=list(categorias),
                                     command='')
        combobox.set("Selecione a Categoria")
        combobox.pack()

        #Descrição do Produto
        label3 = customtkinter.CTkLabel(self, text="Período de venda (Dias)", fg_color="transparent")
        label3.pack()
        entry3 = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Exemplo: 30")
        entry3.pack()

        button = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#ffff00", text="Limpar", command=temaDark)
        button.pack()

        button = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#008000", text="Salvar", command=temaSystem)
        button.pack()

open = view_importacao_manual()
open.mainloop()