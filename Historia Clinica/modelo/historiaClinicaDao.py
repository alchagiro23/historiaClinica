from sqlite3.dbapi2 import Cursor
from .conexion import ConexionDB
from tkinter import messagebox

def listarHistoria(idPersona):
    conexion = ConexionDB()
    listaHistoria = []
    sql = f'SELECT h.idHistoriaClinica, p.apellidoPaterno || " " || p.apellidoMaterno AS Apellidos, h.fechaHistoria, h.motivo, h.examenAuxiliar, h.tratamiento, h.detalle FROM historiaClinica h INNER JOIN Persona p ON p.idPersona = h.idPersona WHERE p.idPersona = {idPersona}'
    
    try:
        conexion.cursor.execute(sql)
        listaHistoria = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'LISTAR HISTORIA'
        mensaje = 'Error al listar historia Clinica'
        messagebox.showerror(title, mensaje)

    return listaHistoria


def guardarHistoria(idPersona, fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle):
    conexion = ConexionDB()
    sql = f"""INSERT INTO historiaClinica (idPersona, fechaHistoria, motivo, tratamiento, detalles)VALUES
            ({idPersona},'{fechaHistoria}','{motivo}','{examenAuxiliar}',{tratamiento}','{detalle}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Historia Clinica'
        mensaje = 'Historia Registrada Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar Historia Clinica'
        mensaje = 'Error al Registrar Historia'
        messagebox.showinfo(title, mensaje)

class historiaClinica:
    def __init__(self, idPersona, fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle):
        self.idHistoriaClinica = None
        self.idPersona = idPersona
        self.fechaHistoria = fechaHistoria
        self.motivo = motivo
        self.examenAuxiliar = examenAuxiliar
        self.tratamiento = tratamiento
        self.detalle = detalle

    def __str__(self):
        return f'historioaClinica[{self.idPersona},{self.fechaHistoria},{self.motivo},{self.examenAuxiliar},{self.tratamiento},{self.detalle} ]'