#!/usr/bin/python
# -*- coding: utf-8 -*-

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

def obtener_sku():
    """
    Para combobox con productos. para filtro por producto
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT sku FROM producto "
    resultado = c.execute(query)
    producto = resultado.fetchall()
    con.close()
    return producto[0]

def venta_folio(sku):
    """
    Para filtrar las ventas segun folio
    """
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM venta WHERE folio = ?"
    resultado = c.execute(query, [sku])
    ventas = resultado.fetchone()
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
    fecha= today.date()
    c.execute(sql, (folio, rut, fecha))
    con.commit()

def agregar_venta(folio, sku, cantidad, precio):
    """
    Cuando se apreta el boton agregar, se agrega al detalle
    """
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO detalle (venta_folio, producto_sku, cantidad, precio_unitario, total)"
        "VALUES (?,?,?,?,?)")
    total=cantidad*precio_unitario
    c.execute(sql, (folio, sku, cantidad, precio, total))
    con.commit()

def editar_venta(folio, cliente_rut, cantidad, precio_unitario):
    """
    Se edita la tabla de detalle.
    """
    con=conectar()
    c = con.cursor()
    sql=(
        "UPDATE detalle SET cantidad=?, precio_unitario=?, total=? WHERE venta_folio=?, cliente_rut=? ")
    total= precio_unitario*cantidad
    c.execute(sql, [cantidad, precio_unitario, total, folio, cliente_rut])
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

