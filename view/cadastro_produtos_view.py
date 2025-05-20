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

        button = customtkinter.CTkButton(self, fg_color="red", text="Limpar")
        button.pack()

        button = customtkinter.CTkButton(self, fg_color="green", text="Cadastrar")
        button.pack()
app = App()
app.mainloop()