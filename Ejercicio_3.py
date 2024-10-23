class P3D:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __sub__(self, otro):
        return P3D(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

punto1 = P3D(6, 8, 2)
punto2 = P3D(7, 3, 2)

resultado = punto1 - punto2

print(f"Resultado de la resta: {resultado}")
