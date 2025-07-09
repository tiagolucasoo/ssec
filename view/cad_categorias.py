import customtkinter
import tkinter as tk
from tkinter import messagebox
import os 

from controller.controller import controller_cadastro

class view_cadastro_categorias(customtkinter.CTkFrame):
    def __init__(self, parent, controller_instance):
        super().__init__(parent)

        self.controller = controller_instance
        self.conferir_categorias = None

        def configuracao_form(): #Width, Height e características padrão para o formulário (Fazer o chamado em Kwargs **)
            CONFIG_BOTOES = {"width":200, "height":50, "border_width":0, "border_color":'#000', "text_color":'#001F21'}
            CONFIG_INPUTS1 = {"width":600, "height":50, "border_width":0} #1 por Linha
            CONFIG_INPUTS2 = {"width":275, "height":50} #2 por Linha
            return CONFIG_BOTOES, CONFIG_INPUTS1, CONFIG_INPUTS2
        
        CONFIG_BOTOES, CONFIG_INPUTS1, CONFIG_INPUTS2 = configuracao_form()
        
        #Código da Categoria
        self.label_codigo_categoria = customtkinter.CTkLabel(self, width=600, height=50, text="Código da Categoria", fg_color="transparent")
        self.label2_codigo_categoria = customtkinter.CTkLabel(self, width=600, height=50, text="", fg_color="transparent")
        self.label2_codigo_categoria.pack()

        #Descrição da Categoria
        self.label_desc_categoria = customtkinter.CTkLabel(self, text="Nome da Categoria", fg_color="transparent")
        self.label_desc_categoria.pack()
        self.input_desc_categoria = customtkinter.CTkEntry(self, **CONFIG_INPUTS1, placeholder_text="Digite aqui o nome da categoria")
        self.input_desc_categoria.pack()

        #Categorias existentes 000
        def categoriasExistentes():
            categorias = self.controller.listarCategorias()
            self.label5 = customtkinter.CTkLabel(self, text="Categorias Existentes", fg_color="transparent")
            #Fazer uma função para esse check de categoria que reutilizo na sugestão de compras
            self.box_categoria = customtkinter.CTkComboBox(self, **CONFIG_INPUTS1, values=list(categorias))
            self.box_categoria.set("Selecione a Categoria")
            self.box_categoria.pack()
            self.conferir_categorias = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#029B99", text="Conferir Categorias", command="")
            
        container_botoes = customtkinter.CTkFrame(self, fg_color="transparent")
        container_botoes.pack(side="top")

        #Botões
        self.limpar_categoria = customtkinter.CTkButton(container_botoes, **CONFIG_BOTOES, fg_color="#ECC039", text="Limpar", command=self.limpar_campos_view)
        self.limpar_categoria.pack(side="left", padx=20, pady=20)
        self.salvar_categoria = customtkinter.CTkButton(container_botoes, **CONFIG_BOTOES, fg_color="#90EE90", text="Cadastrar", command=self.salvar_dados_da_view)
        self.salvar_categoria.pack(side="left", padx=20, pady=20)

        #Visualização Categorias 000
        if self.conferir_categorias is not None:
                self.conferir_categorias.destroy()
                self.conferir_categorias = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#029B99", text="Conferir Categorias", command="")
                #self.conferir_categorias.pack()
        elif self.conferir_categorias is None:
            self.conferir_categorias = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#029B99", text="Conferir Categorias", command=categoriasExistentes)
            #self.conferir_categorias.pack()

    def salvar_dados_da_view(self):
        descricao_categoria = self.input_desc_categoria.get()
        self.controller.cadastrarCategoria(descricao_categoria)

    def limpar_campos_view(self):
        self.input_desc_categoria.delete(0, tk.END)
        self.input_desc_categoria.focus_set()
        os.system('cls')
        print("-- Terminal e demais campos limpos")

    def on_combobox_select(self, choice):
        print(f"V: Categoria selecionada: {choice}")


    '''def atualizar_combobox_categorias(self):
        categorias_do_db = self.controller.obter_categorias_para_view()
        if categorias_do_db:
            self.box_categoria.configure(values=categorias_do_db)
        else:
            self.box_categoria.configure(values=["Nenhuma Categoria"])
        self.box_categoria.set("Selecione a Categoria")'''