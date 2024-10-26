##############################
#  Fenêtre et widget tkinter #
#    des applications (GUI)  #
##############################

# -- Importations --
import tkinter as tk
import ttkbootstrap as ttk
from utility import GUI
from txteditor.app_operations import ouvrir_fichier, enregistrer_fichier, quitter_application


class TextEditor:
    """Application de texte éditeur"""

    def __init__(self, initial_text=""):
        """Initialisation de l'application"""
        self.root = GUI.set_basic_window("Text Editor")  # Fenêtre principale
        self.sidebar = ttk.Frame(self.root)              # Barre latérale pour les boutons
        self.textFrame = ttk.Frame(self.root)            # Cadre pour le texte
        self.main_text = ttk.Text(self.textFrame)             # Zone de texte 
        self.main_text.insert("1.0", initial_text)
        setattr(self.main_text, "path", "")
        
        toolbar = ttk.Menu(self.root)                    # Barre de menu
        self.root.config(menu=toolbar)
        self.menu = ttk.Menu(toolbar)                    # Menu
        toolbar.add_cascade(label="Fichier", menu=self.menu)
        
        
        # Positionnement des widgets
        self.main_text.pack(expand=True, fill="both")
        
        # Key binds & menu (toolbar)
        self.add_binds()

        # Boutons
        self.btn_open = ttk.Button(self.sidebar, text="Ouvrir", command=lambda: ouvrir_fichier(self.main_text)).pack(side="top", pady=5, padx=1, fill="x")
        self.btn_save = ttk.Button(self.sidebar, text="Enregistrer", command=lambda: enregistrer_fichier(self.main_text)).pack(side="top", pady=5, padx=1, fill="x")
        self.btn_quit = ttk.Button(self.sidebar, text="Quitter", command=lambda:quitter_application(self.root, self.main_text)).pack(side="top", pady=5, padx=1, fill="x")

        self.textFrame.pack(side="right", expand=True, fill="both")
        self.sidebar.pack(side="left", fill="y")

        self.root.mainloop()


    def add_binds(self):
        """Lancement de l'application"""
        
        self.menu.add_command(label="Ouvrir", command=lambda: ouvrir_fichier(self.main_text))
        self.menu.add_command(label="Enregistrer", command=lambda: enregistrer_fichier(self.main_text))
        self.menu.add_command(label="Quitter", command=lambda:quitter_application(self.root, self.main_text))
        self.menu.add_command(label="Enregistrer sous", command=lambda: enregistrer_fichier(self.main_text))

        self.root.bind("<Command-o>", lambda event: ouvrir_fichier(self.main_text))
        self.root.bind("<Command-s>", lambda event: enregistrer_fichier(self.main_text))
        self.root.bind("<Command-q>", lambda event: quitter_application(self.root, self.main_text))
        self.root.bind("<Command-S>", lambda event: enregistrer_fichier(self.main_text))
        self.root.bind("<Command-n>", lambda event: enregistrer_fichier(self.main_text, and_delete=True))

    def set_text(self, text: str, path=""):
        """Définir le texte d'un widget Text"""
        self.main_text.delete("1.0", tk.END)
        self.main_text.insert("1.0", text)
        setattr(self.main_text, "path", path)

    def get_text(self):
        """Obtenir le texte d'un widget Text"""
        return self.main_text.get("1.0", tk.END)



if __name__ == "__main__":
    # Tests
    app = TextEditor()