# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventas.ui'
#
# Created: Mon Aug 31 04:05:00 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(718, 572)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(460, 50, 261, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sinFiltro = QtGui.QPushButton(self.layoutWidget)
        self.sinFiltro.setObjectName("sinFiltro")
        self.gridLayout_2.addWidget(self.sinFiltro, 1, 2, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.fecha = QtGui.QDateEdit(self.layoutWidget)
        self.fecha.setWrapping(False)
        self.fecha.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 8, 29), QtCore.QTime(0, 0, 0)))
        self.fecha.setMinimumTime(QtCore.QTime(3, 0, 0))
        self.fecha.setCalendarPopup(True)
        self.fecha.setObjectName("fecha")
        self.gridLayout_2.addWidget(self.fecha, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.comboProv = QtGui.QComboBox(self.layoutWidget)
        self.comboProv.setObjectName("comboProv")
        self.comboProv.addItem("")
        self.comboProv.setItemText(0, "")
        self.gridLayout_2.addWidget(self.comboProv, 3, 1, 1, 1)
        self.comboFolio = QtGui.QComboBox(self.layoutWidget)
        self.comboFolio.setObjectName("comboFolio")
        self.comboFolio.addItem("")
        self.comboFolio.setItemText(0, "")
        self.gridLayout_2.addWidget(self.comboFolio, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)
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
        self.filtro.addItem("")
        self.filtro.setItemText(0, "")
        self.verticalLayout.addWidget(self.filtro)
        self.grilla_prod = QtGui.QTableView(Form)
        self.grilla_prod.setGeometry(QtCore.QRect(10, 20, 431, 511))
        self.grilla_prod.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.grilla_prod.setAlternatingRowColors(True)
        self.grilla_prod.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.grilla_prod.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.grilla_prod.setSortingEnabled(True)
        self.grilla_prod.setObjectName("grilla_prod")
        self.layoutWidget2 = QtGui.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(9, 540, 431, 29))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vender = QtGui.QPushButton(self.layoutWidget2)
        self.vender.setObjectName("vender")
        self.horizontalLayout.addWidget(self.vender)
        self.editar = QtGui.QPushButton(self.layoutWidget2)
        self.editar.setObjectName("editar")
        self.horizontalLayout.addWidget(self.editar)
        self.eliminar = QtGui.QPushButton(self.layoutWidget2)
        self.eliminar.setObjectName("eliminar")
        self.horizontalLayout.addWidget(self.eliminar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.grilla_prod, self.vender)
        Form.setTabOrder(self.vender, self.editar)
        Form.setTabOrder(self.editar, self.eliminar)
        Form.setTabOrder(self.eliminar, self.fecha)
        Form.setTabOrder(self.fecha, self.comboProv)
        Form.setTabOrder(self.comboProv, self.comboFolio)
        Form.setTabOrder(self.comboFolio, self.filtro)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.sinFiltro.setText(QtGui.QApplication.translate("Form", "Refrescar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Factura", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "BUSQUEDA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "FILTRO", None, QtGui.QApplication.UnicodeUTF8))
        self.vender.setText(QtGui.QApplication.translate("Form", "Vender", None, QtGui.QApplication.UnicodeUTF8))
        self.editar.setText(QtGui.QApplication.translate("Form", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar.setText(QtGui.QApplication.translate("Form", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

