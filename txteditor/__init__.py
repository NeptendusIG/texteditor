# __init__.py
""" 
    txteditor - Text Editor Application
    Auteur : Gaetan Lepage 
    Contact : gaetan.lepage18@gmail.com 
    Version : 2.0.0 
    Date : 20-10-26 
    Statut : production 
"""

import logging
import os
from pathlib import Path

# --- Meta Data ---
__version__ = "1.0.0"
__date__ = "20-10-26"
__author__ = "GaetanLepage"
__email__ = "gaetan.lepage18@gmail.com"
__status__ = "production"  # status : dev/test/prod

# --- Initialisation du Logger ---
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
logger.info("Logger initialized for the package")


# --- Expose les fonctionnalités publiques ---
# Importations différées
from .functions import edit_text
from .app import TextEditor as launch_app


# --- __all__ pour les importations globales du package ---
# __all__ spécifie les modules, classes, ou fonctions exportés 
__all__ = [edit_text, launch_app]