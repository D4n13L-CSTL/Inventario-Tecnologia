from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import os
import sys
from search import senam, searchAny, deleteAny, updateAny
import bcrypt
import time

#CAPTURAR LAS ACTUALIZACION Y LOS ERRORES 

def ruta(relativa):
        if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relativa)
        return os.path.join(os.path.abspath("."), relativa)

#VENTANA DE LOGIN
class auten:
    def verif(self,event,master,name):
        self.login = False
        self.busque = senam()
        self.busque.consu(self.user_input.get().upper())
        self.a = self.busque.data
        if name == "anydesk":
            if self.a:
                password = self.a[0]
                if bcrypt.checkpw(self.pass_input.get().encode('utf-8') , password):
                    self.root.after(1000, self.root.destroy())    
                    ventan = anysis()
                    ventan.main(master)
                else:
                    messagebox.showerror("ERROR","Contraseña incorrecta")
            else:
                messagebox.showerror("Error",f"El usario {self.user_input.get()} no existe")
        elif name == "sistema":
            messagebox.showinfo("Sistema","Sistema en construccion")
    def index(self,master,cn):
        self.fuente = ("Arial", 12, "bold")
        self.alto = 400
        self.ancho = 350

        self.root =Toplevel(master)
        self.root.grab_set()
        self.root.geometry(f"{self.ancho}x{self.alto}+{((self.root.winfo_screenwidth() // 2) - (self.ancho // 2))}+{((self.root.winfo_screenheight() // 2) - (self.alto // 2))}")
        self.frame1 = Frame(self.root)
        self.frame1.place(x=130, y=10)

        Label(self.frame1, text=f"Verificacion {cn}", font=self.fuente).grid(row=0, column=0)

        self.frame2 = Frame(self.root)
        self.frame2.place(x=80, y=50)

        
        Label(self.frame2, text="User", font=self.fuente).grid(row=0, column=0, sticky='w')
        self.user_input = Entry(self.frame2, width=20, font="bold")
        self.user_input.grid(row=1, column=0, pady=15)

        Label(self.frame2, text="Pass", font=self.fuente).grid(row=2, column=0, sticky='w')
        self.pass_input = Entry(self.frame2, width=20, font="bold", show="*")
        self.pass_input.grid(row=3, column=0, pady=15)

        Button(self.frame2, text="Enviar", width=15, font="bold", command=lambda:self.verif("<Return>",master, cn)).grid(row=4, column=0, pady=15)
        
        self.root.bind("<Return>", lambda event:self.verif("<Return>",master, cn))

        self.root.mainloop()

class construccion:
    def informacion(self):
        info = messagebox.showinfo("INFO","En construccion")

class add:
    def registro(self,name): 
        self.descripcion = self.input_des.get().upper()
        self.marca = self.input_mark.get().upper()
        self.moodelo = self.input_model.get().upper()
        self.serial = self.input_serial.get().upper()
        self.observ = self.observacion.get("1.0", END)

        self.conexion = sqlite3.connect(ruta("DataBase/Database.db"))
        self.pointer = self.conexion.cursor()
        self.pointer.execute(f"INSERT INTO {name} (DESCRIPCION, MARCA, MODELO, SERIAL,OBSERVACION ) VALUES (?,?,?,?,?)",(self.descripcion, self.marca, self.moodelo, self.serial, self.observ))
        self.conexion.commit()
        self.conexion.close()

        messagebox.showinfo("Registro","Se registro Correctamente")

        self.var_descri.set("")
        self.var_mark.set("")
        self.var_model.set("")
        self.var_serial.set("")
        self.observacion.delete("1.0", "end")

    def main(self, master,titulo, bd):       
        self.fuente_label = ("Arial", 12, "bold")
        self.fuente_entry = ("Arial" , 15, "bold")
        self.alto = 550
        self.ancho = 800
        self.root = Toplevel(master)
        self.root.title(f"Registro de {titulo}")
        self.root.grab_set()
        self.root.geometry(f"{self.ancho}x{self.alto}+{((self.root.winfo_screenwidth() // 2) - (self.ancho  // 2))}+{((self.root.winfo_screenheight() // 2)-(self.alto  // 2))}")
        self.frame = Frame(self.root)
        self.frame.place(x=130, y=50)

        Label(self.root, text=f"Registro De {titulo}", font=self.fuente_label).place(x=300, y=10)
        Label(self.frame, text="Descripcion", font=self.fuente_label).grid(row=0, column=0, sticky='w')
        self.var_descri = StringVar()
        self.input_des = Entry(self.frame, font=self.fuente_entry, width=50, textvariable=self.var_descri)
        self.input_des.grid(row=1, column=0, pady=5)

        Label(self.frame, text="Marca", font=self.fuente_label).grid(row=2, column=0, sticky='w')
        self.var_mark = StringVar()
        self.input_mark = Entry(self.frame, width=50, font=self.fuente_entry, textvariable=self.var_mark)
        self.input_mark.grid(row=3, column=0, pady=5)

        Label(self.frame, text="Modelo", font=self.fuente_label).grid(row=4, column=0,sticky='w')
        self.var_model = StringVar()
        self.input_model = Entry(self.frame, width=50, font=self.fuente_entry, textvariable=self.var_model)
        self.input_model.grid(row=5, column=0, pady=5)

        Label(self.frame, text="Serial", font=self.fuente_label).grid(row=6, column=0,sticky='w')
        self.var_serial = StringVar()
        self.input_serial = Entry(self.frame, width=50, font=self.fuente_entry, textvariable=self.var_serial)
        self.input_serial.grid(row=7, column=0, pady=5)

        Label(self.frame,text="Observacion", font=self.fuente_label).grid(row=10, column=0, sticky='w')
        self.observacion = Text(self.frame, height=5, width=60)
        self.observacion.grid(row=11, column=0)
        Button(self.frame, text="Registrar", font="bold", command=lambda:self.registro(bd) , width=20).grid(row=12, column=0, pady=11)

        self.root.mainloop()


class update:

    def actualizar(self, name, id):
        self.conexion = sqlite3.connect(ruta("DataBase/Database.db"))
        self.pointer = self.conexion.cursor()
        self.pointer.execute(f"UPDATE {name} SET DESCRIPCION = ?, MARCA = ?, MODELO = ?, SERIAL = ?, OBSERVACION = ? WHERE ID = ?",(self.input_des.get().upper(),self.input_mark.get().upper(),self.input_model.get().upper(),self.input_serial.get().upper(),self.observacion.get("1.0", END),id ))
        self.conexion.commit()
        self.conexion.close()
        messagebox.showinfo("UPDATE","Actualizacion Exitosa")


    def main(self,master,titulo, v1, v2, v3, v4, v5, bd, idet):
        self.fuente_label = ("Arial", 12, "bold")
        self.fuente_entry = ("Arial" , 15, "bold")
        self.alto = 550
        self.ancho = 800
        self.root = Toplevel(master)
        self.root.title(f"Actualizacion")
        self.root.grab_set()
        self.root.geometry(f"{self.ancho}x{self.alto}+{((self.root.winfo_screenwidth() // 2) - (self.ancho  // 2))}+{((self.root.winfo_screenheight() // 2)-(self.alto  // 2))}")
        self.frame = Frame(self.root)
        self.frame.place(x=130, y=50)

        Label(self.root, text=f"Actualizacion De {titulo}", font=self.fuente_label).place(x=300, y=10)
        Label(self.frame, text="Descripcion", font=self.fuente_label).grid(row=0, column=0, sticky='w')
        self.var_descri = StringVar()
        self.input_des = Entry(self.frame, font=self.fuente_entry, width=50, textvariable=self.var_descri)
        self.input_des.grid(row=1, column=0, pady=5)

        Label(self.frame, text="Marca", font=self.fuente_label).grid(row=2, column=0, sticky='w')
        self.var_mark = StringVar()
        self.input_mark = Entry(self.frame, width=50, font=self.fuente_entry, textvariable=self.var_mark)
        self.input_mark.grid(row=3, column=0, pady=5)

        Label(self.frame, text="Modelo", font=self.fuente_label).grid(row=4, column=0,sticky='w')
        self.var_model = StringVar()
        self.input_model = Entry(self.frame, width=50, font=self.fuente_entry, textvariable=self.var_model)
        self.input_model.grid(row=5, column=0, pady=5)

        Label(self.frame, text="Serial", font=self.fuente_label).grid(row=6, column=0,sticky='w')
        self.var_serial = StringVar()
        self.input_serial = Entry(self.frame, width=50, font=self.fuente_entry, textvariable=self.var_serial)
        self.input_serial.grid(row=7, column=0, pady=5)

        Label(self.frame,text="Observacion", font=self.fuente_label).grid(row=10, column=0, sticky='w')
        self.observacion = Text(self.frame, height=5, width=60)
        self.observacion.grid(row=11, column=0)
        Button(self.frame, text="Actualizar", font="bold", command=lambda:self.actualizar(bd, idet) , width=20).grid(row=12, column=0, pady=11)

        self.var_descri.set(v1)
        self.var_mark.set(v2)
        self.var_model.set(v3)
        self.var_serial.set(v4)
        self.observacion.insert("1.0",v5)
        
        self.root.mainloop()

#VENTANA DE ANYDESKS
class anysis:
    ancho_a = 450
    alto_a = 80
    def actualiza(self,master):
        self.conexion = sqlite3.connect(ruta("DataBase/Database.db"))
        self.pointer = self.conexion.cursor()
        self.pointer.execute(f"UPDATE ANYDESK SET NOMBRE = ?, DIRECCION = ?, CLAVE = ? WHERE ID = ?",(self.name.get(), self.dire.get(), self.paso.get(), self.valor[0]))
        self.conexion.commit()
        self.conexion.close()
        self.root_up.destroy()
        messagebox.showinfo("UPDATE","Actualizacion con exito")
        self.root.destroy()
        self.main(master)

        
    def editar(self, master):
        self.seleccion = self.tree.selection()
        if self.seleccion:
            for self.fila in self.seleccion:
                self.po = self.tree.item(self.fila)
                self.valor = self.po['values']
        self.root_up = Toplevel(self.root)
        self.root_up.geometry(f"{self.ancho_a}x{self.alto_a}+{((self.root_up.winfo_screenwidth() // 2) - (self.ancho_a // 2))}+{((self.root_up.winfo_screenheight() // 2) - (self.alto_a // 2))}")

        self.root_up.grab_set()


        self.frame_s = Frame(self.root_up)
        self.frame_s.place(x=30, y=20)

        self.name_var = StringVar()
        self.name = Entry(self.frame_s, textvariable=self.name_var)
        self.name.grid(row=0, column=0)

        self.dire_var = StringVar()
        self.dire = Entry(self.frame_s, textvariable=self.dire_var)
        self.dire.grid(row=0, column=1, padx=10)

        self.paso_var = StringVar()
        self.paso = Entry(self.frame_s, textvariable=self.paso_var)
        self.paso.grid(row=0, column=2)
        try:
            self.name_var.set(self.valor[1])
            self.dire_var.set(self.valor[2])
            self.paso_var.set(self.valor[3])
        except AttributeError:
            messagebox.showerror("Error","No has seleccionado un valor")
        
        Button(self.frame_s, text="Aceptar", command=lambda:self.actualiza(master)).grid(row=1, column=0, columnspan=3, pady=5)
        
    

        self.root_up.mainloop()


    def eliminar(self):
        self.eleccion = self.tree.selection()
        if self.eleccion:
            for self.item_id in self.eleccion:
                self.item = self.tree.item(self.item_id)
                valores = self.item['values']
        ask = messagebox.askyesno("Eliminar","Desea eliminar valor")
        if ask:
            clean = deleteAny()
            clean.clear("ANYDESK",valores[0])
            self.root.destroy()
            self.main()

    def filtrar(self, event):
        self.otra = self.data
        for row in self.tree.get_children():
            self.tree.delete(row)
        for self.i in self.otra:
            if self.filtro_input.get().upper() in str(self.i[0]) or self.filtro_input.get().upper() in str(self.i[1]) or self.filtro_input.get().upper() in str(self.i[2]) or self.filtro_input.get().upper() in str(self.i[3]):
                self.tree.insert("",END,values=(self.i[0], self.i[1],self.i[2], self.i[3]))

    def main(self, master):
        self.ancho = 850
        self.alto = 500
        """self.root = Tk()"""
        self.root = Toplevel(master)
        self.root.title("AnyDesk")
        self.root.grab_set()
        self.root.geometry(f"{self.ancho}x{self.alto}+{((self.root.winfo_screenwidth() // 2) - (self.ancho // 2))}+{((self.root.winfo_screenheight() // 2)-(self.alto // 2))}")

        self.frame = Frame(self.root)
        self.frame.place(x=130, y=100)

        self.frame_input = Frame(self.root)
        self.frame_input.place(x=80, y=30)

        Label(self.root, text="Listado de AnyDesk", font=("Arial",15, "bold")).place(x=290, y=5)

        Label(self.frame_input, text="Buscar", font="bold").grid(row=0, column=0, sticky='w')
        self.filtro_input = Entry(self.frame_input, width=50, font=("Arial",10,"bold"))
        self.filtro_input.grid(row=1, column=0)

        Button(self.frame_input, text="Buscar", command=lambda:self.filtrar("<Retunr>"), width=15).grid(row=1, column=1, padx=10)
        Button(self.frame_input, text="Editar", width=15, command=lambda:self.editar(master)).grid(row=1, column=2)
        Button(self.frame_input, text="Elminar", width=15, command=self.eliminar).grid(row=1, column=3, padx=10)
        

        self.tree = ttk.Treeview(self.frame, columns=("ID","NOMBRE","DIRECCION","CLAVE"), show='headings', height=15)
        self.tree.grid(row=0, column=0, pady=10)

        self.tree.heading("ID",text="ID")
        self.tree.heading("NOMBRE", text="NOMBRE")
        self.tree.heading("DIRECCION", text="DIRECCION")
        self.tree.heading("CLAVE", text="CLAVE")

        self.tree.column("ID",anchor='center', width=20)
        self.tree.column("NOMBRE", anchor='center')
        self.tree.column("DIRECCION" ,anchor='center')
        self.tree.column("CLAVE", anchor='center')

        
        self.query = searchAny()
        self.query.query()
        self.data = self.query.data
        for self.i in self.data:
            self.tree.insert("",END,values=(self.i[0], self.i[1], self.i[2],self.i[3]))
        self.root.bind("<Return>",self.filtrar)
        self.root.mainloop()

