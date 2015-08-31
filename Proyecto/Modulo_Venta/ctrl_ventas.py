#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ctrl_Form import FormVenta
from ui_ventas import Ui_Form
import model as db_model
import datetime 

class Main_Ve(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(Main_Ve, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #self.filtrar()
        self.ui.comboProv.activated[int].connect(self.onActivated_cliente)
        self.ui.filtro.activated[int].connect(self.onActivated_producto)
        self.ui.comboFolio.activated[int].connect(self.onActivated_folio)
        ##self.ui.fecha.activated[int].connect(self.onActivated_fecha)
        self.ui.fecha.dateChanged.connect(self.onActivated_fecha)
        self.load_data()
        self.connect_signals()
        self.show()

    def connect_signals(self):
        """
        Funcion que conecta señales
        """
        self.ui.vender.clicked.connect(self.add)
        self.ui.eliminar.clicked.connect(self.delete)
        self.ui.sinFiltro.clicked.connect(self.load_data)
        self.ui.editar.clicked.connect(self.editar)

    def add(self):
        """
        Funcion que al agregar producto, actualiza la grilla
        y muestra un mensaje
        """        
        self.ui.form = FormVenta(self)
        self.ui.form.accepted.connect(self.load_data)
        self.ui.form.show()

    def load_data(self):
        """
        Función que carga la información de ventas en la grilla
        """
        #Se actualizan los combobox.
        self.ui.comboFolio.clear()
        self.ui.comboFolio.addItem("")
        self.ui.comboProv.clear()
        self.ui.comboProv.addItem("")
        self.ui.filtro.clear()
        self.ui.filtro.addItem("")
        self.filtrar()

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
        """
        Elimina una venta
        """
        data = self.ui.grilla_prod.model()
        index = self.ui.grilla_prod.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:
            quit_msg = "¿Esta seguro que desea eliminar la venta?"
            reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                
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
                  

    def editar(self):
        """
        Edita una venta
        """
        data = self.ui.grilla_prod.model()
        index = self.ui.grilla_prod.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False    
        else:
            folio = data.index(index.row(), 0, QtCore.QModelIndex()).data()
            rut = data.index(index.row(), 1, QtCore.QModelIndex()).data()
            print folio
            self.ui.form = FormVenta(self, folio,rut)
            self.ui.form.accepted.connect(self.load_data)
            self.ui.form.show()

    def filtrar(self):
        """
        Funcion que agrega todos los folios y productos al combobox
        """
        rut= db_model.obtener_rut()
        for dato in range(len(rut)):
            self.ui.comboProv.addItem(str(rut[dato][0]))

        folio= db_model.obtener_folio()
        for dato in range(len(folio)):
            self.ui.comboFolio.addItem(str(folio[dato][0]))

        productos= db_model.obtener_producto()
        for dato in range(len(productos)):
            self.ui.filtro.addItem(str(productos[dato][0]))

    def onActivated_cliente(self, index1):

        cliente = self.ui.comboProv.itemText(index1)

        if cliente=="":
            self.load_data()
        else:
            client = db_model.obtener_cliente(cliente)
            
            #Creamos el modelo asociado a la tabla

            self.data = QtGui.QStandardItemModel(len(client), 4)
            self.data.setHorizontalHeaderItem(
                0, QtGui.QStandardItem(u"folio"))
            self.data.setHorizontalHeaderItem(
                1, QtGui.QStandardItem(u"cliente_rut"))
            self.data.setHorizontalHeaderItem(
                2, QtGui.QStandardItem(u"fecha"))
            self.data.setHorizontalHeaderItem(
                3, QtGui.QStandardItem(u"TotalVentas"))
           

            for r, row in enumerate(client):
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

    def onActivated_fecha(self, index1):
        """
        Al seleccionar una fecha, se filtra la grilla ventas
        """
        
        fecha = self.ui.fecha.date()
        
        #print fecha.toPyDateTime()
        index1=index1.toPython()    
        ventas = db_model.filtrar_fecha(index1)
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

    def onActivated_folio(self, index1):
        """
        Al seleccionar un folio en el comboFolio,
        se filtra a grilla de ventas
        """
        folio = self.ui.comboFolio.itemText(index1)
        if folio=="":
            self.load_data()
        else:
            ventas = db_model.venta_folio(folio)
            
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
    
    def onActivated_producto(self, index1):
        """
        Al seleccionar un sku en filtro,
        se filtra la grilla ventas
        """

        sku = self.ui.filtro.itemText(index1)
        
        if sku=="":
            self.load_data()
        else:
            ventas = db_model.filtrar_producto(sku)

            
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
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main_Ve()
    sys.exit(app.exec_())