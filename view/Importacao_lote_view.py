import customtkinter
from tkinter.filedialog import askopenfilename
'''
Código Produto - Código de Barras
Descrição do Produto
Marca - Categoria[]
Custo - Marcação - Venda
'''

class view_importacao_lote(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x800")
        self.title("SSEC - Importação Manual")

        CONFIG_BOTOES = {"width":200, "height":50, "border_width":2, "border_color":'#000', "text_color":'#001F21'}
        #CONFIG_INPUTS1 = {"width":600, "height":50, "border_width":0} #Para 1 por Linha
        CONFIG_INPUTS2 = {"width":275, "height":50, "border_width":0} #Para 2 por Linha

        def selecionar():
            caminho_arquivo = askopenfilename()
            return caminho_arquivo


        abrirtela = customtkinter.CTkButton(self, **CONFIG_BOTOES, text="teste", command=selecionar)
        abrirtela.pack()

        #Código de Barras
        label2 = customtkinter.CTkLabel(self, text="Código do Produto", fg_color="transparent")
        label2.pack()
        entry2 = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Digite aqui o valor")
        entry2.pack()

        #Categoria
        categorias = ("teste", "teste")
        label5 = customtkinter.CTkLabel(self, text="Categoria", fg_color="transparent")
        label5.pack()
        #Fazer uma função para esse check de categoria que reutilizo na sugestão de compras
        combobox = customtkinter.CTkComboBox(self, **CONFIG_INPUTS2, values=list(categorias),
                                     command='')
        combobox.set("Selecione a Categoria")
        combobox.pack()

        #Descrição do Produto
        label3 = customtkinter.CTkLabel(self, text="Período de venda (Dias)", fg_color="transparent")
        label3.pack()
        entry3 = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Exemplo: 30")
        entry3.pack()

        button = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#ECC039", text="Limpar")
        button.pack()

        button = customtkinter.CTkButton(self, **CONFIG_BOTOES, fg_color="#DE4F15", text="Salvar")
        button.pack()

open = view_importacao_lote()
open.mainloop()