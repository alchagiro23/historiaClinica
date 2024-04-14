from .conexion import ConexionDB
from tkinter import messagebox

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