#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def conectar():
    con = sqlite3.connect('../SistemaVentas.db')
    con.row_factory = sqlite3.Row
    return con


def obtener_rut():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM cliente"
    resultado = c.execute(query)
    rut = resultado.fetchall()
    con.close()
    return rut


def obtener_nombre(rut):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM cliente WHERE rut = ?"
    resultado = c.execute(query, [rut])
    nombre = resultado.fetchone()
    con.close()
    return nombre

def obtener_TotalVenta(rut):
    con = conectar()
    c = con.cursor()
    query = "SELECT COUNT(cliente_rut) FROM venta WHERE cliente_rut = ?"
    resultado = c.execute(query, [rut])
    nombre = resultado.fetchone()
    con.close()
    return nombre[0]

def obtener_TotalIngreso(rut):
    con = conectar()
    c = con.cursor()
    query = "SELECT SUM(total) FROM cliente,detalle,venta WHERE rut = cliente_rut and folio=venta_folio and rut=?"
    resultado = c.execute(query, [rut])
    nombre = resultado.fetchone()
    con.close()
    return nombre[0]

def crear_cliente(rut, nombres, apellidos, correo=None):
    con = conectar()
    c = con.cursor()
    sql = (
        "INSERT INTO cliente (rut, nombres, apellidos, correo)"
        "VALUES (?, ?, ?, ?)")
    c.execute(sql, (rut, nombres, apellidos, correo))
    con.commit()

def editar_cliente(rut,nombres,apellidos,correo): 
    con=conectar() 
    c = con.cursor() 
    sql=( "UPDATE cliente SET nombres=?, apellidos=?,correo=? WHERE rut=?")
    c.execute(sql, [nombres, apellidos,correo,rut]) 
    con.commit()

def borrar(rut):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM cliente WHERE rut = ?"
    try:
        resultado = c.execute(query, [rut])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

