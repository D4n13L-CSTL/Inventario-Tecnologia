
import sqlite3

#FUNCION PARA CREAR TABLAS

def creacion_de_tablas():
    conexion = sqlite3.connect("DataBase.db")
    poiter = conexion.cursor()
    poiter.execute('''
            CREATE TABLE TECNOLOGIA(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DESCRIPCION TEXT NOT NULL,
            MARCA TEXT NOT NULL,
            MODELO TEXT NOT NULL,
            SERIAL TEXT NOT NULL,
            OBSERVACION TEXT
            )''')
    
    poiter.execute('''
            CREATE TABLE RRHH(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DESCRIPCION TEXT NOT NULL,
            MARCA TEXT NOT NULL,
            MODELO TEXT NOT NULL,
            SERIAL TEXT NOT NULL,
            OBSERVACION TEXT
            )''')
    poiter.execute('''
            CREATE TABLE PUBLICIDAD(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DESCRIPCION TEXT NOT NULL,
            MARCA TEXT NOT NULL,
            MODELO TEXT NOT NULL,
            SERIAL TEXT NOT NULL,
            OBSERVACION TEXT
            )''')
    
    poiter.execute('''
            CREATE TABLE INVENTARIO(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DESCRIPCION TEXT NOT NULL,
            MARCA TEXT NOT NULL,
            MODELO TEXT NOT NULL,
            SERIAL TEXT NOT NULL,
            OBSERVACION TEXT
            )''')
    
    poiter.execute('''
            CREATE TABLE ADMINISTRACION(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DESCRIPCION TEXT NOT NULL,
            MARCA TEXT NOT NULL,
            MODELO TEXT NOT NULL,
            SERIAL TEXT NOT NULL,
            OBSERVACION TEXT
            )''')

    poiter.execute('''
            CREATE TABLE CECOM(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DESCRIPCION TEXT NOT NULL,
            MARCA TEXT NOT NULL,
            MODELO TEXT NOT NULL,
            SERIAL TEXT NOT NULL,
            OBSERVACION TEXT
            )''')
    
    poiter.execute('''
            CREATE TABLE ENFERMERIA(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DESCRIPCION TEXT NOT NULL,
            MARCA TEXT NOT NULL,
            MODELO TEXT NOT NULL,
            SERIAL TEXT NOT NULL,
            OBSERVACION TEXT
            )''')
    
    poiter.execute('''
            CREATE TABLE CAJAS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DESCRIPCION TEXT NOT NULL,
            MARCA TEXT NOT NULL,
            MODELO TEXT NOT NULL,
            SERIAL TEXT NOT NULL,
            OBSERVACION TEXT
            )''')
    
    conexion.close()





creacion_de_tablas()