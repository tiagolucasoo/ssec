import customtkinter as ctk
from tkinter import Menu
from tkinter import messagebox

from controller.controller import controller_cadastro
import model.model

from view.cad_categorias import view_cadastro_categorias
from view.cad_produtos import view_cadastro_produtos
from view.cad_vendas import view_importacao_manual
from view.sugestao_compras import view_sugestao
from view.imp_vendas import view_importacao_lote

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x800")
        self.title("SSEC - Sistema de Sugestão Estratégica de Compras")

        model.model.BD_cad_categorias()
        model.model.BD_cad_produtos()
        model.model.BD_cad_vendas()

        self.controller = controller_cadastro()
        self.telas = {}

        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        for tela in (view_cadastro_categorias, view_cadastro_produtos, view_importacao_manual, view_importacao_lote, view_sugestao):
            nome = tela.__name__
            frame = tela(parent=container, controller_instance=self.controller)
            self.telas[nome] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.exibir_tela("view_cadastro_categorias")
        self.criar_menu()

    def criar_menu(self):
        barra_menu = Menu(self)
        menu_1 = Menu(barra_menu, tearoff=0)
        menu_1.add_command(label="Página Inicial", command=lambda: self.exibir_tela("view_sugestao"))
        menu_1.add_separator()
        menu_1.add_command(label="Sair", command=self.quit)
        barra_menu.add_cascade(label="Página Inicial", menu=menu_1)

        menu_2 = Menu(barra_menu, tearoff=0)
        menu_2.add_command(label="Produtos", command=lambda: self.exibir_tela("view_cadastro_produtos"))
        menu_2.add_command(label="Categorias", command=lambda: self.exibir_tela("view_cadastro_categorias"))
        menu_2.add_command(label="Vendas", command=lambda: self.exibir_tela("view_importacao_manual"))
        barra_menu.add_cascade(label="Cadastro", menu=menu_2)

        menu_3 = Menu(barra_menu, tearoff=0)
        menu_3.add_command(label="Produtos em lote", command=lambda: self.exibir_tela("view_sugestao"))
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
        messagebox.showinfo("Sucesso", mensagem)

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    app = App()
    app.mainloop()