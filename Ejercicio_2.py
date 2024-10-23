# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"El vehículo {self.marca} {self.modelo} está arrancando.")

#clases hijas
class Coche(Vehiculo):
    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} se enciende y arranca")

class Motocicleta(Vehiculo):
    def arrancar(self):
        print(f"La motocicleta {self.marca} {self.modelo} acelera y arranca.")

class Bicicleta(Vehiculo):
    def arrancar(self):
        print(f"La bicicleta {self.marca} {self.modelo} comienza a moverse por el pedal.")


def arrancar_vehiculo(vehiculo):
    vehiculo.arrancar()

coche = Coche("mercedes", "2020")
moto = Motocicleta("suzuki", "GSX-R750")
bicicleta = Bicicleta("Trek", " Marlin 7")

arrancar_vehiculo(coche)
arrancar_vehiculo(moto)
arrancar_vehiculo(bicicleta)
