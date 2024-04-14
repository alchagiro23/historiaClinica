import tkinter as tk
from tkinter import font

class Frame(tk.Frame):
    def __init__(self, root):

        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#CDD8FF')
        self.camposPaciente()

# LABELS
    def camposPaciente(self):  #
        self.lblNombre = tk.Label(self, text='Nombre: ')
        self.lblNombre.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblNombre.grid(column=0, row=0, padx=10, pady=5)

        self.lblApePaterno = tk.Label(self, text='Apellido Paterno: ')
        self.lblApePaterno.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblApePaterno.grid(column=0, row=1, padx=10, pady=5)

        self.lblApeMaterno = tk.Label(self, text='Apellido Materno: ')
        self.lblApeMaterno.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblApeMaterno.grid(column=0, row=2, padx=10, pady=5)

        self.lblCedula = tk.Label(self, text='Cedula: ')
        self.lblCedula.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblCedula.grid(column=0, row=3, padx=10, pady=5)

        self.lblFechNacimiento = tk.Label(self, text='Fecha Nacimiento: ')
        self.lblFechNacimiento.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblFechNacimiento.grid(column=0, row=4, padx=10, pady=5)

        self.lblEdad = tk.Label(self, text='Edad: ')
        self.lblEdad.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblEdad.grid(column=0, row=5, padx=10, pady=5)

        self.lblAntecedentes = tk.Label(self, text='Antecedentes: ')
        self.lblAntecedentes.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblAntecedentes.grid(column=0, row=6, padx=10, pady=5)

        self.lblCorreo = tk.Label(self, text='Correo: ')
        self.lblCorreo.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblCorreo.grid(column=0, row=7, padx=10, pady=5)

        self.lblTelefono = tk.Label(self, text='Telefono: ')
        self.lblTelefono.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblTelefono.grid(column=0, row=8, padx=10, pady=5)


        #ENTRYS
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=('ARIAL',15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApePaterno = tk.StringVar()
        self.svApePaterno = tk.Entry(self, textvariable=self.svApePaterno)
        self.svApePaterno.config(width=50, font=('ARIAL',15))
        self.svApePaterno.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svApeMaterno = tk.StringVar()
        self.svApeMaterno = tk.Entry(self, textvariable=self.svApeMaterno)
        self.svApeMaterno.config(width=50, font=('ARIAL',15))
        self.svApeMaterno.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svCedula = tk.StringVar()
        self.svCedula = tk.Entry(self, textvariable=self.svCedula)
        self.svCedula.config(width=50, font=('ARIAL',15))
        self.svCedula.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svFechNacimiento = tk.StringVar()
        self.svFechNacimiento = tk.Entry(self, textvariable=self.svFechNacimiento)
        self.svFechNacimiento.config(width=50, font=('ARIAL',15))
        self.svFechNacimiento.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.svEdad = tk.Entry(self, textvariable=self.svEdad)
        self.svEdad.config(width=50, font=('ARIAL',15))
        self.svEdad.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svAntecedentes = tk.StringVar()
        self.svAntecedentes = tk.Entry(self, textvariable=self.svAntecedentes)
        self.svAntecedentes.config(width=50, font=('ARIAL',15))
        self.svAntecedentes.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        self.svCorreo  = tk.StringVar()
        self.svCorreo = tk.Entry(self, textvariable=self.svAntecedentes)
        self.svCorreo.config(width=50, font=('ARIAL',15))
        self.svCorreo.grid(column=1, row=7, padx=10, pady=5, columnspan=2)

        self.svTelefono  = tk.StringVar()
        self.svTelefono = tk.Entry(self, textvariable=self.svAntecedentes)
        self.svTelefono.config(width=50, font=('ARIAL',15))
        self.svTelefono.grid(column=1, row=8, padx=10, pady=5, columnspan=2)

        #BUTTONS
        self.btnNuevo = tk.Button(self, text='Nuevo')
        self.btnNuevo.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2',activebackground='#35BD6F')
        self.btnNuevo.grid(column=0, row=9, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar')
        self.btnGuardar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#0475C6', cursor='hand2',activebackground='#68B3E9')
        self.btnGuardar.grid(column=1, row=9, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar')
        self.btnCancelar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#B00000', cursor='hand2',activebackground='#D27C7C')
        self.btnCancelar.grid(column=2, row=9, padx=10, pady=5)

        




