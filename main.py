import customtkinter
from controller.cadastro_controller import controller_cadastro  # Importa a CLASSE do Controller
from view.cadastro_categorias_view import view_cadastro_categorias # Importa a CLASSE da View
import model.cadastro_model # Importa o módulo model para chamar as funções de criação do DB

if __name__ == "__main__":
    # Configurações iniciais do CustomTkinter
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue") # Ou sua cor padrão: #EBE7B7

    # 1. Inicializa as tabelas do banco de dados (chama as funções do Model)
    # Certifique-se de que o caminho '../banco.db' nos modelos está correto em relação à raiz do seu projeto.
    # Se 'banco.db' estiver na mesma pasta que 'main.py' e as pastas 'model', 'view', 'controller',
    # o caminho nos models deveria ser './banco.db'
    model.cadastro_model.BD_cad_categorias()
    model.cadastro_model.BD_cad_produtos()

    # 2. Instancia o Controller
    # O Controller NÃO precisa de um model_instance aqui se suas funções de Model forem soltas no módulo.
    app_controller = controller_cadastro()

    # 3. Cria a janela principal do CustomTkinter (root)
    app = view_cadastro_categorias(controller_instance=app_controller)
    app_controller.set_view(app)
    app.mainloop()

    #root.geometry("1000x800")
    #root.title("SSEC - Sistema de Gestão")

    # 4. Instancia a View, PASSANDO A INSTÂNCIA DO CONSTROLLER E O MASTER (root)
    # A View espera 'master' como primeiro argumento agora.


    # 5. Injeta a View no Controller (se o Controller precisar de uma referência de volta à View)
    app_controller.set_view(app)

'''
PALETA DE CORES - SSEC
#001F21
#029B99
#EBE7B7
#DE4F15
#ECC039
'''