class PartyAnimal:
    def __init__(self):
        self.x = 0

    def party(self):
        self.x += 1
        print("Party count:", self.x)

# Crear una instancia de PartyAnimal
an = PartyAnimal()

# Usar dir() para listar métodos y atributos de la instancia
print(dir(an))