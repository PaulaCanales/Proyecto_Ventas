# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Productos.ui'
#
# Created: Tue Aug 25 21:51:45 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Productos(object):
    def setupUi(self, Productos):
        Productos.setObjectName("Productos")
        Productos.resize(697, 490)
        self.imagen = QtGui.QWidget(Productos)
        self.imagen.setGeometry(QtCore.QRect(470, 240, 171, 141))
        self.imagen.setObjectName("imagen")
        self.layoutWidget = QtGui.QWidget(Productos)
        self.layoutWidget.setGeometry(QtCore.QRect(450, 110, 241, 118))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.buscar = QtGui.QPushButton(self.layoutWidget)
        self.buscar.setObjectName("buscar")
        self.gridLayout_2.addWidget(self.buscar, 3, 0, 1, 2)
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.combosku = QtGui.QComboBox(self.layoutWidget)
        self.combosku.setEditable(True)
        self.combosku.setObjectName("combosku")
        self.gridLayout_2.addWidget(self.combosku, 1, 1, 1, 1)
        self.combonombre = QtGui.QComboBox(self.layoutWidget)
        self.combonombre.setEditable(True)
        self.combonombre.setObjectName("combonombre")
        self.gridLayout_2.addWidget(self.combonombre, 2, 1, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(Productos)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 440, 411, 29))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.agregar = QtGui.QPushButton(self.layoutWidget1)
        self.agregar.setObjectName("agregar")
        self.gridLayout.addWidget(self.agregar, 0, 0, 1, 1)
        self.editar = QtGui.QPushButton(self.layoutWidget1)
        self.editar.setObjectName("editar")
        self.gridLayout.addWidget(self.editar, 0, 1, 1, 1)
        self.eliminar = QtGui.QPushButton(self.layoutWidget1)
        self.eliminar.setObjectName("eliminar")
        self.gridLayout.addWidget(self.eliminar, 0, 2, 1, 1)
        self.grilla_prod = QtGui.QTableView(Productos)
        self.grilla_prod.setGeometry(QtCore.QRect(10, 20, 421, 391))
        self.grilla_prod.setAlternatingRowColors(True)
        self.grilla_prod.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.grilla_prod.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.grilla_prod.setSortingEnabled(True)
        self.grilla_prod.setObjectName("grilla_prod")

        self.retranslateUi(Productos)
        QtCore.QMetaObject.connectSlotsByName(Productos)

    def retranslateUi(self, Productos):
        Productos.setWindowTitle(QtGui.QApplication.translate("Productos", "Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Productos", "Código", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Productos", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.buscar.setText(QtGui.QApplication.translate("Productos", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Productos", "BUSQUEDA", None, QtGui.QApplication.UnicodeUTF8))
        self.agregar.setText(QtGui.QApplication.translate("Productos", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.editar.setText(QtGui.QApplication.translate("Productos", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar.setText(QtGui.QApplication.translate("Productos", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

