# Clase base Vehiculo
class Vehiculo:
    def _init_(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El {self.modelo} está encendido.")
        else:
            print(f"El {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"El {self.modelo} está apagado.")
        else:
            print(f"El {self.modelo} ya está apagado.")

# Clase Auto que hereda de Vehiculo
class Auto(Vehiculo):
    def tocar_bocina(self):
        print("Beep beep!")

# Clase Motocicleta que hereda de Vehiculo
class Motocicleta(Vehiculo):
    def hacer_caballito(self):
        if self.encendido:
            print("La motocicleta está haciendo un caballito.")
        else:
            print("No puedes hacer un caballito con la moto apagada.")