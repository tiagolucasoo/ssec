import customtkinter as ctk
import os

from tkinter import Menu
from tkinter import messagebox

from controller.controller import controller_cadastro
import model.model

from view.cad_categorias import view_cadastro_categorias
from view.cad_produtos import view_cadastro_produtos
from view.cad_vendas import view_importacao_manual
from view.sugestao_compras import view_sugestao
from view.imp_vendas import view_importacao_lote
from view.imp_produtos import view_importacao_produtos
from view.pag_inicial import view_inicial

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1024x768")
        self.minsize(1024,768)
        self.title("SSEC - Sistema de Sugestão Estratégica de Compras")

        os.system('cls')

        model.model.BD_cad_categorias()
        model.model.BD_cad_produtos()
        model.model.BD_cad_vendas()

        self.controller = controller_cadastro()
        self.controller.set_app(self)

        self.telas = {}

        container = ctk.CTkFrame(master=self, fg_color="transparent")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1) 
        container.grid_columnconfigure(0, weight=1)

        for tela in (view_cadastro_categorias, view_cadastro_produtos, view_importacao_manual, view_importacao_lote, view_sugestao, view_importacao_produtos, view_inicial):
            nome = tela.__name__
            frame = tela(parent=container, controller_instance=self.controller)
            self.telas[nome] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.exibir_tela("view_inicial")
        self.criar_menu()

    def criar_menu(self):
        barra_menu = Menu(self)
        menu_1 = Menu(barra_menu, tearoff=0)
        menu_1.add_command(label="Página Inicial", command=lambda: self.exibir_tela("view_inicial"))
        menu_1.add_separator()
        menu_1.add_command(label="Sair", command=self.quit)
        barra_menu.add_cascade(label="Página Inicial", menu=menu_1)

        menu_2 = Menu(barra_menu, tearoff=0)
        menu_2.add_command(label="Produtos", command=lambda: self.exibir_tela("view_cadastro_produtos"))
        menu_2.add_command(label="Categorias", command=lambda: self.exibir_tela("view_cadastro_categorias"))
        menu_2.add_command(label="Vendas", command=lambda: self.exibir_tela("view_importacao_manual"))
        barra_menu.add_cascade(label="Cadastro", menu=menu_2)

        menu_3 = Menu(barra_menu, tearoff=0)
        menu_3.add_command(label="Produtos em lote", command=lambda: self.exibir_tela("view_importacao_produtos"))
        menu_3.add_command(label="Relatório de Vendas", command=lambda: self.exibir_tela("view_importacao_lote"))
        barra_menu.add_cascade(label="Importar", menu=menu_3)

        menu_4 = Menu(barra_menu, tearoff=0)
        menu_4.add_command(label="Sugestão de Compras", command=lambda: self.exibir_tela("view_sugestao"))
        barra_menu.add_cascade(label="Compras", menu=menu_4)

        menu_5 = Menu(barra_menu, tearoff=0)
        menu_5.add_command(label="Modo Escuro", command=lambda: ctk.set_appearance_mode("dark"))
        menu_5.add_command(label="Modo Claro", command=lambda: ctk.set_appearance_mode("system"))
        barra_menu.add_cascade(label="Aparência", menu=menu_5)

        self.configure(menu=barra_menu)

    def exibir_tela(self, nome_tela):
        frame = self.telas[nome_tela]
        frame.tkraise()
    
    def exibir_mensagem_sucesso(self, mensagem):
        messagebox.showinfo("Sucesso", mensagem, parent=self)

    def exibir_mensagem_erro(self, mensagem):
        messagebox.showerror("Erro", mensagem, parent=self)

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    app = App()
    app.mainloop()