# main.py

class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevo_color):
        self.color = nuevo_color

class Motor:
    def __init__(self, cilindros, tipo, registro):
        self.cilindros = cilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevo_registro):
        self.registro = nuevo_registro

    def asignarTipo(self, nuevo_tipo):
        self.tipo = nuevo_tipo

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos  # Lista de asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        # Cuenta los asientos que no son None
        return sum(1 for asiento in self.asientos if asiento is not None)

    def verificarIntegridad(self):
        # Verifica si todos los asientos tienen el mismo registro que el motor
        for asiento in self.asientos:
            if asiento is not None and asiento.registro != self.motor.registro:
                return "Las piezas no son originales"
        return "Auto original"
