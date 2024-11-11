class Perro:
    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre

    @property
    def raza(self):
        return self.raza

    @raza.setter
    def raza(self, raza):
        self.raza = raza

    @property
    def edad(self):
        return self.edad

    @edad.setter
    def edad(self, edad):
        if 0 < edad <= 3:
            self.edad = edad

    def ladrar(self):
        print(f"¡Guau! Soy {self.nombre} y tengo {self.edad} años.")