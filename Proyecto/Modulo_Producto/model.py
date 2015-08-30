#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def conectar():
    con = sqlite3.connect('SistemaVentas.db')
    con.row_factory = sqlite3.Row
    return con


def obtener_producto():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM producto"
    resultado = c.execute(query)
    producto = resultado.fetchall()
    con.close()
    return producto

def obtener_sku():
    con = conectar()
    c = con.cursor()
    query = "SELECT sku FROM producto "
    resultado = c.execute(query)
    producto = resultado.fetchall()
    con.close()
    return producto

def obtener_nombre():
    con = conectar()
    c = con.cursor()
    query = "SELECT nombre FROM producto "
    resultado = c.execute(query)
    producto = resultado.fetchall()
    con.close()
    return producto

def producto_sku(sku):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM producto WHERE sku = ?"
    resultado = c.execute(query, [sku])
    producto = resultado.fetchone()
    con.close()
    return producto

def producto_nom(nombre):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM producto WHERE nombre = ?"
    resultado = c.execute(query, [nombre])
    producto = resultado.fetchone()
    con.close()
    return producto

def crear_producto(sku, nombre, descripcion, marca, color, imagen, Precio):
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO producto (sku, nombre, descripcion, marca, color, imagen, Precio)"
        "VALUES (?, ?, ?, ?, ?, ?, ?)")
    c.execute(sql, (sku, nombre, descripcion, marca, color, imagen, Precio))
    con.commit()

def editar_producto(sku, nombre,descripcion,marca,color,imagen,Precio):
    con=conectar()
    c = con.cursor()
    sql=(
        "UPDATE producto SET nombre=?, descripcion=?,marca=?,color=?,imagen=?,Precio=? WHERE sku=?")
    c.execute(sql, [nombre, descripcion, marca, color, imagen, Precio,sku])
    con.commit()

def borrar(sku):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM producto WHERE sku = ?"
    try:
        resultado = c.execute(query, [sku])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def eliminar_revision(sku):
    con = conectar()
    c = con.cursor()
    query = "SELECT COUNT(producto_sku) FROM detalle WHERE producto_sku = ?"
    resultado = c.execute(query, [sku])
    prod_esta = resultado.fetchone()
    con.close()
    if prod_esta[0]==0:
        return True #se puede eliminar
    else:
        return False #no se puede eliminar.

def obtener_TotalProducto(sku):
    con = conectar()
    c = con.cursor()
    query = "SELECT COUNT(producto_sku) FROM detalle WHERE producto_sku = ?"
    resultado = c.execute(query, [sku])
    producto = resultado.fetchone()
    con.close()
    return producto[0]

def obtener_CantidadProducto(sku):
    con = conectar()
    c = con.cursor()
    query = "SELECT SUM(cantidad) FROM detalle WHERE producto_sku = ?"
    resultado = c.execute(query, [sku])
    producto = resultado.fetchone()
    con.close()
    if producto[0]==None:
        return 0
    else: 
        return producto[0]
