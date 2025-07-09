import customtkinter
from tkinter.filedialog import askopenfilename

from controller.controller import controller_cadastro
import tkinter as tk
from PIL import Image

class view_inicial(customtkinter.CTkFrame):
    def __init__(self, parent, controller_instance):
        super().__init__(parent)

        self.controller = controller_instance

        fundo = customtkinter.CTkFrame(master=self, fg_color="transparent")
        fundo.pack()

        logo_ssec = customtkinter.CTkImage(light_image=Image.open("logo_01.png"),
                                  dark_image=Image.open("logo_02.png"),
                                  size=(500, 180))
        logo = customtkinter.CTkLabel(self, image=logo_ssec, text="")
        logo.pack()