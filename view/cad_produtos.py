import customtkinter
from controller.controller import controller_cadastro
import tkinter as tk

class view_cadastro_produtos(customtkinter.CTkFrame):
    def __init__(self, parent, controller_instance):
        super().__init__(parent)
        
        self.controller = controller_instance

        CONFIG_BOTOES = {"width":200, "height":50, "border_width":2, "border_color":'#000', "text_color":'#001F21'}
        CONFIG_INPUTS1 = {"width":600, "height":50, "border_width":0} #Para 1 por Linha
        CONFIG_INPUTS2 = {"width":275, "height":50, "border_width":0} #Para 2 por Linha

        #Código
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
        self.input_marca = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="")
        self.input_marca.pack()

        # Categoria
        self.label_categoria = customtkinter.CTkLabel(self, text="Categoria", fg_color="transparent")
        self.label_categoria.pack()

        self.box_categoria = customtkinter.CTkComboBox(self,width=275,height=50,border_width=0,values=self.controller.listarCategorias(),command=self.on_combobox_select)
        self.box_categoria.pack()
        self.atualizar_combobox_categorias()

        # Custo e Venda
        self.label_custo = customtkinter.CTkLabel(self, text="Custo (R$)", fg_color="transparent")
        self.label_custo.pack()
        self.input_custo = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Exemplo: 5.50")
        self.input_custo.pack()

        self.label_venda = customtkinter.CTkLabel(self, text="Venda (R$)", fg_color="transparent")
        self.label_venda.pack()
        self.input_venda = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Exemplo: 9.90")
        self.input_venda.pack()

        #Curva do Produto
        container_radio1 = customtkinter.CTkFrame(self, fg_color="transparent")
        container_radio1.pack(side="top")
        label6 = customtkinter.CTkLabel(self, text="Tipo de Produto", fg_color="transparent")
        label6.pack()
        self.radio_var = customtkinter.Variable(value=0)
        radiobutton_1 = customtkinter.CTkRadioButton(container_radio1, text="Curva A", variable=self.radio_var, value=1)
        radiobutton_1.pack(side="left", pady=20)
        radiobutton_2 = customtkinter.CTkRadioButton(container_radio1, text="Curva B", variable=self.radio_var, value=2)
        radiobutton_2.pack(side="left")
        radiobutton_3 = customtkinter.CTkRadioButton(container_radio1, text="Curva C", variable=self.radio_var, value=3)
        radiobutton_3.pack(side="left")
        radiobutton_4 = customtkinter.CTkRadioButton(container_radio1, text="Lançamento", variable=self.radio_var, value=4)
        radiobutton_4.pack(side="left")
        radiobutton_5 = customtkinter.CTkRadioButton(container_radio1, text="Exclusivo", variable=self.radio_var, value=5)
        radiobutton_5.pack(side="left")

        #Botões
        container_botoes = customtkinter.CTkFrame(self, fg_color="transparent")
        container_botoes.pack(side="top")
        button1 = customtkinter.CTkButton(container_botoes, **CONFIG_BOTOES, fg_color="#ECC039", text="Limpar", command=self.limpar_campos_view)
        button1.pack(side="left", padx=20, pady=20)
        button2 = customtkinter.CTkButton(container_botoes, **CONFIG_BOTOES, fg_color="#DE4F15", text="Cadastrar", command=self.salvar_dados_da_view)
        button2.pack(side="left", padx=20, pady=20)

    def salvar_dados_da_view(self):
        try:
            codigobarras = int(self.input_codigobarras.get())
            descricao_produto = self.input_descricao_produto.get()
            marca = self.input_marca.get()
            categoria = self.box_categoria.get()
            custo = float(self.input_custo.get().replace(',', '.'))
            venda = float(self.input_venda.get().replace(',', '.'))
            curva = int(self.radio_var.get())

            self.controller.cadastrarProduto(codigobarras, descricao_produto, marca, categoria, custo, venda, curva)
        except ValueError:
            print("View (Erro) - cad_produtos.py")
        except Exception as e:
            print(f"View (Erro): {e}")
    
    def limpar_campos_view(self):
        self.entry.delete(0, tk.END)
        self.input_codigobarras.delete(0, tk.END)
        self.input_descricao_produto.delete(0, tk.END)
        self.input_marca.delete(0, tk.END)
        self.input_custo.delete(0, tk.END)
        self.input_venda.delete(0, tk.END)
        self.box_categoria.set("Selecione a Categoria")
        self.radio_var.set(0)
        self.entry.focus_set()
        print("V: Campos de entrada limpos.")
    
    def on_combobox_select(self, choice):
        print(f"V: Categoria selecionada: {choice}")

    def atualizar_combobox_categorias(self):
        categorias = self.controller.listarCategorias()
        self.box_categoria.configure(values=categorias)
        if categorias:
            self.box_categoria.set("Selecione a Categoria")