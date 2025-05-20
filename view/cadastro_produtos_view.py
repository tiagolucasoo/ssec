import customtkinter
'''
Código Produto - Código de Barras
Descrição do Produto
Marca - Categoria[]
Custo - Marcação - Venda
'''

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.title("SSEC - Cadastro de Produtos")

        #Código do Produto
        label = customtkinter.CTkLabel(self, text="Código", fg_color="transparent")
        label.pack()
        entry = customtkinter.CTkEntry(self, placeholder_text="Exemplo: 1010")
        entry.pack()

        #Código de Barras
        label2 = customtkinter.CTkLabel(self, text="Código de Barras", fg_color="transparent")
        label2.pack()
        entry2 = customtkinter.CTkEntry(self, placeholder_text="Exemplo: 7896051020127")
        entry2.pack()

        #Descrição do Produto
        label3 = customtkinter.CTkLabel(self, text="Descrição do Produto", fg_color="transparent")
        label3.pack()
        entry3 = customtkinter.CTkEntry(self, placeholder_text="Exemplo: Energético Furioso 300ml Tradicional")
        entry3.pack()

        #Marca
        label4 = customtkinter.CTkLabel(self, text="Marca", fg_color="transparent")
        label4.pack()
        entry4 = customtkinter.CTkEntry(self, placeholder_text="Value")
        entry4.pack()

        radiobutton_1 = customtkinter.CTkRadioButton(self, text="CTkRadioButton 1", command="", value=1)
        radiobutton_1.pack()
        radiobutton_2 = customtkinter.CTkRadioButton(self, text="CTkRadioButton 2", command="", value=2)
        radiobutton_2.pack()

        button = customtkinter.CTkButton(self, fg_color="red", text="Limpar")
        button.pack()

        button = customtkinter.CTkButton(self, fg_color="green", text="Cadastrar")
        button.pack()
app = App()
app.mainloop()