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
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        return sum(1 for asiento in self.asientos if asiento is not None)

    def verificarIntegridad(self):
        original_registro = self.motor.registro
        for asiento in self.asientos:
            if asiento is not None and asiento.registro != original_registro:
                return "Las piezas no son originales"
        return "Auto original"
