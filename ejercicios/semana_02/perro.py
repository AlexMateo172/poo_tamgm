class Perro:
    def __init__(self, nombre, raza, edad_meses, color_del_perro, peso_kg, tamano, genero, tipo_de_dieta, es_jugueton, nivel_de_babeo):
        
        self.nombre = nombre
        self.raza = raza
        self.edad_meses = edad_meses
        self.color_del_perro = color_del_perro
        self.peso_kg = peso_kg
        self.tamano = tamano
        self.genero = genero
        self.tipo_de_dieta = tipo_de_dieta
        self.es_jugueton = es_jugueton
        self.nivel_de_babeo = nivel_de_babeo

        print(f"Nombre del Perro: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad en meses: {self.edad_meses}")
        print(f"Color del Perro: {self.color_del_perro}")
        print(f"Peso en kg: {self.peso_kg}")
        print(f"Tamaño: {self.tamano}")
        print(f"Género: {self.genero}")
        print(f"Tipo de dieta: {self.tipo_de_dieta}")
        print(f"Es juguetón: {self.es_jugueton}")
        print(f"Nivel de babeo: {self.nivel_de_babeo}")
    

    def ladrar(self):
        print("El perro está ladrando")
    def resoplar(self):
        print("El perro está resoplando")
    def correr(self):
        print("El perro está corriendo")
    def dormir(self):
        print("El perro está durmiendo")
    def comer(self):
        print("El perro está comiendo")

toby = Perro(
    "Toby", "Pug", "8", "Arena",
    "7", "Pequeño", "Macho", "Croquetas",
    "Verdadero", "Alto"
)


toby.ladrar()
toby.resoplar()
toby.correr()
toby.dormir()
toby.comer()
