import customtkinter
from controller.cadastro_controller import controller_cadastro  # Importa a CLASSE do Controller
from view.cadastro_categorias_view import view_cadastro_categorias # Importa a CLASSE da View
import model.cadastro_model # Importa o módulo model para chamar as funções de criação do DB

if __name__ == "__main__":
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    # 1. Inicializa o banco de dados
    model.cadastro_model.BD_cad_categorias()
    model.cadastro_model.BD_cad_produtos()

    # 2. Instancia o Controller
    app_controller = controller_cadastro()

    # 3. Cria a janela principal
    app = view_cadastro_categorias(controller_instance=app_controller)
    app_controller.set_view(app)
    app.mainloop()

    # 5. Injeta a View no Controller
    #app_controller.set_view(app)

'''   -----------------   PALETA DE CORES   -----------------   '''
'''                                                             '''
'''   #001F21     #029B99      #EBE7B7    #DE4F15     #ECC039   '''
'''                                                             '''
'''   -------------------------------------------------------   '''