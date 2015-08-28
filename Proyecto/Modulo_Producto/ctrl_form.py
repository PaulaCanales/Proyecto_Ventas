# -*- coding: utf-8 -*-

from PySide import QtGui
from ui_Form_Pro import Ui_Form
import model

class FormProducto(QtGui.QDialog):

    def __init__(self, parent=None, sku=None):
        """
        Formulario para crear y editar alumnos.
        Si se recibe la var rut
        entonces se está en modo de edición.
        """
        super(FormProducto, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        if sku is None:
            self.ui.agregar.clicked.connect(self.crear_producto)
        else:
            self.colocar_datos(sku)
            self.ui.agregar.clicked.connect(self.editar_producto)

    def colocar_datos(self, sku):
        """
        Coloca los datos del alumno en los widgets
        para su edición
        """
        producto = model.producto_sku(sku)
        self.ui.id.setText(str(producto["sku"]))
        self.ui.nombre.setText(producto["nombre"])
        self.ui.descripcion.setText(producto["descripcion"])
        self.ui.marca.setText(producto["marca"])
        self.ui.color.setText(producto["color"])
        self.ui.imagen.setText(producto["imagen"])
        self.ui.precio.setText(str(producto["Precio"]))
        self.ui.id.setEnabled(False)

    def obtener_datos(self):
        """
        Obtiene los datos colocados por el usuario
        en el formulario
        """
        sku = int(self.ui.id.text())
        nombres = self.ui.nombre.text()
        marca = self.ui.marca.text()
        color = self.ui.color.text()
        imagen = self.ui.imagen.text()
        precio = int(self.ui.precio.text())
        descripcion = self.ui.descripcion.toPlainText()
        return (sku, nombres, descripcion, marca, color, imagen, precio)

    def crear_producto(self):
        sku, nombres, descripcion, marca, color, imagen, precio = self.obtener_datos()
        try:
            model.crear_producto(sku, nombres, descripcion, marca, color, imagen, precio)
            self.accepted.emit()
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"El producto ha sido creado.")
            msgBox.exec_()
            self.close()
        except:
            #Tratar errores!!!!!!
            pass

    def editar_producto(self):
        sku, nombres, descripcion, marca, color, imagen, precio = self.obtener_datos()
        try:
            model.editar_producto(sku, nombres, descripcion, marca, color, imagen, precio)# Invocar la función del modelo que permite editar
            self.accepted.emit()
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"El producto ha sido editado.")
            msgBox.exec_()
            self.close()
        except:
            #Tratar errores!!!!!!
            pass
