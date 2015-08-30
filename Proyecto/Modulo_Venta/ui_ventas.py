# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventas.ui'
#
# Created: Sun Aug 30 01:09:45 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(726, 579)
        self.vender = QtGui.QPushButton(Form)
        self.vender.setGeometry(QtCore.QRect(9, 543, 85, 27))
        self.vender.setObjectName("vender")
        self.eliminar = QtGui.QPushButton(Form)
        self.eliminar.setGeometry(QtCore.QRect(340, 540, 85, 27))
        self.eliminar.setObjectName("eliminar")
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(475, 70, 208, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.fecha = QtGui.QDateEdit(self.layoutWidget)
        self.fecha.setWrapping(False)
        self.fecha.setCalendarPopup(True)
        self.fecha.setObjectName("fecha")
        self.gridLayout_2.addWidget(self.fecha, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 4, 0, 1, 2)
        self.comboBox = QtGui.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 2, 1, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_2.addWidget(self.comboBox_2, 3, 1, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(470, 310, 221, 52))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.filtro = QtGui.QComboBox(self.layoutWidget1)
        self.filtro.setObjectName("filtro")
        self.verticalLayout.addWidget(self.filtro)
        self.grilla_prod = QtGui.QTableView(Form)
        self.grilla_prod.setGeometry(QtCore.QRect(10, 20, 431, 511))
        self.grilla_prod.setAlternatingRowColors(True)
        self.grilla_prod.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.grilla_prod.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.grilla_prod.setSortingEnabled(True)
        self.grilla_prod.setObjectName("grilla_prod")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.vender.setText(QtGui.QApplication.translate("Form", "Vender", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar.setText(QtGui.QApplication.translate("Form", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "BUSQUEDA", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Proveedor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Factura", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "FILTRO", None, QtGui.QApplication.UnicodeUTF8))

