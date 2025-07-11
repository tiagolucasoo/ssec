import customtkinter
from tkinter.filedialog import askopenfilename

from controller.controller import controller_cadastro
import tkinter as tk
from PIL import Image
import datetime

class view_inicial(customtkinter.CTkFrame):
    def __init__(self, parent, controller_instance):
        super().__init__(parent)

        self.controller = controller_instance

        fundo = customtkinter.CTkFrame(master=self, fg_color="transparent")
        fundo.pack()

        logo_ssec = customtkinter.CTkImage(light_image=Image.open("img/logo_light.png"),
                                  dark_image=Image.open("img/logo_dark.png"),
                                  size=(500, 180))
        logo = customtkinter.CTkLabel(self, image=logo_ssec, text="")
        logo.pack()

        # Rodapé
        info_ssec = customtkinter.CTkLabel(self, text="SSEC - Versão 1.0 | Desenvolvido por Tiago Lucas (GitHub: Tiagolucasoo)", fg_color="transparent")
        info_ssec.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

        self.info_hora = customtkinter.CTkLabel(self, text="", fg_color="transparent")
        self.info_hora.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

        self.atualizar_data()

    def atualizar_data(self):
        agora = datetime.datetime.now().strftime("%d/%m/%Y  -  %H:%M:%S")
        self.info_hora.configure(text=agora)
        self.after(1000, self.atualizar_data)