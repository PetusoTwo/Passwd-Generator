#Generador de contraseñas#
#Autor: Petusotwo
import random
import string
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox, QApplication
from PyQt6.QtCore import Qt, QPoint

def generate_password(cantidad, numeros=True, caracterespeciales=True):
    letras = string.ascii_letters
    digitos = string.digits
    caracteres = string.punctuation
    password = []
    for i in range(cantidad):
        if numeros:
            password.append(random.choice(digitos))
        if caracterespeciales:
            password.append(random.choice(caracteres))
        password.append(random.choice(letras))
    random.shuffle(password)
    password = ''.join(password)
    return password

