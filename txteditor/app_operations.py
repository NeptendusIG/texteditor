#####################################
#          Titre - Date             #
#####################################
# NOTES :
"""
L'application va se construire autour d'une variable contenant l'entièreté du texte.
-> Donc il ne peut pas y avoir plus d'une fenêtre ouverte à la fois. (sauf pls runtime)
"""
# -- IMPORTS --
# Modules
from utility import GUI
from tkinter import filedialog
import tkinter as tk
import ttkbootstrap as ttk
# Classes
# -- FONCTIONS DÉFINIES --
def ouvrir_fichier(text_widger):
    """Ouvrir un fichier"""
    if len(text_widger.get("1.0", tk.END))>5:
        if GUI.ask_yes_no("Le text en cour sera écrasé.", "Voulez-vous enregistrer le fichier avant d'ouvrir un autre?"):
            enregistrer_fichier(text_widger)
    file_path = GUI.ask_file(context="Choisissez un fichier", types=[("Fichiers texte", "*.txt"), ("Fichiers csv", "*.csv")])
    with open(file_path, 'r') as file:
        text = file.read()
    text_widger.delete("1.0", tk.END)
    text_widger.insert("1.0", text)
    setattr(text_widger, "path", file_path)

def enregistrer_fichier(text_widger, to_new_file=None, and_delete=False):
    """Enregistrer un fichier"""
    if to_new_file is True or not text_widger.path:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if not file_path:
            return False
        text_widger.path = file_path
    text = text_widger.get("1.0", tk.END)
    with open(text_widger.path, 'w') as file:
        file.write(text)
    if and_delete:
        text_widger.delete("1.0", tk.END)
    return True

def quitter_application(root, text_var):
    """Quitter l'application"""
    result = True
    if len(text_var.get('1.0', tk.END)) > 5:
        if GUI.ask_yes_no("Suppression", "Voulez-vous enregistrer le fichier avant de quitter?"):
            result = enregistrer_fichier(text_var)
    if result:
        root.quit()
        root.hide()



# -- VARIABLES INITIALES --
# root = GUI.set_basic_window("Text Editor")
# main_text = ttk.Text(root)
# setattr(main_text, "path", "")


    







