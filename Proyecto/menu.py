# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created: Tue Aug 25 12:34:34 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(264, 469)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.productos = QtGui.QPushButton(self.centralwidget)
        self.productos.setObjectName("productos")
        self.verticalLayout.addWidget(self.productos)
        self.clientes = QtGui.QPushButton(self.centralwidget)
        self.clientes.setObjectName("clientes")
        self.verticalLayout.addWidget(self.clientes)
        self.ventas = QtGui.QPushButton(self.centralwidget)
        self.ventas.setObjectName("ventas")
        self.verticalLayout.addWidget(self.ventas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 264, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.productos.setText(QtGui.QApplication.translate("MainWindow", "Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.clientes.setText(QtGui.QApplication.translate("MainWindow", "Clientes", None, QtGui.QApplication.UnicodeUTF8))
        self.ventas.setText(QtGui.QApplication.translate("MainWindow", "Ventas", None, QtGui.QApplication.UnicodeUTF8))

