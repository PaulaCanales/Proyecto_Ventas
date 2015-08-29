# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Productos.ui'
#
# Created: Sat Aug 29 15:32:31 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Productos(object):
    def setupUi(self, Productos):
        Productos.setObjectName("Productos")
        Productos.resize(817, 619)
        self.gridLayout_3 = QtGui.QGridLayout(Productos)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtGui.QLabel(Productos)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.buscar = QtGui.QPushButton(Productos)
        self.buscar.setObjectName("buscar")
        self.gridLayout_2.addWidget(self.buscar, 3, 0, 1, 2)
        self.combosku = QtGui.QComboBox(Productos)
        self.combosku.setEditable(True)
        self.combosku.setObjectName("combosku")
        self.gridLayout_2.addWidget(self.combosku, 1, 1, 1, 1)
        self.combonombre = QtGui.QComboBox(Productos)
        self.combonombre.setEditable(True)
        self.combonombre.setObjectName("combonombre")
        self.gridLayout_2.addWidget(self.combonombre, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Productos)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtGui.QLabel(Productos)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.grilla_prod = QtGui.QTableView(Productos)
        self.grilla_prod.setAlternatingRowColors(True)
        self.grilla_prod.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.grilla_prod.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.grilla_prod.setSortingEnabled(True)
        self.grilla_prod.setObjectName("grilla_prod")
        self.gridLayout_3.addWidget(self.grilla_prod, 1, 0, 2, 3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.agregar = QtGui.QPushButton(Productos)
        self.agregar.setObjectName("agregar")
        self.gridLayout.addWidget(self.agregar, 0, 0, 1, 1)
        self.editar = QtGui.QPushButton(Productos)
        self.editar.setObjectName("editar")
        self.gridLayout.addWidget(self.editar, 0, 1, 1, 1)
        self.eliminar = QtGui.QPushButton(Productos)
        self.eliminar.setObjectName("eliminar")
        self.gridLayout.addWidget(self.eliminar, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.imagen = QtGui.QWidget(Productos)
        self.imagen.setObjectName("imagen")
        self.gridLayout_3.addWidget(self.imagen, 3, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 3, 1, 1, 1)

        self.retranslateUi(Productos)
        QtCore.QMetaObject.connectSlotsByName(Productos)

    def retranslateUi(self, Productos):
        Productos.setWindowTitle(QtGui.QApplication.translate("Productos", "Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Productos", "Código", None, QtGui.QApplication.UnicodeUTF8))
        self.buscar.setText(QtGui.QApplication.translate("Productos", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Productos", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Productos", "BUSQUEDA", None, QtGui.QApplication.UnicodeUTF8))
        self.agregar.setText(QtGui.QApplication.translate("Productos", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.editar.setText(QtGui.QApplication.translate("Productos", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar.setText(QtGui.QApplication.translate("Productos", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

