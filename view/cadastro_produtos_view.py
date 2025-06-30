import customtkinter
import tkinter as tk
from tkinter import Menu

from controller.cadastro_controller import controller_cadastro

import subprocess
import sys
import os
'''
Código Produto - Código de Barras
Descrição do Produto
Marca - Categoria[]
Custo - Marcação - Venda
'''

class view_cadastro_produtos(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x800")
        self.title("SSEC - Cadastro de Produtos")
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
        CONFIG_INPUTS1 = {"width":600, "height":50, "border_width":0} #Para 1 por Linha
        CONFIG_INPUTS2 = {"width":275, "height":50, "border_width":0} #Para 2 por Linha

        #Código da Categoria
        self.label = customtkinter.CTkLabel(self, text="Código", fg_color="transparent")
        self.label.pack()
        self.entry = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Exemplo: 1010")
        self.entry.pack()

        #Código de Barras
        self.label2 = customtkinter.CTkLabel(self, text="Código de Barras", fg_color="transparent")
        self.label2.pack()
        self.input_codigobarras = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Exemplo: 7896051020127")
        self.input_codigobarras.pack()

        #Descrição do Produto
        self.label3 = customtkinter.CTkLabel(self, text="Descrição do Produto", fg_color="transparent")
        self.label3.pack()
        self.input_descricao_produto = customtkinter.CTkEntry(self, **CONFIG_INPUTS1, placeholder_text="Exemplo: Energético Furioso 300ml Tradicional")
        self.input_descricao_produto.pack()

        #Marca
        self.label4 = customtkinter.CTkLabel(self, text="Marca", fg_color="transparent")
        self.label4.pack()
        self.input_marca = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Value")
        self.input_marca.pack()

        # Categoria (ComboBox)
        self.label_categoria = customtkinter.CTkLabel(self, text="Categoria", fg_color="transparent")
        self.label_categoria.pack()

        self.box_categoria = customtkinter.CTkComboBox(
            self,
            width=275,
            height=50,
            border_width=0,
            values=self.controller.listarCategorias(),  # Puxa categorias do banco
            command=self.on_combobox_select  # sem aspas! é uma função
        )
        self.box_categoria.pack()
        self.atualizar_combobox_categorias()

        # Custo e Venda (Adicione as entradas para esses campos)
        self.label_custo = customtkinter.CTkLabel(self, text="Custo (R$)", fg_color="transparent")
        self.label_custo.pack()
        self.input_custo = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Exemplo: 5.50")
        self.input_custo.pack()

        self.label_venda = customtkinter.CTkLabel(self, text="Venda (R$)", fg_color="transparent")
        self.label_venda.pack()
        self.input_venda = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Exemplo: 9.90")
        self.input_venda.pack()

        container_radio1 = customtkinter.CTkFrame(self, fg_color="transparent")
        container_radio1.pack(side="top")

        label6 = customtkinter.CTkLabel(self, text="Tipo de Produto", fg_color="transparent")
        label6.pack()
        self.radio_var = customtkinter.Variable(value=0)
        radiobutton_1 = customtkinter.CTkRadioButton(container_radio1, text="1) Curva A", variable=self.radio_var, value=1)
        radiobutton_1.pack(side="left")
        radiobutton_2 = customtkinter.CTkRadioButton(container_radio1, text="1) Curva B", variable=self.radio_var, value=2)
        radiobutton_2.pack(side="left")
        radiobutton_3 = customtkinter.CTkRadioButton(container_radio1, text="1) Curva C", variable=self.radio_var, value=3)
        radiobutton_3.pack(side="left")
        radiobutton_4 = customtkinter.CTkRadioButton(container_radio1, text="1) Lançamento", variable=self.radio_var, value=4)
        radiobutton_4.pack(side="left")
        radiobutton_5 = customtkinter.CTkRadioButton(container_radio1, text="1) Exclusivo", variable=self.radio_var, value=5)
        radiobutton_5.pack(side="left")

        button1 = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#ECC039", text="Limpar", command=self.limpar_campos_view)
        button1.pack()

        button2 = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#DE4F15", text="Cadastrar", command=self.salvar_dados_da_view)
        button2.pack()

    def salvar_dados_da_view(self):
        try:
            # Obter os dados dos campos de entrada
            codigobarras = int(self.input_codigobarras.get())
            descricao_produto = self.input_descricao_produto.get()
            marca = self.input_marca.get()
            categoria = self.box_categoria.get() # Pega o valor selecionado no combobox
            custo = float(self.input_custo.get().replace(',', '.')) # Para aceitar vírgula como decimal
            venda = float(self.input_venda.get().replace(',', '.')) # Para aceitar vírgula como decimal
            curva = int(self.radio_var.get())

            # Chama o Controller para cadastrar o produto
            self.controller.cadastrarProduto(codigobarras, descricao_produto, marca, categoria, custo, venda, curva)
        except ValueError:
            self.exibir_mensagem_erro("Por favor, insira valores numéricos válidos para Código de Barras, Custo e Venda.")
        except Exception as e:
            self.exibir_mensagem_erro(f"Erro ao salvar produto: {e}")
    
    def limpar_campos_view(self):
        # self.input_codigo.delete(0, tk.END) # Se você manteve um campo de código editável
        self.input_codigobarras.delete(0, tk.END)
        self.input_descricao_produto.delete(0, tk.END)
        self.input_marca.delete(0, tk.END)
        self.input_custo.delete(0, tk.END)
        self.input_venda.delete(0, tk.END)
        self.box_categoria.set("Selecione a Categoria")
        self.radio_var.set(0) # Limpa os radio buttons
        self.input_codigobarras.focus_set() # Define o foco para o primeiro campo
        print("View: Campos de entrada limpos.")
    
    def on_combobox_select(self, choice):
        print(f"View: Categoria selecionada no ComboBox: {choice}")

    def exibir_mensagem_sucesso(self, mensagem):
        tk.messagebox.showinfo("Sucesso", mensagem)
        self.limpar_campos_view() # Limpa os campos após o sucesso

    def exibir_mensagem_erro(self, mensagem):
        tk.messagebox.showerror("Erro", mensagem)

    def atualizar_combobox_categorias(self):
        categorias = self.controller.listarCategorias()
        self.box_categoria.configure(values=categorias)
        if categorias:
            self.box_categoria.set("Selecione a Categoria")


open = view_cadastro_produtos()
open.mainloop()