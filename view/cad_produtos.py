import customtkinter
from controller.controller import controller_cadastro
import tkinter as tk
import os

class view_cadastro_produtos(customtkinter.CTkFrame):
    def __init__(self, parent, controller_instance):
        super().__init__(parent)
        
        self.controller = controller_instance

        # Rodapé
        info_ssec = customtkinter.CTkLabel(self, text="SSEC - Versão 1.0 | Desenvolvido por Tiago Lucas (GitHub: Tiagolucasoo)", fg_color="transparent")
        info_ssec.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)
        
        CONFIG_BOTOES = {"width":200, "height":50, "text_color":'#001F21'}
        CONFIG_INPUTS1 = {"width":600, "height":50, "border_width":0} #Para 1 por Linha
        CONFIG_INPUTS2 = {"width":275, "height":50, "border_width":0} #Para 2 por Linha

        #CONTAINER ----- CÓDIGO E CÓDIGO DE BARRAS
        container_codigos = customtkinter.CTkFrame(self, fg_color="transparent")
        container_codigos.pack(side="top", padx=20, pady=20)  

        container_cod = customtkinter.CTkFrame(container_codigos, fg_color="transparent")
        container_cod.pack(side="left", padx=20)  
        self.label = customtkinter.CTkLabel(container_cod, text="Código", fg_color="transparent")
        self.label.pack(side="top", padx=20)
        self.input_codigo = customtkinter.CTkEntry(container_cod, **CONFIG_INPUTS2, placeholder_text="Exemplo: 1010")
        self.input_codigo.pack(side="top", pady=10)

        container_barras = customtkinter.CTkFrame(container_codigos, fg_color="transparent")
        container_barras.pack(side="right", padx=20) 
        self.label2 = customtkinter.CTkLabel(container_barras, text="Código de Barras", fg_color="transparent")
        self.label2.pack(side="top", padx=20)
        self.input_codigobarras = customtkinter.CTkEntry(container_barras, **CONFIG_INPUTS2, placeholder_text="Exemplo: 7896051020127")
        self.input_codigobarras.pack(side="top", pady=10)

        #Descrição do Produto
        self.label3 = customtkinter.CTkLabel(self, text="Descrição do Produto", fg_color="transparent")
        self.label3.pack()
        self.input_descricao_produto = customtkinter.CTkEntry(self, **CONFIG_INPUTS1, placeholder_text="Exemplo: Energético Furioso 300ml Tradicional")
        self.input_descricao_produto.pack(pady=10)

        # CONTAINER ----- MARCA & CATEGORIA
        container_marca_categoria = customtkinter.CTkFrame(self, fg_color="transparent")
        container_marca_categoria.pack(side="top", padx=20)  

        container_marca = customtkinter.CTkFrame(container_marca_categoria, fg_color="transparent")
        container_marca.pack(side="left", padx=20)  
        self.label4 = customtkinter.CTkLabel(container_marca, text="Marca", fg_color="transparent")
        self.label4.pack(side="top", padx=20)
        self.input_marca = customtkinter.CTkEntry(container_marca, **CONFIG_INPUTS2, placeholder_text="")
        self.input_marca.pack(side="top", pady=10)

        container_categoria = customtkinter.CTkFrame(container_marca_categoria, fg_color="transparent")
        container_categoria.pack(side="right", padx=20)
        self.label_categoria = customtkinter.CTkLabel(container_categoria, text="Categoria", fg_color="transparent")
        self.label_categoria.pack(side="top", padx=20)
        self.box_categoria = customtkinter.CTkComboBox(container_categoria,width=275,height=50,border_width=0,values=self.controller.listarCategorias(),command=self.on_combobox_select)
        self.box_categoria.pack(side="top", pady=10)
        self.atualizar_combobox_categorias()
        
        # CONTAINER ----- CUSTO & VALOR
        container_valor = customtkinter.CTkFrame(self, fg_color="transparent")
        container_valor.pack(side="top", padx=20)  
        
        container_custo = customtkinter.CTkFrame(container_valor, fg_color="transparent")
        container_custo.pack(side="left", padx=20)
        self.label_custo = customtkinter.CTkLabel(container_custo, text="Custo (R$)", fg_color="transparent")
        self.label_custo.pack(side="top", padx=20)
        self.input_custo = customtkinter.CTkEntry(container_custo, **CONFIG_INPUTS2, placeholder_text="Exemplo: 5.50")
        self.input_custo.pack(side="top", pady=10)

        container_venda = customtkinter.CTkFrame(container_valor, fg_color="transparent")
        container_venda.pack(side="right", padx=20)
        self.label_venda = customtkinter.CTkLabel(container_venda, text="Venda (R$)", fg_color="transparent")
        self.label_venda.pack(side="top", padx=20)
        self.input_venda = customtkinter.CTkEntry(container_venda, **CONFIG_INPUTS2, placeholder_text="Exemplo: 9.90")
        self.input_venda.pack(side="top", pady=10)

        #Curva do Produto
        container_radio0 = customtkinter.CTkFrame(self, fg_color="transparent")
        container_radio0.pack(side="top", pady=10)
        container_radio1 = customtkinter.CTkFrame(self, fg_color="transparent")
        container_radio1.pack(side="top")

        label6 = customtkinter.CTkLabel(container_radio0, text="Tipo de Produto", fg_color="transparent")
        label6.pack()
        self.radio_var = customtkinter.Variable(value=0)
        radiobutton_1 = customtkinter.CTkRadioButton(container_radio1, text="Curva A", variable=self.radio_var, value=1)
        radiobutton_1.pack(side="left", padx=20)
        radiobutton_2 = customtkinter.CTkRadioButton(container_radio1, text="Curva B", variable=self.radio_var, value=2)
        radiobutton_2.pack(side="left", padx=20)
        radiobutton_3 = customtkinter.CTkRadioButton(container_radio1, text="Curva C", variable=self.radio_var, value=3)
        radiobutton_3.pack(side="left", padx=20)
        radiobutton_4 = customtkinter.CTkRadioButton(container_radio1, text="Lançamento", variable=self.radio_var, value=4)
        radiobutton_4.pack(side="left", padx=20)
        radiobutton_5 = customtkinter.CTkRadioButton(container_radio1, text="Exclusivo", variable=self.radio_var, value=5)
        radiobutton_5.pack(side="left", padx=20)

        #Botões
        container_botoes = customtkinter.CTkFrame(self, fg_color="transparent")
        container_botoes.pack(side="top")
        button1 = customtkinter.CTkButton(container_botoes, **CONFIG_BOTOES, fg_color="#ffc107", hover_color="#e0a800", text="Limpar Campos", command=self.limpar_campos_view)
        button1.pack(side="left", padx=20, pady=30)
        button2 = customtkinter.CTkButton(container_botoes, **CONFIG_BOTOES, fg_color="#28a745", hover_color="#218838", text="Cadastrar Produto", command=self.salvar_dados_da_view)
        button2.pack(side="left", padx=20, pady=30)

    def salvar_dados_da_view(self):
        try:
            codigo_produto = self.input_codigo.get()
            codigobarras = self.input_codigobarras.get()
            descricao_produto = self.input_descricao_produto.get()
            marca = self.input_marca.get()
            categoria = self.box_categoria.get()
            custo = self.input_custo.get()
            venda = self.input_venda.get()
            curva = self.radio_var.get()

            self.controller.cadastrarProduto(codigo_produto, codigobarras, descricao_produto, marca, categoria, custo, venda, curva)
        except ValueError as v:
            print(f"View (Erro) - cad_produtos.py: {v}")
        except Exception as e:
            print(f"View (Erro): {e}")
    
    def limpar_campos_view(self):
        self.input_codigo.delete(0, tk.END)
        self.input_codigobarras.delete(0, tk.END)
        self.input_descricao_produto.delete(0, tk.END)
        self.input_marca.delete(0, tk.END)
        self.input_custo.delete(0, tk.END)
        self.input_venda.delete(0, tk.END)
        self.box_categoria.set("Selecione a Categoria")
        self.radio_var.set(0)
        self.input_codigo.focus_set()
        os.system('cls')
        print("-- Terminal e demais campos limpos")
    
    def on_combobox_select(self, choice):
        print(f"V: Categoria selecionada: {choice}")

    def atualizar_combobox_categorias(self):
        categorias = self.controller.listarCategorias()
        self.box_categoria.configure(values=categorias)
        if categorias:
            self.box_categoria.set("Selecione a Categoria")