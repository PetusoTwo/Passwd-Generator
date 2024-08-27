#Generador de contraseñas#
#Autor: Petusotwo
import random
import string
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox, QApplication
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QIntValidator
import sys
    
class Myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super(Myapp, self).__init__()
        uic.loadUi('design.ui', self)

        #Configuraciones de la ventana#
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(0.95)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        #Configuraciones de los botones#
        self.close.clicked.connect(lambda: self.close()) 
        self.copy.clicked.connect(self.copy_password)
        self.generar.clicked.connect(self.generar_password)
        
    def generar_password(self, cantidad, numeros=True, caracterespeciales=True):
        letras = string.ascii_letters
        digitos = string.digits
        caracteres = string.punctuation
        self.maxDigi.setValidator(QIntValidator(0, 10000, self))
        cantidad = self.maxDigi.text()
        password = []
        for i in range(cantidad):
            QMessageBox.information(self, 'Numeros', 'Desea agregar numeros?')
            if self.numeros.isChecked():
                password.append(random.choice(digitos))
            QMessageBox.information(self, 'Caracteres especiales', 'Desea agregar caracteres especiales?')
            if self.caracteresEspeciales.isChecked():
                password.append(random.choice(caracteres))
            password.append(random.choice(letras))
            random.shuffle(password)
            password = ''.join(password)
        self.password.setPlainText(password)
        
    def copy_password(self):        
        if self.password.toPlainText() != '':
            self.password.selectAll()
            self.password.copy()
            self.password.clear()
            QMessageBox.information(self, 'Copiado', 'La contraseña ha sido copiada')
        else:
            QMessageBox.warning(self, 'Advertencia', 'No hay contraseña para copiar')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Myapp()
    window.show()
    sys.exit(app.exec())