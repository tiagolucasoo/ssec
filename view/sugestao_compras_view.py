import customtkinter
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
        self.title("SSEC - Sugestão de Compras")

        CONFIG_BOTOES = {"width":200, "height":50, "border_width":2, "border_color":'#000', "text_color":'#001F21'}
        CONFIG_INPUTS1 = {"width":600, "height":50, "border_width":0} #Para 1 por Linha
        CONFIG_INPUTS2 = {"width":275, "height":50, "border_width":0} #Para 2 por Linha
        #Categoria
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