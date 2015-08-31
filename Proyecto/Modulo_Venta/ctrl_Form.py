# -*- coding: utf-8 -*-
import sqlite3
from PySide import QtGui, QtCore
from ui_Form_Ventas import Ui_Form
from ui_ventas import Ui_Form as ui_venta
import model as db_model

class FormVenta(QtGui.QDialog):
    
    def __init__(self, parent=None, folio=None,rut=None):
        """
        Formulario para crear y editar cliente.
        Si se recibe la var folio
        entonces se está en modo de edición.
        """
        super(FormVenta, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        if folio is None:
            
            self.ui.aceptar.clicked.connect(self.crear_venta)
            self.ui.venta.clicked.connect(self.crear_venta2)
            rut= db_model.obtener_rut()
            for dato in range(len(rut)):
                self.ui.comboRut.addItem(str(rut[dato][0]))
        else:
            
            self.ui.comboRut.addItem(str(rut))
            detalle = db_model.obtener_ventas_formulario(folio)
            self.ui.comboRut.setEnabled(False)
            self.ui.folio.setText(str(folio))
            self.ui.folio.setEnabled(False)
            self.ui.id_prod.setEnabled(False)
            self.ui.cantidad.setEnabled(False)
            self.ui.precio.setEnabled(False)
            #Creamos el modelo asociado a la tabla
            self.data = QtGui.QStandardItemModel(len(detalle), 4)
            self.data.setHorizontalHeaderItem(
                0, QtGui.QStandardItem(u"producto"))
            self.data.setHorizontalHeaderItem(
                1, QtGui.QStandardItem(u"cantidad"))
            self.data.setHorizontalHeaderItem(
                2, QtGui.QStandardItem(u"precio unitario"))
            self.data.setHorizontalHeaderItem(
                3, QtGui.QStandardItem(u"Total"))
           

            for r, row in enumerate(detalle):
                index = self.data.index(r, 0, QtCore.QModelIndex())
                self.data.setData(index, row['producto_sku'])
                index = self.data.index(r, 1, QtCore.QModelIndex())
                self.data.setData(index, row['cantidad'])
                index = self.data.index(r, 2, QtCore.QModelIndex())
                self.data.setData(index, row['precio_unitario'])
                index = self.data.index(r, 3, QtCore.QModelIndex())
                self.data.setData(index, row['total'])                

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

            self.ui.aceptar.clicked.connect(self.carga_venta)
            

    def crear_venta(self):        
        folio,producto,precio,cantidad=self.obtener_datos()
        try:
            
            db_model.agregar_venta(folio, producto, cantidad, precio)
            detalle = db_model.obtener_ventas_formulario(folio)
            self.ui.comboRut.setEnabled(False)
            self.ui.folio.setText(str(folio))
            self.ui.folio.setEnabled(False)
            
            #Creamos el modelo asociado a la tabla
            self.data = QtGui.QStandardItemModel(len(detalle), 4)
            self.data.setHorizontalHeaderItem(
                0, QtGui.QStandardItem(u"producto"))
            self.data.setHorizontalHeaderItem(
                1, QtGui.QStandardItem(u"cantidad"))
            self.data.setHorizontalHeaderItem(
                2, QtGui.QStandardItem(u"precio unitario"))
            self.data.setHorizontalHeaderItem(
                3, QtGui.QStandardItem(u"Total"))           

            for r, row in enumerate(detalle):
                index = self.data.index(r, 0, QtCore.QModelIndex())
                self.data.setData(index, row['producto_sku'])
                index = self.data.index(r, 1, QtCore.QModelIndex())
                self.data.setData(index, row['cantidad'])
                index = self.data.index(r, 2, QtCore.QModelIndex())
                self.data.setData(index, row['precio_unitario'])
                index = self.data.index(r, 3, QtCore.QModelIndex())
                self.data.setData(index, row['total'])               

            self.ui.grilla_prod.setModel(self.data)
            
        except sqlite3.Error as e: 
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"Error !")
            msgBox.exec_() 

    def crear_venta2(self):
        rut=int(self.ui.comboRut.currentText ())
        folio = self.ui.folio.text()
        try:
            db_model.crear_venta(int(folio), rut)
            self.close()

        except sqlite3.Error as e: 
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"Error !")
            msgBox.exec_() 
        

    def carga_venta(self):
        
        self.ui.cantidad.setEnabled(True)
        self.ui.precio.setEnabled(True)
        data = self.ui.grilla_prod.model()
        index = self.ui.grilla_prod.currentIndex()
        self.ui.id_prod.setText(str(data.index(index.row(), 0, QtCore.QModelIndex()).data()))
        self.ui.cantidad.setText(str(data.index(index.row(), 1, QtCore.QModelIndex()).data()))
        self.ui.precio.setText(str(data.index(index.row(), 2, QtCore.QModelIndex()).data()))
        self.ui.venta.clicked.connect(self.edita_venta)

    def edita_venta(self): 
        folio,producto,precio,cantidad= self.obtener_datos() 
        
        try: 
            db_model.editar_venta(folio,producto,cantidad,precio)
            # Invocar la función del modelo que permite editar 
            self.accepted.emit() 
            msgBox = QtGui.QMessageBox() 
            msgBox.setText(u"La Venta ha sido editado.") 
            msgBox.exec_() 
            self.close() 
            print "Editar" 
        except sqlite3.Error as e: 
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"Error!")
            msgBox.exec_() 

    def obtener_datos(self):
        """
        Obtiene los datos colocados por el usuario
        en el formulario
        """
        folio = self.ui.folio.text()
        producto = self.ui.id_prod.text()
        cantidad = self.ui.cantidad.text()
        precio = self.ui.precio.text()
        return (int(folio),producto,int(precio),int(cantidad))
            

            


        
        
            

	

