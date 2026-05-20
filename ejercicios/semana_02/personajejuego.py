class PersonajedelJuego:
    def __init__(self, nombre, especie, color, velocidad, altura, peso, contador, vidas, estado_actual, habilidad):

        self.nombre = nombre
        self.especie = especie
        self.color = color
        self.velocidad = velocidad
        self.altura = altura
        self.peso = peso
        self.contador = contador
        self.vidas = vidas
        self.estado_actual = estado_actual
        self.habilidad = habilidad

        print(f"Nombre del Personaje: {self.nombre}")
        print(f"Especie del Personaje: {self.especie}")
        print(f"Color del Personaje: {self.color}")
        print(f"Velocidad del Personaje: {self.velocidad}")
        print(f"Altura del Personaje: {self.altura}")
        print(f"Peso del Personaje: {self.peso}")
        print(f"Contador del Personaje: {self.contador}")
        print(f"Vidas del Personaje {self.vidas}")
        print(f"Estado actual del Personaje: {self.estado_actual}")
        print(f"Habilidad del Personaje: {self.habilidad}")

    def correr(self):
        print(f"El personaje esta corriendo")
    def saltar(self):
        print(f"El personaje esta saltando")
    def frenar(self):
        print(f"Esta frenando el personaje")
    def rodar(self):
        print(f"Esta rodando el personaje")
    def agacharse(self):
        print(f"Esta agachandose el personaje")

sonic = PersonajedelJuego(
    "Sonic","Erizo","Azul","Supersonica",
    "1 metro","35 kg","50","3 Vidas","vivo",
    "Spind Bash"
)

sonic.correr()
sonic.saltar()
sonic.frenar()
sonic.rodar()
sonic.agacharse()