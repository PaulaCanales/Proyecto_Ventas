#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ctrl_form import FormProducto
from ui_Productos import Ui_Productos
import model as db_model

 
class Main_Pro(QtGui.QWidget):
    """
    Esta es una grilla y un buscador
    """
    def __init__(self, parent=None):
        super(Main_Pro, self).__init__(parent)
        self.ui = Ui_Productos()
        self.ui.setupUi(self)

        self.load_data()
        self.connect_signals()
        self.ui.combosku.activated[int].connect(self.onActivated_sku)
        self.ui.combonombre.activated[int].connect(self.onActivated_nombre)
        self.show()

    def connect_signals(self):
        self.ui.agregar.clicked.connect(self.agrega)
        self.ui.actualizar.clicked.connect(self.load_data)
        self.ui.eliminar.clicked.connect(self.elimina)
        self.ui.editar.clicked.connect(self.edita)
        self.ui.grilla_prod.clicked.connect(self.show_poster)

    def agrega(self):
        self.ui.form = FormProducto(self)
        self.ui.form.accepted.connect(self.load_data)
        self.ui.form.show()

    def load_data(self):
        """
        Función que carga la información de productos en la grilla
        """
        #Se actualizan los combobox.
        self.ui.combosku.clear()
        self.ui.combosku.addItem("")
        self.ui.combonombre.clear()
        self.ui.combonombre.addItem("")
        self.filtrar()

        producto = db_model.obtener_producto()
        #Creamos el modelo asociado a la tabla
        self.data = QtGui.QStandardItemModel(len(producto), 8)
        self.data.setHorizontalHeaderItem(
            0, QtGui.QStandardItem(u"ID"))
        self.data.setHorizontalHeaderItem(
            1, QtGui.QStandardItem(u"Nombre"))
        self.data.setHorizontalHeaderItem(
            2, QtGui.QStandardItem(u"Descripcion"))
        self.data.setHorizontalHeaderItem(
            3, QtGui.QStandardItem(u"Marca"))
        self.data.setHorizontalHeaderItem(
            4, QtGui.QStandardItem(u"Color"))
        self.data.setHorizontalHeaderItem(
            5, QtGui.QStandardItem(u"Imagen"))
        self.data.setHorizontalHeaderItem(
            6, QtGui.QStandardItem(u"Precio"))
        self.data.setHorizontalHeaderItem(
            7, QtGui.QStandardItem(u"Cantidad"))
        self.data.setHorizontalHeaderItem(
            8, QtGui.QStandardItem(u"Total"))
        
        cantidad_producto=0

        for r, row in enumerate(producto):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['sku'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['nombre'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['descripcion'])
            index = self.data.index(r, 3, QtCore.QModelIndex())
            self.data.setData(index, row['marca'])
            index = self.data.index(r, 4, QtCore.QModelIndex())
            self.data.setData(index, row['color'])
            index = self.data.index(r, 5, QtCore.QModelIndex())
            self.data.setData(index, row['imagen'])
            index = self.data.index(r, 6, QtCore.QModelIndex())
            self.data.setData(index, row['Precio'])
            index = self.data.index(r, 7, QtCore.QModelIndex())

            cantidad_producto= db_model.obtener_CantidadProducto(row['sku'])
            
            self.data.setData(index, cantidad_producto)
            index = self.data.index(r, 8, QtCore.QModelIndex())
            self.data.setData(index, cantidad_producto*row['Precio'])
            


        self.ui.grilla_prod.setModel(self.data)

        
        self.ui.grilla_prod.setColumnWidth(0, 100)
        self.ui.grilla_prod.setColumnWidth(1, 150)
        self.ui.grilla_prod.setColumnWidth(2, 200)
        self.ui.grilla_prod.setColumnWidth(3, 100)
        self.ui.grilla_prod.setColumnWidth(4, 100)
        self.ui.grilla_prod.setColumnWidth(5, 200)
        self.ui.grilla_prod.setColumnWidth(6, 100)
        self.ui.grilla_prod.setColumnWidth(7, 100)
        self.ui.grilla_prod.setColumnWidth(8, 100)



    def elimina(self):
        """
        Función que intenta borrar un alumno de la base de datos e
        indica el resultado de la operación
        """

        # ANTES DE REALIZAR LA ACCIÓN SE DEBERÍA PREGUNTAR
        # AL USUARIO CONFIRMAR LA OPERACIÓN !!!!!!!!!!!!!!
        data = self.ui.grilla_prod.model()
        index = self.ui.grilla_prod.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False

        else:
            quit_msg = "¿Esta seguro que desea eliminar el producto?"
            reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                
                sku = data.index(index.row(), 0, QtCore.QModelIndex()).data()
                if db_model.eliminar_revision(sku):
                    if (db_model.borrar(sku)):
                        self.load_data()
                        msgBox = QtGui.QMessageBox()
                        msgBox.setText(u"EL producto fue eliminado.")
                        msgBox.exec_()
                        return True
                    else:
                        self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                        self.ui.errorMessageDialog.showMessage(
                            u"Error al eliminar el producto")
                        return False
                else:
                        msgBox = QtGui.QMessageBox()
                        msgBox.setText(u"Cliente posee ventas, imposible eliminar")
                        msgBox.exec_()

   

    def edita(self):
        """
        Función obtiene el producto seleccionado en la grilla
        para poner sus datos en el formulario para su edición
        """
        data = self.ui.grilla_prod.model()
        index = self.ui.grilla_prod.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:
            sku = data.index(index.row(), 0, QtCore.QModelIndex()).data()
            self.ui.form = FormProducto(self, sku)
            self.ui.form.accepted.connect(self.load_data)
            self.ui.form.show()

    def show_poster(self):
        """
        Funcion que muestra la imagen del producto en un label
        """
        data = self.ui.grilla_prod.model()
        index = self.ui.grilla_prod.currentIndex()
        imagen = data.index(index.row(), 5, QtCore.QModelIndex()).data()
        # Ahora la imagen
        img = QtGui.QPixmap(str(imagen))
        self.ui.img.setPixmap(img.scaled(100,100))


    def filtrar(self):
        """
        Funcion que agrega todos los sku y nombre al combobox
        """
        sku= db_model.obtener_sku()
        for dato in range(len(sku)):
            self.ui.combosku.addItem(str(sku[dato][0]))

        nombre= db_model.obtener_nombre()
        for dato in range(len(nombre)):
            self.ui.combonombre.addItem(str(nombre[dato][0]))


    def onActivated_sku(self, index1):

        sku = self.ui.combosku.itemText(index1)
        if sku=="":
            self.load_data()
        else:
            lista=[]
            producto = db_model.producto_sku(sku)
            lista.append(producto)
            #Creamos el modelo asociado a la tabla
            self.data = QtGui.QStandardItemModel(len(lista), 8)
            self.data.setHorizontalHeaderItem(
                0, QtGui.QStandardItem(u"ID"))
            self.data.setHorizontalHeaderItem(
                1, QtGui.QStandardItem(u"Nombre"))
            self.data.setHorizontalHeaderItem(
                2, QtGui.QStandardItem(u"Descripcion"))
            self.data.setHorizontalHeaderItem(
                3, QtGui.QStandardItem(u"Marca"))
            self.data.setHorizontalHeaderItem(
                4, QtGui.QStandardItem(u"Color"))
            self.data.setHorizontalHeaderItem(
                5, QtGui.QStandardItem(u"Imagen"))
            self.data.setHorizontalHeaderItem(
                6, QtGui.QStandardItem(u"Precio"))
            self.data.setHorizontalHeaderItem(
                7, QtGui.QStandardItem(u"Cantidad"))
            self.data.setHorizontalHeaderItem(
                8, QtGui.QStandardItem(u"Total"))

            for r, row in enumerate(lista):
            	index = self.data.index(r, 0, QtCore.QModelIndex())
            	self.data.setData(index, row['sku'])
            	index = self.data.index(r, 1, QtCore.QModelIndex())
            	self.data.setData(index, row['nombre'])
            	index = self.data.index(r, 2, QtCore.QModelIndex())
            	self.data.setData(index, row['descripcion'])
            	index = self.data.index(r, 3, QtCore.QModelIndex())
            	self.data.setData(index, row['marca'])
            	index = self.data.index(r, 4, QtCore.QModelIndex())
            	self.data.setData(index, row['color'])
            	index = self.data.index(r, 5, QtCore.QModelIndex())
            	self.data.setData(index, row['imagen'])
            	index = self.data.index(r, 6, QtCore.QModelIndex())
            	self.data.setData(index, row['Precio'])
            	index = self.data.index(r, 7, QtCore.QModelIndex())
            	cantidad_producto= db_model.obtener_CantidadProducto(row['sku'])
            	self.data.setData(index, cantidad_producto)
            	index = self.data.index(r, 8, QtCore.QModelIndex())

            	self.data.setData(index, cantidad_producto*row['Precio'])
            self.ui.grilla_prod.setModel(self.data)

            self.ui.grilla_prod.setColumnWidth(0, 100)
            self.ui.grilla_prod.setColumnWidth(1, 150)
            self.ui.grilla_prod.setColumnWidth(2, 200)
            self.ui.grilla_prod.setColumnWidth(3, 100)
            self.ui.grilla_prod.setColumnWidth(4, 100)
            self.ui.grilla_prod.setColumnWidth(5, 200)
            self.ui.grilla_prod.setColumnWidth(6, 100)
            self.ui.grilla_prod.setColumnWidth(7, 100)
            self.ui.grilla_prod.setColumnWidth(8, 100)

    def onActivated_nombre(self, index1):

        nom = self.ui.combonombre.itemText(index1)
        if nom=="":
            self.load_data()
        else:
	        lista=[]
	        producto = db_model.producto_nom(nom)
	        lista.append(producto)
	        #Creamos el modelo asociado a la tabla
	        self.data = QtGui.QStandardItemModel(len(producto), 8)
	        self.data.setHorizontalHeaderItem(
	            0, QtGui.QStandardItem(u"ID"))
	        self.data.setHorizontalHeaderItem(
	            1, QtGui.QStandardItem(u"Nombre"))
	        self.data.setHorizontalHeaderItem(
	            2, QtGui.QStandardItem(u"Descripcion"))
	        self.data.setHorizontalHeaderItem(
	            3, QtGui.QStandardItem(u"Marca"))
	        self.data.setHorizontalHeaderItem(
	            4, QtGui.QStandardItem(u"Color"))
	        self.data.setHorizontalHeaderItem(
	            5, QtGui.QStandardItem(u"Imagen"))
	        self.data.setHorizontalHeaderItem(
	            6, QtGui.QStandardItem(u"Precio"))
	        self.data.setHorizontalHeaderItem(
	            7, QtGui.QStandardItem(u"Cantidad"))
	        self.data.setHorizontalHeaderItem(
	            8, QtGui.QStandardItem(u"Total"))
	        
	        cantidad_producto=0


	        for r, row in enumerate(producto):
	        	
	        	index = self.data.index(r, 0, QtCore.QModelIndex())
	        	self.data.setData(index, row['sku'])
	        	index = self.data.index(r, 1, QtCore.QModelIndex())
	        	self.data.setData(index, row['nombre'])
	        	index = self.data.index(r, 2, QtCore.QModelIndex())
	        	self.data.setData(index, row['descripcion'])
	        	index = self.data.index(r, 3, QtCore.QModelIndex())
	        	self.data.setData(index, row['marca'])
	        	index = self.data.index(r, 4, QtCore.QModelIndex())
	        	self.data.setData(index, row['color'])
	        	index = self.data.index(r, 5, QtCore.QModelIndex())
	        	self.data.setData(index, row['imagen'])
	        	index = self.data.index(r, 6, QtCore.QModelIndex())
	        	self.data.setData(index, row['Precio'])
	        	index = self.data.index(r, 7, QtCore.QModelIndex())
	        	cantidad_producto= db_model.obtener_CantidadProducto(row['sku'])
	        	self.data.setData(index, cantidad_producto)
	        	index = self.data.index(r, 8, QtCore.QModelIndex())
	        	self.data.setData(index, cantidad_producto*row['Precio'])
	        self.ui.grilla_prod.setModel(self.data)

	        self.ui.grilla_prod.setColumnWidth(0, 100)
	        self.ui.grilla_prod.setColumnWidth(1, 150)
	        self.ui.grilla_prod.setColumnWidth(2, 200)
	        self.ui.grilla_prod.setColumnWidth(3, 100)
	        self.ui.grilla_prod.setColumnWidth(4, 100)
	        self.ui.grilla_prod.setColumnWidth(5, 200)
	        self.ui.grilla_prod.setColumnWidth(6, 100)
	        self.ui.grilla_prod.setColumnWidth(7, 100)
	        self.ui.grilla_prod.setColumnWidth(8, 100)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main_Pro()
    sys.exit(app.exec_())