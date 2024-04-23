from .conexion import ConexionDB
from tkinter import messagebox

def guardarHistoria(idPersona, fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle):
    conexion = ConexionDB()
    sql = f"""INSERT INTO historiaClinica (idPersona, fechaHistoria, motivo, tratamiento, detalles)VALUES
            ({idPersona},'{fechaHistoria}','{motivo}','{examenAuxiliar},'{tratamiento}','{detalle}')"""
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