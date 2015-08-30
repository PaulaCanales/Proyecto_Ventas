# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clientes.ui'
#
# Created: Sun Aug 30 03:36:09 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Cliente(object):
    def setupUi(self, Cliente):
        Cliente.setObjectName("Cliente")
        Cliente.resize(762, 462)
        self.gridLayout = QtGui.QGridLayout(Cliente)
        self.gridLayout.setObjectName("gridLayout")
        self.table = QtGui.QTableView(Cliente)
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setSortingEnabled(True)
        self.table.setObjectName("table")
        self.gridLayout.addWidget(self.table, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(Cliente)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Cliente)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(Cliente)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.retranslateUi(Cliente)
        QtCore.QMetaObject.connectSlotsByName(Cliente)

    def retranslateUi(self, Cliente):
        Cliente.setWindowTitle(QtGui.QApplication.translate("Cliente", "Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Cliente", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Cliente", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Cliente", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

