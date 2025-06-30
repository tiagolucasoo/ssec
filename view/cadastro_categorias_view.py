import customtkinter
import tkinter as tk
from tkinter import Menu
from controller.cadastro_controller import controller_cadastro

import subprocess
import sys
import os


#cadastro_categorias_view.py
#Fazer padrão botões 200x50 e entry em 2 medidas - 600x50 (Apenas 1) - 275x50 (2)

class view_cadastro_categorias(customtkinter.CTk):
    def __init__(self, controller_instance=None):
        super().__init__()

        self.geometry("1000x800")
        self.title("SSEC - Cadastro de Categorias")
        self.controller = controller_instance
        self.conferir_categorias = None

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
            menu_1.add_command(label="Página Inicial", command="")
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

        def configuracao_form(): #Width, Height e características padrão para o formulário (Fazer o chamado em Kwargs **)
            CONFIG_BOTOES = {"width":200, "height":50, "border_width":0, "border_color":'#000', "text_color":'#001F21'}
            CONFIG_INPUTS1 = {"width":600, "height":50, "border_width":0} #1 por Linha
            CONFIG_INPUTS2 = {"width":275, "height":50} #2 por Linha
            return CONFIG_BOTOES, CONFIG_INPUTS1, CONFIG_INPUTS2
        CONFIG_BOTOES, CONFIG_INPUTS1, CONFIG_INPUTS2 = configuracao_form()
        
        #Código da Categoria
        self.label_codigo_categoria = customtkinter.CTkLabel(self, width=600, height=50, text="Código da Categoria", fg_color="transparent")
        self.label_codigo_categoria.pack()
        self.label2_codigo_categoria = customtkinter.CTkLabel(self, width=600, height=50, text="", fg_color="white")
        self.label2_codigo_categoria.pack()

        #Descrição da Categoria
        self.label_desc_categoria = customtkinter.CTkLabel(self, text="Nome da Categoria", fg_color="transparent")
        self.label_desc_categoria.pack()
        self.input_desc_categoria = customtkinter.CTkEntry(self, **CONFIG_INPUTS1, placeholder_text="Digite aqui o nome da categoria")
        self.input_desc_categoria.pack()

        #Categorias existentes
        def categoriasExistentes():
            categorias = self.controller.listarCategorias()
            self.label5 = customtkinter.CTkLabel(self, text="Categorias Existentes", fg_color="transparent")
            self.label5.pack()
            #Fazer uma função para esse check de categoria que reutilizo na sugestão de compras
            self.box_categoria = customtkinter.CTkComboBox(self, **CONFIG_INPUTS1, values=list(categorias))
            self.box_categoria.set("Selecione a Categoria")
            self.box_categoria.pack()
            self.conferir_categorias = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#029B99", text="Conferir Categorias", command="")
            

        #Botões Limpar e Salvar


        self.limpar_categoria = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#ECC039", text="Limpar", command=self.limpar_campos_view)
        self.limpar_categoria.pack()
        self.salvar_categoria = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#DE4F15", text="Salvar", command=self.salvar_dados_da_view)
        self.salvar_categoria.pack()

        if self.conferir_categorias is not None:
                self.conferir_categorias.destroy()
                self.conferir_categorias = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#029B99", text="Conferir Categorias", command="")
                self.conferir_categorias.pack()
        elif self.conferir_categorias is None:
            self.conferir_categorias = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#029B99", text="Conferir Categorias", command=categoriasExistentes)
            self.conferir_categorias.pack()

    def salvar_dados_da_view(self):
        # Obtém os dados dos campos de entrada
        # (Você mencionou "Código do Produto" e "Descrição da Categoria")
        # Adapte as variáveis conforme o que você quer salvar
        # Por enquanto, estou usando 'descricao_categoria' como exemplo de dado a ser salvo
        descricao_categoria = self.input_desc_categoria.get()

        # Chama o Controller, passando a descrição da categoria
        # Note que o Controller precisa de um método que receba esses argumentos
        self.controller.cadastrarCategoria(descricao_categoria) # <--- CHAMA O CONTROLLER

    def limpar_campos_view(self):
        self.input_codigo_categoria.delete(0, tk.END)
        self.input_desc_categoria.delete(0, tk.END)
        self.input_codigo_categoria.focus_set()
        self.box_categoria("Selecione a Categoria")
        print("View: Campos de entrada limpos.")

    def on_combobox_select(self, choice):
        print(f"View: Categoria selecionada no ComboBox: {choice}")

    def exibir_mensagem_sucesso(self, mensagem):
        tk.messagebox.showinfo("Sucesso", mensagem)
        self.limpar_campos_view()

    def exibir_mensagem_erro(self, mensagem):
        tk.messagebox.showerror("Erro", mensagem)


    def atualizar_combobox_categorias(self):
        categorias_do_db = self.controller.obter_categorias_para_view()
        if categorias_do_db:
            self.box_categoria.configure(values=categorias_do_db)
        else:
            self.box_categoria.configure(values=["Nenhuma Categoria"])
        self.box_categoria.set("Selecione a Categoria")