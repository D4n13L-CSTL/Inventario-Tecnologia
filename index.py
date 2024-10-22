from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import os
import modulotec
import mainmo
import search
import bcrypt
ancho = 1085
alto = 550


def buscar(event):
    def clean():
        for item in tree.get_children():
            tree.delete(item)
    clean()
    try:
        busq = search.search()
        busq.search(lista.get().upper())
        a = busq.data
        for i in a:
            tree.insert("", END, values=(i[0],i[1],i[2],i[3],i[4],i[5]))
    except sqlite3.OperationalError as error:
        messagebox.showerror("ERROR",f"Error {error}")

def filtrar(event):
    try:
        busq = search.search()
        busq.search(lista.get().upper())
        a = busq.data
        for row in tree.get_children(): #LIMPIA EL TREEW
                tree.delete(row)    
        for i in a:
            valor = "".join(f"{i[1]} {i[2]}")
            if entrada.get() in str(i[0]) or entrada.get().upper() in i[1] or entrada.get().upper() in i[2] or entrada.get().upper() in i[3] or entrada.get().upper() in i[4] or entrada.get().upper() in i[5] or entrada.get().upper() in valor:
                tree.insert("", END, values=(i[0],i[1],i[2],i[3],i[4],i[5]))
    except sqlite3.OperationalError as error:
        messagebox.showerror("ERROR",f"Error {error}")
      
def agregar():
    def eleccion():
        if lista.get() == elementos[1]:
            root_agg.destroy()
            tech = modulotec.add()
            tech.main(root_index,elementos[1], elementos[1].upper())
        elif lista.get() == elementos[2]:
            root_agg.destroy()
            rr = modulotec.add()
            rr.main(root_index,elementos[2], elementos[2].upper())
        elif lista.get() == elementos[3]:
            root_agg.destroy()
            pbl = modulotec.add()
            pbl.main(root_index,elementos[3], elementos[3].upper())
        elif lista.get() == elementos[4]:
            root_agg.destroy()
            inve = modulotec.add()
            inve.main(root_index,elementos[4], elementos[4].upper())
        elif lista.get() == elementos[5]:
            root_agg.destroy()
            admi = modulotec.add()
            admi.main(root_index,elementos[5], elementos[5].upper())
        elif lista.get() == elementos[6]:
            root_agg.destroy()
            cecom = modulotec.add()
            cecom.main(root_index,elementos[6], elementos[6].upper())
        elif lista.get() == elementos[7]:
            root_agg.destroy()
            ssl = modulotec.add()
            ssl.main(root_index,elementos[7], elementos[7].upper())
        elif lista.get() == elementos[8]:
            root_agg.destroy()
            cajas = modulotec.add()
            cajas.main(root_index,elementos[8], elementos[8].upper())
        
    alto_agg = 100
    ancho_agg = 285
    root_agg  = Toplevel(root_index)
    
    root_agg.geometry(f"{ancho_agg}x{alto_agg}+{((root_agg.winfo_screenwidth() // 2) - (ancho_agg  // 2))}+{((root_agg.winfo_screenheight() // 2)-(alto_agg  // 2))}")
    frame = Frame(root_agg)
    frame.place(x=50, y=10)
    Label(frame, text="Eliga el Dpto", font="bold").grid(row=0, column=0)
    elementos = ["Departamentos",
             "Tecnologia",
             "RRHH",
             "Publicidad",
             "Inventario",
             "Administracion",
             "CECOM",
             "Enfermeria",
             "Cajas"
             ]
    seleccion = StringVar()
    lista = ttk.Combobox(frame, values=elementos, textvariable=seleccion, state='readonly', font=("Arial", 12, "bold"), justify="center")
    lista.grid(row=1, column=0)
    lista.current(0)
    Button(frame, text="Aceptar",command=eleccion).grid(row=2, column=0, pady=10)

    root_agg.mainloop()

def actualizar():
    eleccion = tree.selection()
    if eleccion:
        for item_id in eleccion:
            item = tree.item(item_id)
            valores = item['values']
    try:  
        up = modulotec.update()
        up.main(root_index,f"{valores[1]} de {lista.get()}", valores[1],valores[2],valores[3],valores[4],valores[5], lista.get().upper(), valores[0])
    except UnboundLocalError :
        messagebox.showerror("ERROR",f"No has seleccionado ningun valor")

def eliminar():
    eleccion = tree.selection()
    if eleccion:
        for item_id in eleccion:
            item = tree.item(item_id)
            valores = item['values']
        a = messagebox.askyesno("BORRAR","Desea eliminar este valor")
        if a:
            cln = search.delete()
            cln.clear(valores[0], lista.get().upper())

def autenticacion(nombre):
    ventana = modulotec.auten()
    ventana.index(root_index, nombre)

def sistema(nombre):
    """sis = mainmo.sistema()
    sis.main(root_index)"""
    ventana = modulotec.auten()
    ventana.index(root_index, nombre)

def informacion():
    info = modulotec.construccion()
    info.informacion()

root_index = Tk()
barra_de_menu = Menu(root_index)
root_index.config(menu=barra_de_menu)
alto_pantalla = root_index.winfo_screenheight()
ancho_pantalla = root_index.winfo_screenwidth()

pos_x = (ancho_pantalla // 2) - (ancho // 2)
pos_y = (alto_pantalla // 2) - (alto // 2)

root_index.geometry(f"{ancho}x{alto}+{pos_x}+{pos_y}")
root_index.title("INVENTARIO")

Label(root_index,text="Inventario General de Tecnologia", font=("Arial",20,"bold")).place(x=385, y=10)

frame_inputs = Frame(root_index)
frame_inputs.place(x=150, y=80)

frame_btns = Frame(root_index)
frame_btns.place(x=350, y=480)

elementos = ["Departamentos",
             "Tecnologia",
             "RRHH",
             "Publicidad",
             "Inventario",
             "Administracion",
             "CECOM",
             "Enfermeria",
             "Cajas"
             ]

seleccion = StringVar()
lista = ttk.Combobox(frame_inputs, values=elementos, textvariable=seleccion, state='readonly', font=("Arial", 12, "bold"), justify="center")
lista.grid(row=0, column=0)
lista.current(0)

entrada = Entry(frame_inputs, width=50, font=("Arial", 12, "bold"))
entrada.grid(row=0, column=1, padx=15)

Button(frame_inputs, text="Buscar", width=15, command=lambda:buscar("<Return>")).grid(row=0, column=2)
Button(frame_inputs, text="Filtrar", width=15, command=lambda:filtrar("<Return>")).grid(row=0, column=3, padx=5)


tree = ttk.Treeview(frame_inputs, columns=("id", "DESCRIPCION", "MARCA", "MODELO", "SERIAL", "OBSERVACION"), show='headings', height=15)
tree.grid(row=1, column=0, columnspan=3, pady=20)

tree.heading("id", text="ID")
tree.heading("DESCRIPCION", text="DESCRIPCION")
tree.heading("MARCA",text="MARCA")
tree.heading("MODELO",text="MODELO")
tree.heading("SERIAL", text="SERIAL")
tree.heading("OBSERVACION",text="OBSERVACION")

tree.column("id", width=30)
tree.column("DESCRIPCION", width=125,anchor='center')
tree.column("MARCA", width=100, anchor='center')
tree.column("MODELO", width=120,anchor='center')
tree.column("SERIAL", width=120)
tree.column("OBSERVACION",width=250)

Button(frame_btns, text="Agregar", width=15, command=agregar).grid(row=0, column=0)
Button(frame_btns, text="Actualizar", width=15, command=actualizar).grid(row=0, column=1, padx=25)
Button(frame_btns, text="Borrar", width=15, command=eliminar).grid(row=0, column=2)

#-----MENU-----#

internet=Menu(barra_de_menu, tearoff=0)
internet.add_command(label="Consumibles", command=informacion)
internet.add_command(label="POS", command=informacion)


date = Menu(barra_de_menu, tearoff=0)
date.add_command(label="AnyDesk", command=lambda:autenticacion("anydesk"))
date.add_command(label="Sistema", command=lambda:sistema("sistema"))

serial = Menu(barra_de_menu, tearoff=0)
serial.add_command(label="Generar QR", command=informacion)
serial.add_command(label="Generar Serial", command=informacion)

barra_de_menu.add_cascade(label="Reportes", menu=internet)
barra_de_menu.add_cascade(label="Datos", menu=date)
barra_de_menu.add_cascade(label="Codigos", menu=serial)

root_index.bind("<Return>",buscar)
root_index.bind("<Return>",filtrar)

root_index.mainloop()

