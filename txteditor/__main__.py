##############################
#  Application texte éditeur #
##############################


# -- Importations --
import ttkbootstrap as ttk
from utility import GUI
from functions import demarrer_application

# -- Programme --
window = GUI.set_basic_window("Text Editor")
main_text = ttk.Text(root)
setattr(main_text, "path", "")

demarrer_application(window, main_text)