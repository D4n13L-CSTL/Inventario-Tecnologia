import sqlite3
from tkinter import ttk, messagebox
import os
import sys



#CLASES DE INTERACION CON LA BASE DE DATOS
def ruta(relativa):
        if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relativa)
        return os.path.join(os.path.abspath("."), relativa)

class search:
        def search(self,name):
                self.conexion = sqlite3.connect(ruta("DataBase/Database.db"))
                self.pointer = self.conexion.cursor()
                self.pointer.execute(f"SELECT * FROM {name}")
                self.data = self.pointer.fetchall()
                self.conexion.commit()
                self.conexion.close()

class delete:
        def clear(self,id,name):
                self.conexion = sqlite3.connect(ruta("DataBase/Database.db"))
                self.pointer = self.conexion.cursor()
                self.pointer.execute(f"DELETE FROM {name} WHERE ID =?",(id,))
                self.data = self.pointer.fetchall()
                self.conexion.commit()
                self.conexion.close()
                messagebox.showinfo("DELETE","Valor eliminado")

class deleteAny: #Borrar daato de AnyDesk
        def clear(self,name,nombre):
                self.conexion = sqlite3.connect(ruta("DataBase/Database.db"))
                self.pointer = self.conexion.cursor()
                self.pointer.execute(f"DELETE FROM {name} WHERE NOMBRE =?",(nombre,))                
                self.conexion.commit()
                self.conexion.close()
                messagebox.showinfo("DELETE","Valor eliminado")


class senam: #Search Name #CONSULTA PARA USUARIO
        def consu(self,user):
                self.conexion = sqlite3.connect(ruta("DataBase/Database.db"))
                self.pointer = self.conexion.cursor()
                self.pointer.execute(f"SELECT PASS FROM USERS WHERE NAME = ?",(user,))
                self.data = self.pointer.fetchone()
                self.conexion.close()


class searchAny: #Consulta para Anydesk
        def query(self):
                self.conexion = sqlite3.connect(ruta("DataBase/Database.db"))
                self.pointer = self.conexion.cursor()
                self.pointer.execute(f"SELECT * FROM ANYDESK")
                self.data = self.pointer.fetchall()
                self.conexion.close()



class updateAny:
        def query(self, name,dire,clave,n):
                self.conexion = sqlite3.connect(ruta("DataBase/Database.db"))
                self.pointer = self.conexion.cursor()
                self.pointer.execute(f"UPDATE ANYDESK SET NOMBRE = ?, DIRECCION = ?, CLAVE = ? WHERE DIRECCION = ?", (name, dire, clave, n))
                self.conexion.commit()
                self.conexion.close()
                