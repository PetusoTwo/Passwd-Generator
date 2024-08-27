import random
import string
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
import sys
#Este generador de contraseñas la cantiodad que ingreses es la cantidad que te dara de cada tipo (numero, letras, caracteres especiales)#
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('design.ui', self)

        self.maxDigi = self.findChild(QtWidgets.QLineEdit, 'maxDigi')
        self.password = self.findChild(QtWidgets.QTextEdit, 'password')

        # Configuraciones de la ventana
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(0.95)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Configuraciones de los botones
        self.close.clicked.connect(lambda: self.close()) 
        self.copy.clicked.connect(self.copy_password)
        self.generar.clicked.connect(self.generar_password)
        
        # Agregar el validador para permitir solo números
        self.maxDigi.setValidator(QIntValidator(1, 10000, self))
        
    def generar_password(self):
        try:
            cantidad = self.maxDigi.text()
            if not cantidad.isdigit() or int(cantidad) <= 0:
                QMessageBox.warning(self, 'Error', 'Por favor, ingrese un número válido.')
                return
            cantidad = int(cantidad)
            letras = string.ascii_letters
            digitos = string.digits
            caracteres = string.punctuation
            password = []
            # Pregunta si quiere agregar numeros a la password
            respuesta_numeros = QMessageBox.question(
                self, 'Números', '¿Desea agregar números a la contraseña?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            # Pregunta si quiere agregar caracteres especiales a la password
            respuesta_caracteres = QMessageBox.question(
                self, 'Caracteres especiales', '¿Desea agregar caracteres especiales a la contraseña?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            # Generar la contraseña
            for i in range(cantidad):
                if respuesta_numeros == QMessageBox.StandardButton.Yes:
                    password.append(random.choice(digitos))
                if respuesta_caracteres == QMessageBox.StandardButton.Yes:
                    password.append(random.choice(caracteres))
                password.append(random.choice(letras))
            random.shuffle(password)
            password = ''.join(password)
            self.password.setPlainText(password)
        except Exception as e:
            QMessageBox.critical(self, "Error", "No se pudo generar la contraseña :c ")
        
    def copy_password(self):        
        if self.password.toPlainText() != '':
            self.password.selectAll()
            self.password.copy()
            self.password.clear()
            QMessageBox.information(self, 'Copiado', 'La contraseña ha sido copiada en el portapapeles.')
        else:
            QMessageBox.warning(self, 'Advertencia', 'No hay contraseña para copiar')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
