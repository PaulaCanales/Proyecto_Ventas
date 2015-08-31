# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    """
    Se conecta a la base de datos
    """
    con = sqlite3.connect('usuario.db')
    con.row_factory = sqlite3.Row
    return con

def obtener_usuario():
	"""
	Obtener nombre de usuario 
	"""
	con = conectar()
	c = con.cursor()
	query = "SELECT name FROM usuario"
	resultado = c.execute(query)
	user = resultado.fetchall()
	con.close()
	return user[0]

def obtener_pass():
	"""
	Obtener contraseña
	"""
	con = conectar()
	c = con.cursor()
	query = "SELECT pass FROM usuario"
	resultado = c.execute(query)
	pas = resultado.fetchall()
	con.close()
	return pas[0]