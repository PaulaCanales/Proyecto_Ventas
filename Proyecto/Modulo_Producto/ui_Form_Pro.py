# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_Pro.ui'
#
# Created: Tue Aug 25 15:23:19 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(409, 397)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.nombre = QtGui.QLineEdit(Form)
        self.nombre.setObjectName("nombre")
        self.gridLayout.addWidget(self.nombre, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.imagen = QtGui.QLineEdit(Form)
        self.imagen.setObjectName("imagen")
        self.gridLayout.addWidget(self.imagen, 4, 1, 1, 1)
        self.cargar = QtGui.QPushButton(Form)
        self.cargar.setObjectName("cargar")
        self.gridLayout.addWidget(self.cargar, 4, 2, 1, 1)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.descripcion = QtGui.QTextEdit(Form)
        self.descripcion.setObjectName("descripcion")
        self.gridLayout.addWidget(self.descripcion, 6, 1, 1, 2)
        self.marca = QtGui.QLineEdit(Form)
        self.marca.setObjectName("marca")
        self.gridLayout.addWidget(self.marca, 2, 1, 1, 1)
        self.color = QtGui.QLineEdit(Form)
        self.color.setObjectName("color")
        self.gridLayout.addWidget(self.color, 3, 1, 1, 1)
        self.id = QtGui.QLineEdit(Form)
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 0, 1, 1, 1)
        self.agregar = QtGui.QPushButton(Form)
        self.agregar.setObjectName("agregar")
        self.gridLayout.addWidget(self.agregar, 7, 1, 1, 1)
        self.precio = QtGui.QLineEdit(Form)
        self.precio.setObjectName("precio")
        self.gridLayout.addWidget(self.precio, 5, 1, 1, 1)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Formulario", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Imagen", None, QtGui.QApplication.UnicodeUTF8))
        self.cargar.setText(QtGui.QApplication.translate("Form", "Cargar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Descripción", None, QtGui.QApplication.UnicodeUTF8))
        self.agregar.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Precio", None, QtGui.QApplication.UnicodeUTF8))

