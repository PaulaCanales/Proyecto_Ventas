#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ctrl_form import FormCliente
from Ui_Cliente import Ui_Cliente
import model as db_model




class Main_Cli(QtGui.QWidget):
    """
    Controlador Principal Clientes
    """
    
    def __init__(self, parent=None):
        super(Main_Cli, self).__init__(parent)
        self.ui = Ui_Cliente()
        self.ui.setupUi(self)

        self.load_data()
        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.ui.pushButton.clicked.connect(self.add)
        self.ui.pushButton_3.clicked.connect(self.delete)
        self.ui.pushButton_2.clicked.connect(self.edit)

    def add(self):        
        self.ui.form = FormCliente(self)
        self.ui.form.accepted.connect(self.load_data)
        self.ui.form.show()

    def load_data(self):
        """
        Función que carga la información de clientes en la grilla
        """
        clientes = db_model.obtener_rut()
        #Creamos el modelo asociado a la tabla
        self.data = QtGui.QStandardItemModel(len(clientes), 6)
        self.data.setHorizontalHeaderItem(
            0, QtGui.QStandardItem(u"RUT"))
        self.data.setHorizontalHeaderItem(
            1, QtGui.QStandardItem(u"Nombres"))
        self.data.setHorizontalHeaderItem(
            2, QtGui.QStandardItem(u"Apellidos"))
        self.data.setHorizontalHeaderItem(
            3, QtGui.QStandardItem(u"Correo"))
        self.data.setHorizontalHeaderItem(
            4, QtGui.QStandardItem(u"TotalVentas"))
        self.data.setHorizontalHeaderItem(
            5, QtGui.QStandardItem(u"TotalIngreso"))

        for r, row in enumerate(clientes):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['rut'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['nombres'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['apellidos'])
            index = self.data.index(r, 3, QtCore.QModelIndex())
            self.data.setData(index, row['correo'])
            index = self.data.index(r, 4, QtCore.QModelIndex())
            self.data.setData(index, db_model.obtener_TotalVenta(row['rut']))
            index = self.data.index(r, 5, QtCore.QModelIndex())
            self.data.setData(index, db_model.obtener_TotalIngreso(row['rut']))

        self.ui.table.setModel(self.data)

        # Para que las columnas 1 y 2 se estire o contraiga cuando
        # se cambia el tamaño de la pantalla
        self.ui.table.horizontalHeader().setResizeMode(
            1, self.ui.table.horizontalHeader().Stretch)
        self.ui.table.horizontalHeader().setResizeMode(
            2, self.ui.table.horizontalHeader().Stretch)

        self.ui.table.setColumnWidth(0, 100)
        self.ui.table.setColumnWidth(1, 210)
        self.ui.table.setColumnWidth(2, 210)
        self.ui.table.setColumnWidth(3, 220)

    def delete(self):
        """
        Funcion que elimina un cliente, 
        validando que no tenga ventas asociadas
        """
        data = self.ui.table.model()
        index = self.ui.table.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:
            #Confirmacion eliminar
            quit_msg = "¿esta seguro que desea eliminar el cliente?"
            reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                
                rut = data.index(index.row(), 0, QtCore.QModelIndex()).data()
                if db_model.obtener_TotalVenta(rut)==0:
                    if (db_model.borrar(rut)):
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
                else:
                        msgBox = QtGui.QMessageBox()
                        msgBox.setText(u"Cliente posee ventas")
                        msgBox.exec_()        

    def edit(self):
        """
        Se abre el formulario de edicion.
        """
        
        data = self.ui.table.model()
        index = self.ui.table.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False    
        else:
            rut = data.index(index.row(), 0, QtCore.QModelIndex()).data()
            print rut
            
            self.ui.form = FormCliente(self, rut)
            self.ui.form.accepted.connect(self.load_data)
            self.ui.form.show()
            


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main_Cli()
    sys.exit(app.exec_())
