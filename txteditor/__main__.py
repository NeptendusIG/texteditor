##############################
#  Application texte éditeur #
##############################


# -- Importations --
import ttkbootstrap as ttk
from utility import GUI
from txteditor.app import TextEditor

from txteditor import logger
# -- Programme --
# root = GUI.set_basic_window("Text Editor")
# main_text = ttk.Text(root)
# setattr(main_text, "path", "")

logger.info("Starting the application")
TextEditor()
logger.info("Application closed")