#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import date
import sqlite3

def conectar():
    con = sqlite3.connect('../SistemaVentas.db')
    con.row_factory = sqlite3.Row
    return con


def obtener_ventas():
    """
    Desplegar en la tabla grande
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM venta"
    resultado = c.execute(query)
    ventas = resultado.fetchall()
    con.close()
    return ventas

def obtener_ventas_formulario(folio):
    """
    Desplegar en la tabla formulario
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM detalle WHERE venta_folio=?"
    resultado = c.execute(query, [folio])
    ventas = resultado.fetchall()
    con.close()
    return ventas

def obtener_folio():
    """
    Se obtienen todos los Folios para el combobox
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT folio FROM venta "
    resultado = c.execute(query)
    ventas = resultado.fetchall()
    con.close()
    return ventas
    
def filtrar_producto(sku):
    """
    Para combobox con productos, busqueda de ventas asociadas
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT folio, cliente_rut, fecha FROM detalle, venta WHERE producto_sku =? and venta_folio=folio"
    resultado = c.execute(query, [sku])
    ventas = resultado.fetchall()
    con.close()
    return ventas

def obtener_producto():
    """
    Para combobox con productos. para filtro por producto
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT sku FROM producto "
    resultado = c.execute(query)
    producto = resultado.fetchall()
    con.close()
    return producto

def obtener_rut():
    """
    Para combobox con rut de clientes, en el formulario
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT rut FROM cliente "
    resultado = c.execute(query)
    cliente = resultado.fetchall()
    con.close()
    return cliente

def obtener_idprod():
    """
    Para combobox con rut de clientes, en el formulario
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT sku FROM producto "
    resultado = c.execute(query)
    producto = resultado.fetchall()
    con.close()
    return producto

def obtener_cliente(cliente_rut):
    """
    Para combobox con rut de clientes, en el formulario
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM venta WHERE cliente_rut =?"
    resultado = c.execute(query, [cliente_rut])
    cliente = resultado.fetchall()
    con.close()
    return cliente

def obtener_precio(sku):
    con = conectar()
    c = con.cursor()
    query = "SELECT Precio FROM producto WHERE sku = ?"
    resultado = c.execute(query, [sku])
    producto = resultado.fetchone()
    con.close()
    return producto[0]

def filtrar_fecha(fecha):
    """
    Para combobox con fecha de ventas que filtra 
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM venta WHERE fecha =?"
    resultado = c.execute(query, [fecha])
    ventas = resultado.fetchall()
    con.close()
    return ventas

def venta_folio(fol):
    """
    Para filtrar las ventas segun folio
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM venta WHERE folio =?"
    resultado = c.execute(query, [int(fol)])
    ventas = resultado.fetchall()
    con.close()
    return ventas

def venta_fecha(nombre):
    """
    Se obtienen todas las ventas de la fecha.
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM venta WHERE fecha =? "
    resultado = c.execute(query, [nombre])
    ventas = resultado.fetchone()
    con.close()
    return ventas

def crear_venta(folio, rut):
    """
    Cuando se apreta el boton Terminar venta
    """
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO venta (folio,cliente_rut, fecha)"
        "VALUES (?,?,?)")
    fecha= date.today()
    c.execute(sql, (folio, rut, fecha))
    con.commit()

def agregar_venta(folio, sku, cantidad, precio):
    """
    Cuando se apreta el boton agregar, se agrega al detalle
    """
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO detalle (venta_folio, producto_sku, cantidad, precio_unitario, total) VALUES (?,?,?,?,?)")
    total=cantidad*precio
    c.execute(sql, (folio, sku, cantidad, precio, total))
    con.commit()

def editar_venta(folio, producto_sku, cantidad, precio_unitario):
    """
    Se edita la tabla de detalle.
    """
    con=conectar()
    c = con.cursor()
    sql=(
        "UPDATE detalle SET cantidad=?, precio_unitario=?, total=? WHERE venta_folio=? and producto_sku=? ")
    total= precio_unitario*cantidad
    c.execute(sql, [cantidad,precio_unitario, total, folio, producto_sku])
    con.commit()

def borrar(folio):
    """
    Elimina una venta, eliminado en detalle y venta
    """
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM detalle WHERE venta_folio = ?"
    sql = "DELETE FROM venta WHERE folio=? "
    try:
        resultado = c.execute(query, [folio])
        resultado = c.execute(sql, [folio])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito


def obtener_total_Venta(folio):
    """
    Para obtener el total de la venta
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT SUM(total) FROM detalle WHERE venta_folio = ?"
    resultado = c.execute(query, [folio])
    venta = resultado.fetchone()
    con.close()
    if venta[0]==None:
        return 0
    else: 
        return venta[0]

