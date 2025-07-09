import customtkinter
import tkinter as tk
from controller.controller import controller_cadastro

class view_importacao_manual(customtkinter.CTkFrame):
    def __init__(self, parent, controller_instance):
        super().__init__(parent)

        self.controller = controller_instance
        
        CONFIG_BOTOES = {"width":200, "height":50, "border_width":2, "border_color":'#000', "text_color":'#001F21'}
        #CONFIG_INPUTS1 = {"width":600, "height":50, "border_width":0} #Para 1 por Linha
        CONFIG_INPUTS2 = {"width":275, "height":50, "border_width":0} #Para 2 por Linha

        #Código
        label2 = customtkinter.CTkLabel(self, text="Código do Produto", fg_color="transparent")
        label2.pack()
        self.codigo_produto = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Digite aqui o valor")
        self.codigo_produto.pack()

        #Quantidade
        label4 = customtkinter.CTkLabel(self, text="Quantidade Vendida", fg_color="transparent")
        label4.pack()
        self.quantidade_vendida = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Exemplo: 30")
        self.quantidade_vendida.pack()

        #Período
        label3 = customtkinter.CTkLabel(self, text="Período de venda (Dias)", fg_color="transparent")
        label3.pack()
        self.periodo_vendas = customtkinter.CTkEntry(self, **CONFIG_INPUTS2, placeholder_text="Exemplo: 30")
        self.periodo_vendas.pack()

        #Botões
        container_botoes = customtkinter.CTkFrame(self, fg_color="transparent")
        container_botoes.pack(side="top")
        button1 = customtkinter.CTkButton(container_botoes, **CONFIG_BOTOES, fg_color="#ECC039", text="Limpar", command=self.limpar_dados)
        button1.pack(side="left", padx=20, pady=20)
        button2 = customtkinter.CTkButton(container_botoes, **CONFIG_BOTOES, fg_color="#DE4F15", text="Salvar", command=self.salvar_dados)
        button2.pack(side="left", padx=20, pady=20)

    def salvar_dados(self):
            try:
                codigo_produto = int(self.codigo_produto.get())
                quantidade_vendida = int(self.quantidade_vendida.get())
                periodo_vendas = int(self.periodo_vendas.get())

                self.controller.cadastrarVenda(codigo_produto, quantidade_vendida, periodo_vendas)
            except ValueError:
                self.exibir_mensagem_erro("Confira os dados digitados e tente novamente!")
            except Exception as e:
                self.exibir_mensagem_erro(f"Erro ao salvar produto: {e}")
    def limpar_dados(self):
        self.codigo_produto.delete(0, tk.END)
        self.quantidade_vendida.delete(0, tk.END)
        self.periodo_vendas.delete(0, tk.END)