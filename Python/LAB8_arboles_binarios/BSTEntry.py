class BSTEntry:
    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __str__(self):
        return f"Clave: {self.key}, Datos: {self.data}"