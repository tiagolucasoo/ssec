import customtkinter
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

        CONFIG_BOTOES = {"width":200, "height":50, "border_width":2, "border_color":'#000', "text_color":'#001F21'}
        CONFIG_INPUTS1 = {"width":600, "height":50, "border_width":0} #Para 1 por Linha
        CONFIG_INPUTS2 = {"width":275, "height":50, "border_width":0} #Para 2 por Linha

        #Código da Categoria
        label = customtkinter.CTkLabel(self, text="Código", fg_color="transparent")
        label.pack()
        entry = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Exemplo: 1010")
        entry.pack()

        #Código de Barras
        label2 = customtkinter.CTkLabel(self, text="Código de Barras", fg_color="transparent")
        label2.pack()
        entry2 = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Exemplo: 7896051020127")
        entry2.pack()

        #Descrição do Produto
        label3 = customtkinter.CTkLabel(self, text="Descrição do Produto", fg_color="transparent")
        label3.pack()
        entry3 = customtkinter.CTkEntry(self, **CONFIG_INPUTS1, placeholder_text="Exemplo: Energético Furioso 300ml Tradicional")
        entry3.pack()

        #Marca
        label4 = customtkinter.CTkLabel(self, text="Marca", fg_color="transparent")
        label4.pack()
        entry4 = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Value")
        entry4.pack()

        #Categoria
        categorias = ("teste", "teste")
        label5 = customtkinter.CTkLabel(self, text="Categoria", fg_color="transparent")
        label5.pack()
        #Fazer uma função para esse check de categoria que reutilizo na sugestão de compras
        combobox = customtkinter.CTkComboBox(self, **CONFIG_INPUTS2, values=list(categorias),
                                     command='')
        combobox.set("Selecione a Categoria")
        combobox.pack()

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

        button = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#ECC039", text="Limpar")
        button.pack()

        button = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#DE4F15", text="Cadastrar")
        button.pack()

open = view_cadastro_produtos()
open.mainloop()