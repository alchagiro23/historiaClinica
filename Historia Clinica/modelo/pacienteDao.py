from .conexion import ConexionDB
from tkinter import messagebox


def editarDatoPaciente(persona, idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET nombre = '{persona.nombre}', apellidoPaterno = '{persona.apellidoPaterno}',
            apellidoMaterno = '{persona.apellidoMaterno}', cedula = {persona.cedula}, fechaNacimiento = '{persona.fechaNacimiento}',
            edad = {persona.edad}, antecedentes = '{persona.antecedentes}', correo = '{persona.correo}', telefono = '{persona.telefono}', activo = 1 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Paciente'
        mensaje = 'Paciente editado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Paciente'
        mensaje = 'Error al editar Paciente'
        messagebox.showinfo(title, mensaje)

def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona (nombre, apellidoPaterno, apellidoMaterno, 
            cedula, fechaNacimiento, edad, antecedentes, correo, telefono, activo) VALUES
            ('{persona.nombre}','{persona.apellidoPaterno}','{persona.apellidoMaterno}',
            {persona.cedula},'{persona.fechaNacimiento}','{persona.edad}','{persona.antecedentes}',
            '{persona.correo}','{persona.telefono}',1)"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Paciente'
        mensaje = 'Paciente Registrado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar Paciente'
        mensaje = 'Error al registrar Paciente'
        messagebox.showerror(title, mensaje) 

def listar():
    conexion = ConexionDB()
    
    listaPersona = []
    sql = 'SELECT * FROM Persona WHERE activo = 1'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()

    except: 
        title = 'Datos'
        mensaje = 'Registros no Existen'
        messagebox.showwarning(title, mensaje)
    return listaPersona

def listarCondicion(where):
    conexion = ConexionDB()
    listaPersona = []
    sql = f'SELECT * FROM Persona {where}'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()

    except: 
        title = 'Datos'
        mensaje = 'Registros no Existen'
        messagebox.showwarning(title, mensaje)   
    return listaPersona    

def eliminarPaciente(idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Paciente'
        mensaje = 'Paciente eliminado exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Paciente'
        mensaje = 'Error al eliminar Paciente'
        messagebox.showwarning(title, mensaje)





class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, cedula, fechaNacimiento, edad, antecedentes, correo, telefono):
        self.idPersona = None
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.cedula = cedula
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.antecedentes = antecedentes
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f'Persona[{self.nombre},{self.apellidoPaterno},{self.apellidoMaterno},{self.cedula},{self.fechaNacimiento},{self.edad},{self.antecedentes},{self.correo},{self.telefono}]'    