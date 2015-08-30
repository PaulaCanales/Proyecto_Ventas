# -*- coding: utf-8 -*-
import sqlite3
from PySide import QtGui, QtCore
from ui_Form_Ventas import Ui_Form
from ui_ventas import Ui_Form as ui_venta
import model as db_model

class FormVenta(QtGui.QDialog):

    def __init__(self, parent=None, folio=None):
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
            rut= db_model.obtener_rut()
            for dato in range(len(rut)):
                self.ui.comboRut.addItem(str(rut[dato][0]))
        else:
            detalle = db_model.obtener_ventas_formulario(folio)
            self.ui.comboRut.setEnabled(False)
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

            self.ui.aceptar.clicked.connect(self.edita_venta)

 

    def crear_venta(self):
        pass

    def edita_venta(self): 
        folio,producto.precio,cantidad= self.obtener_datos() 
        
        try: 
            model.editar_cliente(rut, nombres, apellidos, correo)
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
        return (folio,producto.precio,cantidad)
            


        
        
            

	

