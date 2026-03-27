# Paradigma Orientado a objetos:

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print("Nombre:", self.nombre)

class Cliente(Persona):
    def __init__(self, nombre, telefono):
        super().__init__(nombre)
        self.telefono = telefono

    def mostrar_datos(self):
        print(f"Cliente: {self.nombre} - Teléfono: {self.telefono}")


class Servicio:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_servicio(self):
        print(f"Servicio: {self.nombre} - Precio: ${self.precio}")

class Turno:
    def __init__(self, cliente, servicio, hora):
        self.cliente = cliente
        self.servicio = servicio
        self.hora = hora

    def mostrar_turno(self):
        print("---- Turno ----")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Servicio: {self.servicio.nombre}")
        print(f"Hora: {self.hora}")
        print(f"Precio: ${self.servicio.precio}")


cliente1 = Cliente("Santiago Suarez", "123456789")
servicio1 = Servicio("Corte de pelo", 2500)

turno1 = Turno(cliente1, servicio1, "15:30")

cliente1.mostrar_datos()
servicio1.mostrar_servicio()
turno1.mostrar_turno()