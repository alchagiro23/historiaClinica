import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel, LabelFrame
from tkinter import messagebox
from modelo.pacienteDao import Persona, guardarDatoPaciente, listarCondicion, listar, editarDatoPaciente, eliminarPaciente
from modelo.historiaClinicaDao import historiaClinica, guardarHistoria, listarHistoria
from tkinter import font
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date


class Frame(tk.Frame):
    def __init__(self, root):

        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#CDD8FF')
        self.idPersona = None
        self.camposPaciente()
        self.deshabilitar()
        self.tablaPaciente()


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
        self.entryApePaterno = tk.Entry(self, textvariable=self.svApePaterno)
        self.entryApePaterno.config(width=50, font=('ARIAL',15))
        self.entryApePaterno.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svApeMaterno = tk.StringVar()
        self.entryApeMaterno = tk.Entry(self, textvariable=self.svApeMaterno)
        self.entryApeMaterno.config(width=50, font=('ARIAL',15))
        self.entryApeMaterno.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svCedula = tk.StringVar()
        self.entryCedula = tk.Entry(self, textvariable=self.svCedula)
        self.entryCedula.config(width=50, font=('ARIAL',15))
        self.entryCedula.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svFechNacimiento = tk.StringVar()
        self.entryFechNacimiento = tk.Entry(self, textvariable=self.svFechNacimiento)
        self.entryFechNacimiento.config(width=50, font=('ARIAL',15))
        self.entryFechNacimiento.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=('ARIAL',15))
        self.entryEdad.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svAntecedentes = tk.StringVar()
        self.entryAntecedentes = tk.Entry(self, textvariable=self.svAntecedentes)
        self.entryAntecedentes.config(width=50, font=('ARIAL',15))
        self.entryAntecedentes.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        self.svCorreo  = tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=50, font=('ARIAL',15))
        self.entryCorreo.grid(column=1, row=7, padx=10, pady=5, columnspan=2)

        self.svTelefono  = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=('ARIAL',15))
        self.entryTelefono.grid(column=1, row=8, padx=10, pady=5, columnspan=2)

        #BUTTONS
        self.btnNuevo = tk.Button(self, text='Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2',activebackground='#35BD6F')
        self.btnNuevo.grid(column=0, row=9, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#0475C6', cursor='hand2',activebackground='#68B3E9')
        self.btnGuardar.grid(column=1, row=9, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#B00000', cursor='hand2',activebackground='#D27C7C')
        self.btnCancelar.grid(column=2, row=9, padx=10, pady=5)


        #BUSCADOR
        #LABEL BUSCADOR
        self.lblBuscarCedula = tk.Label(self, text='Buscar Cedula: ')
        self.lblBuscarCedula.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblBuscarCedula.grid(column=3, row=0, padx=10, pady=5)

        self.lblBuscarApellido = tk.Label(self, text='Buscar Apellido: ')
        self.lblBuscarApellido.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblBuscarApellido.grid(column=3, row=1, padx=10, pady=5)

        #ENTRYS BUSCADOR
        self.svBuscarCedula = tk.StringVar()
        self.entryBuscarCedula = tk.Entry(self, textvariable=self.svBuscarCedula)
        self.entryBuscarCedula.config(width=25, font=('ARIAL',15))
        self.entryBuscarCedula.grid(column=4, row=0, padx=10, pady=5, columnspan=2)

        self.svBuscarApellido = tk.StringVar()
        self.entryBuscarApellido = tk.Entry(self, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=25, font=('ARIAL',15))
        self.entryBuscarApellido.grid(column=4, row=1, padx=10, pady=5, columnspan=2)

        #BUTTON BUSCAR
        self.btnBuscarCondicion = tk.Button(self, text='Buscar', command= self.buscarCondicion)
        self.btnBuscarCondicion.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#00396F', cursor='hand2',activebackground='#5B8D8D')
        self.btnBuscarCondicion.grid(column=3, row=2, padx=10, pady=5, columnspan=1)

        self.btnLimpiarBuscador = tk.Button(self, text='Limpiar', command= self.limpiarBuscador)
        self.btnLimpiarBuscador.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#00396F', cursor='hand2',activebackground='#5B8D8D')
        self.btnLimpiarBuscador.grid(column=4, row=2, padx=10, pady=5, columnspan=1)

        #BUTTON CALENDARIO
        self.btnCalendario = tk.Button(self, text='Calendario', command= self.vistaCalendario)
        self.btnCalendario.config(width=12, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#00396F', cursor='hand2',activebackground='#5B8D8D')
        self.btnCalendario.grid(column=3, row=4, padx=10, pady=5, columnspan=1)

    def vistaCalendario(self):
        self.calendario = Toplevel()
        self.calendario.title("FECHA NACIMIENTO")
        self.calendario.resizable(0,0)
        self.calendario.config(bg='#CDD8FF')
        
        self.svCalendario = StringVar()
        self.calendar = tc.Calendar(self.calendario, selectmode='day', year=1990, month=1, day=1, locale = 'es_US', bg='#777777', fg= '#FFFFFF', headersbackground='#B6DDFE', cursor='hand2', date_pattern='dd-mm-Y')
        self.calendar.pack(pady=22)
        self.calendar.grid(row=1, column = 0)
        self.calendar.bind("<<CalendarSelected>>", self.enviarFecha)  # MODIFICACION QUE CORRIGE GPT
        self.enviarFecha()
     #   self.svCalendario.trace_add('write', self.enviarFecha)

   # def enviarFecha(self, *args):
   #     self.svFechNacimiento.set('' + self.svCalendario.get())


    def enviarFecha(self, event=None):   #MODIFICACION QUE DA GPT (FUNCIONA)
        selected_date = self.calendar.get_date()
        self.svFechNacimiento.set(selected_date)
        if len(self.calendar.get_date()) > 1:
            self.calcularEdad() 


      #  if len(self.calendar.get_date()) > 1:
       #     self.svCalendario.trace()
    def calcularEdad(self, *args):
        self.fechaActual = date.today()
        self.date1 = self.calendar.get_date()
        self.conver = datetime.strptime(self.date1, "%d-%m-%Y")

        self.resul = self.fechaActual.year - self.conver.year
        self.resul -= ((self.fechaActual.month, self.fechaActual.day) < (self.conver.month, self.conver.day))
        self.svEdad.set(self.resul)




    def limpiarBuscador(self):     #LIMPIAR EL BUSCADOR
        self.svBuscarApellido.set('')
        self.svBuscarCedula.set('')
        self.tablaPaciente()

    def buscarCondicion(self):     # FUNCION BUSCAR
        if len(self.svBuscarCedula.get()) > 0 or len(self.svBuscarApellido.get()) > 0:
            where = "WHERE 1=1"
            if (len(self.svBuscarCedula.get())) > 0:
                where = "WHERE cedula = " + self.svBuscarCedula.get() + ""
            if (len(self.svBuscarApellido.get())) > 0:
                where = "WHERE apellidoPaterno LIKE '" + self.svBuscarApellido.get() + "%' AND activo = 1" 

            self.tablaPaciente(where)
        else:
            self.tablaPaciente()


        
    def guardarPaciente(self):
        persona = Persona(
            self.svNombre.get(), self.svApePaterno.get(), self.svApeMaterno.get(), self.svCedula.get(), self.svFechNacimiento.get(), self.svEdad.get(), self.svAntecedentes.get(), self.svCorreo.get(), self.svTelefono.get()
        )

        if self.idPersona == None:
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)


        self.deshabilitar()
        self.tablaPaciente()

    def habilitar(self):
        #self.idPersona = None
        self.svNombre.set('')
        self.svApePaterno.set('')
        self.svApeMaterno.set('')
        self.svCedula.set('')
        self.svFechNacimiento.set('')
        self.svEdad.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')

        self.entryNombre.config(state='normal')
        self.entryApePaterno.config(state='normal')
        self.entryApeMaterno.config(state='normal')
        self.entryCedula.config(state='normal')
        self.entryFechNacimiento.config(state='normal')
        self.entryEdad.config(state='normal')
        self.entryAntecedentes.config(state='normal')
        self.entryCorreo.config(state='normal')
        self.entryTelefono.config(state='normal')

        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')
        self.btnCalendario.config(state='normal')


    def deshabilitar(self):
        self.idPersona = None
        self.svNombre.set('')
        self.svApePaterno.set('')
        self.svApeMaterno.set('')
        self.svCedula.set('')
        self.svFechNacimiento.set('')
        self.svEdad.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')


        self.entryNombre.config(state='disabled')
        self.entryApePaterno.config(state='disabled')
        self.entryApeMaterno.config(state='disabled')
        self.entryCedula.config(state='disabled')
        self.entryFechNacimiento.config(state='disabled')
        self.entryEdad.config(state='disabled')
        self.entryAntecedentes.config(state='disabled')
        self.entryCorreo.config(state='disabled')
        self.entryTelefono.config(state='disabled')

        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')
        self.btnCalendario.config(state='disabled')

    def tablaPaciente(self, where=""):

        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()
         #   self.listaPersona.reverse()    PARA QUE SALGAN EN ORDEN LOS ID

        self.tabla = ttk.Treeview(self, column=('Nombre', 'Apaterno', 'AMaterno', 'cedula', 'FNacimiento', 'Edad', 'Antecedentes','Correo', 'Telefono'))    
        self.tabla.grid(column=0, row=10, columnspan=10, sticky='nse')
        
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=10, column=11, sticky='nse')

        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.tag_configure('evenrow', background='#C5EAFE')

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Apellido P')
        self.tabla.heading('#3',text='Apellido M')
        self.tabla.heading('#4',text='Cedula')
        self.tabla.heading('#5',text='F Nacimiento')
        self.tabla.heading('#6',text='Edad')
        self.tabla.heading('#7',text='Antecedentes')
        self.tabla.heading('#8',text='Correo')
        self.tabla.heading('#9',text='Telefono')

        self.tabla.column("#0", anchor=W, width=50)
        self.tabla.column("#1", anchor=W, width=150)
        self.tabla.column("#2", anchor=W, width=150)
        self.tabla.column("#3", anchor=W, width=150)
        self.tabla.column("#4", anchor=W, width=80)
        self.tabla.column("#5", anchor=W, width=100)
        self.tabla.column("#6", anchor=W, width=50)
        self.tabla.column("#7", anchor=W, width=300)
        self.tabla.column("#8", anchor=W, width=250)
        self.tabla.column("#9", anchor=W, width=80)


        for p in self.listaPersona:

            self.tabla.insert('',0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9]), tags=('evenrow',))

# MAS BUTTONS (EDITAR, ELIMINAR, HISTORIA PACIENTE)
        self.btnEditarPaciente = tk.Button(self, text='Editar Paciente', command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#1E0075', activebackground='#9379E0', cursor='hand2')    
        self.btnEditarPaciente.grid(row=11, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command=self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#8A0000', activebackground='#D58A8A', cursor='hand2')    
        self.btnEliminarPaciente.grid(row=11, column=1, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text='Historial Paciente', command=self.historiaClinica)
        self.btnHistorialPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#007C79', activebackground='#99F2F0', cursor='hand2')    
        self.btnHistorialPaciente.grid(row=11, column=2, padx=10, pady=5)

        self.btnSalir = tk.Button(self, text='Salir', command=self.root.destroy)
        self.btnSalir.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', activebackground='#5E5E5E', cursor='hand2')    
        self.btnSalir.grid(row=11, column=4, padx=10, pady=5)


    def historiaClinica (self):

        try:
            if self.idPersona == None:
                self.idPersona = self.tabla.item(self.tabla.selection())['text']

            if (self.idPersona > 0):
                idPersona = self.idPersona

            self.topHistoriaClinica = Toplevel()
            self.topHistoriaClinica.title('HISTORIA CLINICA')
            self.topHistoriaClinica.resizable(0,0)
            self.topHistoriaClinica.config(bg='#CDD8FF')

            self.listaHistoria = listarHistoria(idPersona)
            self.tablaHistoria = ttk.Treeview(self.topHistoriaClinica, column=('Apellidos','Fecha Historia', 'Motivo','Examen Auxiliar','Tratamiento','Detalle'))
            self.tablaHistoria.grid(row=0, column=0, columnspan=7, sticky='nse')

            self.scrollHistoria = ttk.Scrollbar(self.topHistoriaClinica, orient='vertical', command=self.tablaHistoria.yview) 
            self.scrollHistoria.grid(row=0, column=8, sticky='nse')

            self.tablaHistoria.configure(yscrollcommand=self.scrollHistoria.set)
            self.tablaHistoria.heading('#0', text='ID')
            self.tablaHistoria.heading('#1', text='Apellidos')
            self.tablaHistoria.heading('#2', text='Fecha y Hora')
            self.tablaHistoria.heading('#3', text='Motivo')
            self.tablaHistoria.heading('#4', text='Examen Auxiliar')
            self.tablaHistoria.heading('#5', text='Tratamiento')
            self.tablaHistoria.heading('#6', text='Detalle')

            self.tablaHistoria.column('#0', anchor=W, width=50)
            self.tablaHistoria.column('#1', anchor=W, width=100)
            self.tablaHistoria.column('#2', anchor=W, width=100)
            self.tablaHistoria.column('#3', anchor=W, width=120)
            self.tablaHistoria.column('#4', anchor=W, width=250)
            self.tablaHistoria.column('#5', anchor=W, width=200)
            self.tablaHistoria.column('#6', anchor=W, width=500)

            for p in self.listaHistoria:
                self.tablaHistoria.insert('',0, text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6]))

            self.btnGuardarHistoria = tk.Button(self.topHistoriaClinica, text='Agregar Historia', command=self.topAgregarHistoria)
            self.btnGuardarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#002771', cursor='hand2', activebackground='#7198E0')
            self.btnGuardarHistoria.grid(row=2, column=0, padx=10, pady=5)

            self.btnEditarHistoria = tk.Button(self.topHistoriaClinica, text='Editar Historia')
            self.btnEditarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#002771', cursor='hand2', activebackground='#7198E0')
            self.btnEditarHistoria.grid(row=2, column=1, padx=10, pady=5)

            self.btnEliminarHistoria = tk.Button(self.topHistoriaClinica, text='Elminar Historia')
            self.btnEliminarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#002771', cursor='hand2', activebackground='#7198E0')
            self.btnEliminarHistoria.grid(row=2, column=2, padx=10, pady=5)

            self.btnSalirHistoria = tk.Button(self.topHistoriaClinica, text='Salir', command=self.salirTop)
            self.btnSalirHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#002771', cursor='hand2', activebackground='#7198E0')
            self.btnSalirHistoria.grid(row=2, column=6, padx=10, pady=5)

        except:
            title = 'Historia Clinica'
            mensaje = 'Error al mostrar Historia'
            messagebox.showerror(title, mensaje)

    def topAgregarHistoria(self):
        self.topAHistoria = Toplevel()
        self.topAHistoria.title('AGREGAR HISTORIA')
        self.topAHistoria.resizable(0,0)
        self.topAHistoria.config(bg='#CDD8FF')
        #FRAME 1
        self.frameDatosHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameDatosHistoria.config(bg='#CDD8FF')
        self.frameDatosHistoria.pack(fill="both", expand="yes", pady=10, padx=20)

        #LABELS AGREGAR HISTORIA CLINICA
        self.lblMotivoHistoria = tk.Label(self.frameDatosHistoria, text='Motivo de la Historia medica', width=30, font=('ARIAL', 15,'bold'), bg='#CDD8FF')
        self.lblMotivoHistoria.grid(row=0, column=0, padx=5, pady=3)

        self.lblExamenAuxiliarHistoria = tk.Label(self.frameDatosHistoria, text='Examen Auxiliar', width=20, font=('ARIAL', 15,'bold'), bg='#CDD8FF')
        self.lblExamenAuxiliarHistoria.grid(row=2, column=0, padx=5, pady=3)

        self.lblTratamientoHistoria = tk.Label(self.frameDatosHistoria, text='Tratamiento', width=20, font=('ARIAL', 15,'bold'), bg='#CDD8FF')
        self.lblTratamientoHistoria.grid(row=4, column=0, padx=5, pady=3)

        self.lblDetalleHistoria = tk.Label(self.frameDatosHistoria, text='Detalle de la Historia', width=30, font=('ARIAL', 15,'bold'), bg='#CDD8FF')
        self.lblDetalleHistoria.grid(row=6, column=0, padx=5, pady=3)

        # ENTRYS AGREGAR HISTORIA CLINICA
        self.svMotivoHistoria = tk.StringVar()
        self.motivoHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svMotivoHistoria)
        self.motivoHistoria.config(width=70, font=('ARIAL', 15))
        self.motivoHistoria.grid(row=1, column=0, padx=5, pady=3, columnspan=2)

        self.svExamenAuxiliarHistoria = tk.StringVar()
        self.examenAuxiliarHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svExamenAuxiliarHistoria)
        self.examenAuxiliarHistoria.config(width=70, font=('ARIAL', 15))
        self.examenAuxiliarHistoria.grid(row=3, column=0, padx=5, pady=3, columnspan=2)

        self.svTratamientoHistoria = tk.StringVar()
        self.tratamientoHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svTratamientoHistoria)
        self.tratamientoHistoria.config(width=70, font=('ARIAL', 15))
        self.tratamientoHistoria.grid(row=5, column=0, padx=5, pady=3, columnspan=2)

        self.svDetalleHistoria = tk.StringVar()
        self.detalleHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svDetalleHistoria)
        self.detalleHistoria.config(width=70, font=('ARIAL', 15))
        self.detalleHistoria.grid(row=7, column=0, padx=5, pady=3, columnspan=2)
        # FRAME 2
        self.frameFechaHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameFechaHistoria.config(bg='#CDD8FF')
        self.frameFechaHistoria.pack(fill="both", expand="yes", pady=10, padx=20)

        #LABEL FECHA AGREGAR HISTORIA 
        self.lblFechaHistoria = tk.Label(self.frameFechaHistoria, text='Fecha y Hora', width=20, font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
        self.lblFechaHistoria.grid(row=1, column=0, padx=5, pady=3)
        
        #ENTRY FECHA AGREGAR HISTORIA
        self.svFechaHistoria = tk.StringVar()
        self.entryFechaHistoria = tk.Entry(self.frameFechaHistoria, textvariable=self.svFechaHistoria)
        self.entryFechaHistoria.config(width=20, font=('ARIAL', 15))
        self.entryFechaHistoria.grid(row=1, column=1, pady=3, padx=5)
        #TRAER FECHA ACTUAL
        self.svFechaHistoria.set(datetime.today().strftime('%d-%m-%Y %H:%M'))

        #BUTTONS AGREGAR HISTORIA
        self.btnAgregarHistoria = tk.Button(self.frameFechaHistoria, text='Agregar Historia')
        self.btnAgregarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000992', cursor='hand2', activebackground='#4E56C6')
        self.btnAgregarHistoria.grid(row=2, column=0, padx=10, pady=5)

        self.btnSalirAgregarHistoria = tk.Button(self.frameFechaHistoria, text='Salir', command=self.topAHistoria.destroy)
        self.btnSalirAgregarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000992', cursor='hand2', activebackground='#4E56C6')
        self.btnSalirAgregarHistoria.grid(row=2, column=3, padx=10, pady=5)
        


    def salirTop(self):
        self.topHistoriaClinica.destroy()



    def editarPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text'] #TRAE EL ID
            self.nombrePaciente = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellidoPaternoPaciente = self.tabla.item(self.tabla.selection())['values'][1]
            self.apellidoMaternoPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            self.cedulaPaciente = self.tabla.item(self.tabla.selection())['values'][3]
            self.fechaNacimientoPaciente = self.tabla.item(self.tabla.selection())['values'][4]
            self.edadPaciente = self.tabla.item(self.tabla.selection())['values'][5]
            self.antecedentesPaciente = self.tabla.item(self.tabla.selection())['values'][6]
            self.correoPaciente = self.tabla.item(self.tabla.selection())['values'][7]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())['values'][8]

            self.habilitar()

            self.entryNombre.insert(0, self.nombrePaciente)
            self.entryApePaterno.insert(0, self.apellidoPaternoPaciente)
            self.entryApeMaterno.insert(0, self.apellidoMaternoPaciente)
            self.entryCedula.insert(0, self.cedulaPaciente)
            self.entryFechNacimiento.insert(0, self.fechaNacimientoPaciente)
            self.entryEdad.insert(0, self.edadPaciente)
            self.entryAntecedentes.insert(0, self.antecedentesPaciente)
            self.entryCorreo.insert(0, self.correoPaciente)
            self.entryTelefono.insert(0, self.telefonoPaciente)      
        except:
            title = 'Editar Paciente'
            mensaje = 'Error al editar Paciente'
            messagebox.showerror(title, mensaje)   

    def eliminarDatoPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.idPersona)
            
            self.tablaPaciente()
            self.idPersona = None
        except:
            title = 'Eliminar Paciente'
            mensaje = 'No se pudo eliminar el paciente'
            messagebox.showerror(title, mensaje)
