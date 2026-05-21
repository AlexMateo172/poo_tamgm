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
        """
        Este metodo incrementa el movimiento para que El personaje corra, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def saltar(self):
        print(f"El personaje esta saltando")
        """
        Este metodo realiza la accion de elevarse para que El personaje salte, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def frenar(self):
        print(f"Esta frenando el personaje")
        """
        Este metodo se encarga de detener el movimiento de el personaje, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def rodar(self):
        print(f"Esta rodando el personaje")
        """
        Este metodo hace que el personaje gire sobre su propio eje rodando, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def agacharse(self):
        print(f"Esta agachandose el personaje")
        """
        Este metodo reduce la altura de el personaje al agacharse, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """

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