#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ui_Login import Ui_Form
import Model as db_model
from ctrl_menu import Main

class Login(QtGui.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # Cargamos las acciones al presionar el menú
        self.menu_actions()
        self.show()

    def menu_actions(self):
        self.ui.ingresar.clicked.connect(self.load_main)

    def load_main(self):
        """
        Funcion que carga al sistema de venta
        si se ingresa el usuario y clave correcta
        """
        name = db_model.obtener_usuario()[0]
        pas = db_model.obtener_pass()[0]
        nombre = self.ui.Usuario.text()
        contrasena = self.ui.contrasena.text()
        if (name==nombre and pas==contrasena):
            self.close()
            widget = Main(self)
            self.setCentralWidget(widget)
            return True
        else:
            self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
            self.ui.errorMessageDialog.showMessage(
                u"Usuario/Contraseña no valida")
            return False

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Login()
    sys.exit(app.exec_())