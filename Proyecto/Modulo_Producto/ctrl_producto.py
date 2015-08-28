#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ctrl_form import FormProducto
from ui_Productos import Ui_Productos
import model as db_model


class Main(QtGui.QWidget):
    """
    Esta es una grilla y un buscador
    """
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Productos()
        self.ui.setupUi(self)

        self.load_data()
        self.connect_signals()
        self.filtrar()
        self.ui.combosku.activated[int].connect(self.onActivated)
        self.show()

    def connect_signals(self):
        self.ui.agregar.clicked.connect(self.agrega)
        self.ui.eliminar.clicked.connect(self.elimina)
        self.ui.editar.clicked.connect(self.edita)

    def agrega(self):
        self.ui.form = FormProducto(self)
        self.ui.form.accepted.connect(self.load_data)
        self.ui.form.show()

    def load_data(self):
        """
        Función que carga la información de alumnos en la grilla
        """
        producto = db_model.obtener_producto()
        #Creamos el modelo asociado a la tabla
        self.data = QtGui.QStandardItemModel(len(producto), 6)
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
        self.ui.grilla_prod.setColumnWidth(4, 220)
        self.ui.grilla_prod.setColumnWidth(5, 220)
        self.ui.grilla_prod.setColumnWidth(6, 220)

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
            sku = data.index(index.row(), 0, QtCore.QModelIndex()).data()
            if (db_model.borrar(sku)):
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

    def edita(self):
        """
        Función obtiene el alumno seleccionado en la grilla
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

    def filtrar(self):
        """
        Funcion que agrega todos los sku y nombre al combobox y luego filtra.
        """
        sku= db_model.obtener_sku()
        for dato in range(len(sku)):
            self.ui.combosku.addItem(str(sku[dato][0]))

        nombre= db_model.obtener_nombre()
        for dato in range(len(nombre)):
            self.ui.combonombre.addItem(str(nombre[dato][0]))


    def onActivated(self, index):
        sku = self.ui.combosku.itemText(index)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())