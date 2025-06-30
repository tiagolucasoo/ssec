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
        
        self.geometry("1000x800")
        self.title("SSEC - Sugestão de Compras")

        CONFIG_BOTOES = {"width":200, "height":50, "border_width":2, "border_color":'#000', "text_color":'#001F21'}
        CONFIG_INPUTS1 = {"width":600, "height":50, "border_width":0} #Para 1 por Linha
        CONFIG_INPUTS2 = {"width":275, "height":50, "border_width":0} #Para 2 por Linha
        #Categoria

        def categoriasExistentes():
            categorias = self.controller.listarCategorias()
            self.label5 = customtkinter.CTkLabel(self, text="Categorias Existentes", fg_color="transparent")
            self.label5.pack()
            #Fazer uma função para esse check de categoria que reutilizo na sugestão de compras
            self.box_categoria = customtkinter.CTkComboBox(self, **CONFIG_INPUTS1, values=list(categorias))
            self.box_categoria.set("Selecione a Categoria")
            self.box_categoria.pack()
            self.conferir_categorias = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#029B99", text="Conferir Categorias", command="")
            
        categorias = ("teste", "teste")
        label5 = customtkinter.CTkLabel(self, text="Categoria", fg_color="transparent")
        label5.pack(side="top", pady=20)
        #Fazer uma função para esse check de categoria que reutilizo na sugestão de compras
        combobox = customtkinter.CTkComboBox(self, **CONFIG_INPUTS1, values=list(categorias),
                                     command='')
        combobox.set("Selecione a Categoria")
        combobox.pack(side="top")

        label6 = customtkinter.CTkLabel(self, text="Curva de Vendas", fg_color="transparent")
        label6.pack(side="top", pady=20)

        container_radio = customtkinter.CTkFrame(self, fg_color="transparent")
        container_radio.pack(side="top")
        self.radio_var = customtkinter.Variable(value=0)

        
        radiobutton_0 = customtkinter.CTkRadioButton(container_radio, text="Todos", variable=self.radio_var, value=0)
        radiobutton_0.pack(side="left", padx=10, pady=20)
        radiobutton_1 = customtkinter.CTkRadioButton(container_radio, text="Curva A", variable=self.radio_var, value=1)
        radiobutton_1.pack(side="left", padx=10, pady=20)
        radiobutton_2 = customtkinter.CTkRadioButton(container_radio, text="Curva B", variable=self.radio_var, value=2)
        radiobutton_2.pack(side="left", padx=10, pady=20)
        radiobutton_3 = customtkinter.CTkRadioButton(container_radio, text="Curva C", variable=self.radio_var, value=3)
        radiobutton_3.pack(side="left", padx=10, pady=20)
        radiobutton_4 = customtkinter.CTkRadioButton(container_radio, text="Lançamento", variable=self.radio_var, value=4)
        radiobutton_4.pack(side="left", padx=10, pady=20)
        radiobutton_5 = customtkinter.CTkRadioButton(container_radio, text="Exclusivo", variable=self.radio_var, value=5)
        radiobutton_5.pack(side="left", padx=10, pady=20)

        ##### BLOCO DE PERÍODO
        label7 = customtkinter.CTkLabel(self, text="Período para reposição", fg_color="transparent")
        label7.pack(side="top", pady=20)

        container_radio1 = customtkinter.CTkFrame(self, fg_color="transparent")
        container_radio2 = customtkinter.CTkFrame(self, fg_color="transparent")
        container_radio1.pack(side="top")
        self.radio_var = customtkinter.Variable(value=0)

        
        radiobutton_10 = customtkinter.CTkRadioButton(container_radio1, text="15 Dias", variable=self.radio_var, value=0)
        radiobutton_10.pack(side="left", padx=10, pady=20)
        radiobutton_11 = customtkinter.CTkRadioButton(container_radio1, text="30 Dias", variable=self.radio_var, value=1)
        radiobutton_11.pack(side="left", padx=10, pady=20)
        radiobutton_12 = customtkinter.CTkRadioButton(container_radio1, text="45 Dias", variable=self.radio_var, value=2)
        radiobutton_12.pack(side="left", padx=10, pady=20)
        radiobutton_13 = customtkinter.CTkRadioButton(container_radio1, text="60 Dias", variable=self.radio_var, value=3)
        radiobutton_13.pack(side="left", padx=10, pady=20)
        radiobutton_14 = customtkinter.CTkRadioButton(container_radio1, text="75 Dias", variable=self.radio_var, value=4)
        radiobutton_14.pack(side="left", padx=10, pady=20)
        radiobutton_15 = customtkinter.CTkRadioButton(container_radio1, text="90 Dias", variable=self.radio_var, value=5)
        radiobutton_15.pack(side="left", padx=10, pady=20)

        container_radio2.pack(side="top")
        gerar = customtkinter.CTkButton(container_radio2, text="Gerar Sugestão")
        gerar.pack(side="left", padx=20)

        limpar = customtkinter.CTkButton(container_radio2, text="Limpar Dados")
        limpar.pack(side="left", padx=20)
    

open = view_importacao_manual()
open.mainloop()