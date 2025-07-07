import customtkinter
import tkinter as tk

from controller.controller import controller_cadastro

class view_sugestao(customtkinter.CTkFrame):
    def __init__(self, parent, controller_instance):
        super().__init__(parent)

        self.controller = controller_instance
        self.controller.set_view(self)

        CONFIG_BOTOES = {"width":200, "height":50, "border_width":2, "border_color":'#000', "text_color":'#001F21'}
        CONFIG_INPUTS1 = {"width":600, "height":50, "border_width":0} #Para 1 por Linha
        CONFIG_INPUTS2 = {"width":275, "height":50, "border_width":0} #Para 2 por Linha
        
        # Categoria
        self.label_categoria = customtkinter.CTkLabel(self, text="Categoria", fg_color="transparent")
        self.label_categoria.pack()

        self.box_categoria = customtkinter.CTkComboBox(self,width=275,height=50,border_width=0,values=self.controller.listarCategorias(),command=self.on_combobox_select)
        self.box_categoria.pack()

        label5 = customtkinter.CTkLabel(self, text="Categoria", fg_color="transparent")
        label5.pack(side="top", pady=20)

        #Curva
        label6 = customtkinter.CTkLabel(self, text="Curva de Vendas", fg_color="transparent")
        label6.pack(side="top", pady=20)

        container_radio = customtkinter.CTkFrame(self, fg_color="transparent")
        container_radio.pack(side="top")
        self.radio_var_curva = customtkinter.Variable(value=0)

        radiobutton_0 = customtkinter.CTkRadioButton(container_radio, text="Todos", variable=self.radio_var_curva, value=0)
        radiobutton_0.pack(side="left", padx=10, pady=20)
        radiobutton_1 = customtkinter.CTkRadioButton(container_radio, text="Curva A", variable=self.radio_var_curva, value=1)
        radiobutton_1.pack(side="left", padx=10, pady=20)
        radiobutton_2 = customtkinter.CTkRadioButton(container_radio, text="Curva B", variable=self.radio_var_curva, value=2)
        radiobutton_2.pack(side="left", padx=10, pady=20)
        radiobutton_3 = customtkinter.CTkRadioButton(container_radio, text="Curva C", variable=self.radio_var_curva, value=3)
        radiobutton_3.pack(side="left", padx=10, pady=20)
        radiobutton_4 = customtkinter.CTkRadioButton(container_radio, text="Lançamento", variable=self.radio_var_curva, value=4)
        radiobutton_4.pack(side="left", padx=10, pady=20)
        radiobutton_5 = customtkinter.CTkRadioButton(container_radio, text="Exclusivo", variable=self.radio_var_curva, value=5)
        radiobutton_5.pack(side="left", padx=10, pady=20)

        # PERÍODO
        label7 = customtkinter.CTkLabel(self, text="Período para reposição", fg_color="transparent")
        label7.pack(side="top", pady=20)

        container_radio1 = customtkinter.CTkFrame(self, fg_color="transparent")
        container_radio2 = customtkinter.CTkFrame(self, fg_color="transparent")
        container_radio1.pack(side="top")
        self.radio_var_periodo = customtkinter.Variable(value=0)
        
        radiobutton_10 = customtkinter.CTkRadioButton(container_radio1, text="15 Dias", variable=self.radio_var_periodo, value=15)
        radiobutton_10.pack(side="left", padx=10, pady=20)
        radiobutton_11 = customtkinter.CTkRadioButton(container_radio1, text="30 Dias", variable=self.radio_var_periodo, value=30)
        radiobutton_11.pack(side="left", padx=10, pady=20)
        radiobutton_12 = customtkinter.CTkRadioButton(container_radio1, text="45 Dias", variable=self.radio_var_periodo, value=45)
        radiobutton_12.pack(side="left", padx=10, pady=20)
        radiobutton_13 = customtkinter.CTkRadioButton(container_radio1, text="60 Dias", variable=self.radio_var_periodo, value=60)
        radiobutton_13.pack(side="left", padx=10, pady=20)
        radiobutton_14 = customtkinter.CTkRadioButton(container_radio1, text="75 Dias", variable=self.radio_var_periodo, value=75)
        radiobutton_14.pack(side="left", padx=10, pady=20)
        radiobutton_15 = customtkinter.CTkRadioButton(container_radio1, text="90 Dias", variable=self.radio_var_periodo, value=90)
        radiobutton_15.pack(side="left", padx=10, pady=20)

        #Botões
        container_radio2.pack(side="top")
        gerar = customtkinter.CTkButton(container_radio2, text="Gerar Sugestão", command=self.gerar_sugestao)
        gerar.pack(side="left", padx=20)

        limpar = customtkinter.CTkButton(container_radio2, text="Limpar Dados")
        limpar.pack(side="left", padx=20)

        self.frame_resultados = customtkinter.CTkScrollableFrame(self, label_text="Sugestões de Compra")
        self.frame_resultados.pack(fill="both", expand=True, padx=20, pady=20)

    def exibir_resultados(self, sugestoes):
            for widget in self.frame_resultados.winfo_children():
                widget.destroy()

            #Cabecalho
            cabecalho = ["Cód", "Descrição", "Categoria", "Custo", "Venda", "Qtde Sugerida", "Custo Total", "Venda Total"]
            for i, texto_linha0 in enumerate(cabecalho):
                label = customtkinter.CTkLabel(self.frame_resultados, text=texto_linha0, font=("", 12, "bold"))
                label.grid(row=0, column=i, padx=10, pady=5)

            for linha, sugestao in enumerate(sugestoes, start=1):
                for coluna, valor in enumerate(sugestao):
                    label = customtkinter.CTkLabel(self.frame_resultados, text=str(valor))
                    label.grid(row=linha, column=coluna, padx=10, pady=2)
    
    def on_combobox_select(self, choice):
        print(f"View: Categoria selecionada: {choice}")

    def gerar_sugestao(self):
        categoria_selecionada = self.box_categoria.get()
        curva_selecionada = self.radio_var_curva.get()
        periodo_selecionado = self.radio_var_periodo.get()

        lista_de_sugestoes = self.controller.obter_sugestao_de_compra(
            categoria_selecionada, curva_selecionada, periodo_selecionado)

        self.exibir_resultados(lista_de_sugestoes)