from datetime import datetime

class Mensaje:
    def __init__(self, remitente, destinatario, titulo, contenido):
        self.remitente = remitente
        self.destinatario = destinatario
        self.titulo = titulo
        self.contenido = contenido
        self.fecha = datetime.now()

    def __str__(self):
        return f"{self.fecha} - {self.titulo} de {self.remitente}"
