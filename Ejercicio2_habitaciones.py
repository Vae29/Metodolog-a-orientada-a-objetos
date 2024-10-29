# Clase Habitacion
class Habitacion:
    def _init_(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.ocupada = False

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            print(f"Habitación {self.numero} ({self.tipo}) ha sido reservada.")
        else:
            print(f"Habitación {self.numero} ya está ocupada.")

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            print(f"Habitación {self.numero} ha sido liberada.")
        else:
            print(f"Habitación {self.numero} ya está libre.")

# Clase Huesped
class Huesped:
    def _init_(self, nombre):
        self.nombre = nombre

    def reservar_habitacion(self, habitacion):
        if not habitacion.ocupada:
            habitacion.reservar()
            print(f"{self.nombre} ha reservado la habitación {habitacion.numero}.")
        else:
            print(f"La habitación {habitacion.numero} no está disponible.")