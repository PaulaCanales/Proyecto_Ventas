#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ctrl_Form import FormVenta
from ui_ventas import Ui_Form
import model as db_model


class Main(QtGui.QWidget):
    
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.load_data()
        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.ui.vender.clicked.connect(self.add)
        self.ui.eliminar.clicked.connect(self.delete)
        self.ui.pushButton_3.clicked.connect(self.busca)
        self.ui.editar.clicked.connect(self.editar)

    def add(self):        
        self.ui.form = FormVenta(self)
        self.ui.form.accepted.connect(self.load_data)
        self.ui.form.show()

    def load_data(self):
        """
        Función que carga la información de ventas en la grilla
        """
        ventas = db_model.obtener_ventas()
        #Creamos el modelo asociado a la tabla
        self.data = QtGui.QStandardItemModel(len(ventas), 4)
        self.data.setHorizontalHeaderItem(
            0, QtGui.QStandardItem(u"folio"))
        self.data.setHorizontalHeaderItem(
            1, QtGui.QStandardItem(u"cliente_rut"))
        self.data.setHorizontalHeaderItem(
            2, QtGui.QStandardItem(u"fecha"))
        self.data.setHorizontalHeaderItem(
            3, QtGui.QStandardItem(u"TotalVentas"))
       

        for r, row in enumerate(ventas):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['folio'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['cliente_rut'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['fecha'])
            index = self.data.index(r, 3, QtCore.QModelIndex())
            self.data.setData(index, db_model.obtener_total_Venta(row['folio']))
            

        self.ui.grilla_prod.setModel(self.data)

        # Para que las columnas 1 y 2 se estire o contraiga cuando
        # se cambia el tamaño de la pantalla
        self.ui.grilla_prod.horizontalHeader().setResizeMode(
            1, self.ui.grilla_prod.horizontalHeader().Stretch)
        self.ui.grilla_prod.horizontalHeader().setResizeMode(
            2, self.ui.grilla_prod.horizontalHeader().Stretch)

        self.ui.grilla_prod.setColumnWidth(0, 100)
        self.ui.grilla_prod.setColumnWidth(1, 210)
        self.ui.grilla_prod.setColumnWidth(2, 210)
        self.ui.grilla_prod.setColumnWidth(3, 220)

    def delete(self):        

        # ANTES DE REALIZAR LA ACCIÓN SE DEBERÍA PREGUNTAR
        # AL USUARIO CONFIRMAR LA OPERACIÓN !!!!!!!!!!!!!!
        data = self.ui.grilla_prod.model()
        index = self.ui.grilla_prod.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:                           
            folio = data.index(index.row(), 0, QtCore.QModelIndex()).data()            
            if (db_model.borrar(folio)):
                self.load_data()
                msgBox = QtGui.QMessageBox()
                msgBox.setText(u"EL registro fue eliminado.")
                msgBox.exec_()
                return True
            else:
                self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                self.ui.errorMessageDialog.showMessage(
                    u"Error al eliminar el registro")
                return False
                  

    def busca(self):
        
        data = self.ui.grilla_prod.model()
        index = self.ui.grilla_prod.currentIndex()

    def editar(self):
        data = self.ui.grilla_prod.model()
        index = self.ui.grilla_prod.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False    
        else:
            folio = data.index(index.row(), 0, QtCore.QModelIndex()).data()
            print folio
            self.ui.form = FormVenta(self, folio)
            self.ui.form.accepted.connect(self.load_data)
            self.ui.form.show()
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())