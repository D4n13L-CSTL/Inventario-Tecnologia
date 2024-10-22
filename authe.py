from tkinter import *
from tkinter import ttk, messagebox
import bcrypt
from search import senam
from modulotec import anysis


#VENTANA DE LOGIN
class auten:
    
    def verif(self,master):
        self.login = False
        self.busque = senam()
        self.busque.consu(self.user_input.get())
        self.a = self.busque.data
        

        if self.a:
            password = self.a[0]
            if bcrypt.checkpw(self.pass_input.get().encode('utf-8'), password):
                self.root.destroy()
                users_any = anysis()
                users_any.main(master)
                
               
            else:
                messagebox.showerror("ERROR","Contraseña incorrecta")
        else:
             messagebox.showerror("Error",f"El usario {self.user_input.get()} no existe")

    def index(self,master):
        self.fuente = ("Arial", 12, "bold")
        self.alto = 400
        self.ancho = 350

        self.root =Toplevel(master)
        """self.root =Tk()"""
        self.root.grab_set()
        
        self.frame1 = Frame(self.root)
        self.frame1.place(x=130, y=10)

        Label(self.frame1, text="Verificacion", font=self.fuente).grid(row=0, column=0)

        self.frame2 = Frame(self.root)
        self.frame2.place(x=80, y=50)

        
        Label(self.frame2, text="User", font=self.fuente).grid(row=0, column=0, sticky='w')
        self.user_input = Entry(self.frame2, width=20, font="bold")
        self.user_input.grid(row=1, column=0, pady=15)

        Label(self.frame2, text="Pass", font=self.fuente).grid(row=2, column=0, sticky='w')
        self.pass_input = Entry(self.frame2, width=20, font="bold", show="*")
        self.pass_input.grid(row=3, column=0, pady=15)

        Button(self.frame2, text="Enviar", width=15, font="bold", command=lambda:self.verif(master)).grid(row=4, column=0, pady=15)
        
        self.root.geometry(f"{self.ancho}x{self.alto}+{((self.root.winfo_screenwidth() // 2) - (self.ancho // 2))}+{((self.root.winfo_screenheight() // 2) - (self.alto // 2))}")
        self.root.mainloop()

