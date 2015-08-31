# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created: Mon Aug 31 01:49:23 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 713)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 25))
        self.menubar.setObjectName("menubar")
        self.menuModulos = QtGui.QMenu(self.menubar)
        self.menuModulos.setObjectName("menuModulos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClientes = QtGui.QAction(MainWindow)
        self.actionClientes.setObjectName("actionClientes")
        self.actionProductos = QtGui.QAction(MainWindow)
        self.actionProductos.setObjectName("actionProductos")
        self.actionVentas = QtGui.QAction(MainWindow)
        self.actionVentas.setObjectName("actionVentas")
        self.menuModulos.addAction(self.actionClientes)
        self.menuModulos.addAction(self.actionProductos)
        self.menuModulos.addAction(self.actionVentas)
        self.menubar.addAction(self.menuModulos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.menuModulos.setTitle(QtGui.QApplication.translate("MainWindow", "Modulos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClientes.setText(QtGui.QApplication.translate("MainWindow", "Clientes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProductos.setText(QtGui.QApplication.translate("MainWindow", "Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVentas.setText(QtGui.QApplication.translate("MainWindow", "Ventas", None, QtGui.QApplication.UnicodeUTF8))

