# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_ventas.ui'
#
# Created: Sun Aug 30 13:07:57 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(465, 441)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboRut = QtGui.QComboBox(Form)
        self.comboRut.setObjectName("comboRut")
        self.comboRut.addItem("")
        self.comboRut.setItemText(0, "")
        self.gridLayout.addWidget(self.comboRut, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.id_prod = QtGui.QLineEdit(Form)
        self.id_prod.setObjectName("id_prod")
        self.gridLayout.addWidget(self.id_prod, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.precio = QtGui.QLineEdit(Form)
        self.precio.setObjectName("precio")
        self.gridLayout.addWidget(self.precio, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.cantidad = QtGui.QLineEdit(Form)
        self.cantidad.setObjectName("cantidad")
        self.gridLayout.addWidget(self.cantidad, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.folio = QtGui.QLineEdit(Form)
        self.folio.setObjectName("folio")
        self.gridLayout.addWidget(self.folio, 1, 1, 1, 1)
        self.aceptar = QtGui.QPushButton(Form)
        self.aceptar.setObjectName("aceptar")
        self.gridLayout.addWidget(self.aceptar, 6, 1, 1, 1)
        self.grilla_prod = QtGui.QTableView(Form)
        self.grilla_prod.setAlternatingRowColors(True)
        self.grilla_prod.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.grilla_prod.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.grilla_prod.setSortingEnabled(True)
        self.grilla_prod.setObjectName("grilla_prod")
        self.gridLayout.addWidget(self.grilla_prod, 5, 1, 1, 2)
        self.venta = QtGui.QPushButton(Form)
        self.venta.setObjectName("venta")
        self.gridLayout.addWidget(self.venta, 7, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.comboRut, self.pushButton)
        Form.setTabOrder(self.pushButton, self.folio)
        Form.setTabOrder(self.folio, self.id_prod)
        Form.setTabOrder(self.id_prod, self.precio)
        Form.setTabOrder(self.precio, self.cantidad)
        Form.setTabOrder(self.cantidad, self.grilla_prod)
        Form.setTabOrder(self.grilla_prod, self.aceptar)
        Form.setTabOrder(self.aceptar, self.venta)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Rut Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Nuevo Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "ID Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Precio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Cantidad", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Detalle Informacion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Folio", None, QtGui.QApplication.UnicodeUTF8))
        self.aceptar.setText(QtGui.QApplication.translate("Form", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.venta.setText(QtGui.QApplication.translate("Form", "Terminar Venta", None, QtGui.QApplication.UnicodeUTF8))

