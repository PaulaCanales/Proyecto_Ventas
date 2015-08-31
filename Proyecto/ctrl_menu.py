#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui
from ui_menu import Ui_MainWindow
from Modulo_Cliente.ctrl_grid import Main_Cli
from Modulo_Producto.ctrl_producto import Main_Pro
from Modulo_Venta.ctrl_ventas import Main_Ve


class Main(QtGui.QMainWindow):
    """
    Módulo principal del sistema
    """
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Cargamos las acciones al presionar el menú
        self.menu_actions()
        self.show()

    def menu_actions(self):
        self.ui.actionClientes.triggered.connect(self.load_maincli)
        self.ui.actionProductos.triggered.connect(self.load_mainpro)
        self.ui.actionVentas.triggered.connect(self.load_mainve)

    def load_maincli(self):
        widget = Main_Cli(self)
        self.setCentralWidget(widget)

    def load_mainpro(self):
        widget = Main_Pro(self)
        self.setCentralWidget(widget)

    def load_mainve(self):
        widget = Main_Ve(self)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())