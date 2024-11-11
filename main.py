class Asiento:
    def __init__(self, color, precio, registro):
        self.precio = precio
        self.registro = registro
        self.color = None
        self.cambiarColor(color)

    def cambiarColor(self, nuevo_color):
        colores_permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if nuevo_color in colores_permitidos:
            self.color = nuevo_color


class Motor:
    def __init__(self, cilindros, tipo, registro):
        self.cilindros = cilindros
        self.tipo = None
        self.registro = registro
        self.asignarTipo(tipo)

    def cambiarRegistro(self, nuevo_registro):
        self.registro = nuevo_registro

    def asignarTipo(self, nuevo_tipo):
        tipos_permitidos = ["electrico", "gasolina"]
        if nuevo_tipo in tipos_permitidos:
            self.tipo = nuevo_tipo


class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        return sum(1 for asiento in self.asientos if isinstance(asiento, Asiento))

    def verificarIntegridad(self):
        for asiento in self.asientos:
            if asiento is not None and asiento.registro != self.motor.registro:
                return "Las piezas no son originales"
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        return "Auto original"
