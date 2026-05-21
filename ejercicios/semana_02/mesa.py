class Mesa:
    def __init__(self, tipo_madera, color, largo, ancho, altura, peso, capacidad_personas, grosor_tablon, estilo, precio):

        self.tipo_madera = tipo_madera
        self.color = color
        self.largo = largo
        self.ancho = ancho
        self.altura = altura
        self.peso = peso
        self.capacidad_personas = capacidad_personas
        self.grosor_tablon = grosor_tablon
        self.estilo = estilo
        self.precio = precio

        print(f"Tipo de Madera: {self.tipo_madera}")
        print(f"Color de la Mesa: {self.color}")
        print(f"Largo de la Mesa: {self.largo}")
        print(f"Ancho de la Mesa: {self.ancho}")
        print(f"Alto de la Mesa: {self.altura}")
        print(f"Peso de la Mesa: {self.peso}")
        print(f"Capacidad de Personas: {self.capacidad_personas}")
        print(f"Grosor de la Mesa {self.grosor_tablon}")
        print(f"Estilo de la Mesa: {self.estilo}")
        print(f"Precio de la Mesa: {self.precio}")

    def armar(self):
        print(f"Estoy armando la Mesa")
        """
        Este metodo se encarga de ensamblar las partes de la Mesa, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def desarmar(self):
        print(f"Estoy desarmando la Mesa")
        """
        Este metodo realiza la accion de separar las piezas de la Mesa, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def soportar(self):
        print(f"Yo soporto la Mesa")
        """
        Este metodo simula la funcion de sostener objetos sobre la Mesa, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def limpiar(self):
        print(f"Yo limpio la Mesa")
        """
        Este metodo realiza la accion de quitar la suciedad de la Mesa, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def mover(self):
        print(f"Yo muevo la Mesa")
        """
        Este metodo permite cambiar de lugar o desplazar la Mesa, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """

mesa_comedor_imperial = Mesa(
    "Roble Europeo","Marron","3 Metros" ,"1,2 metros",
    "0.83 metros","120 kg","12 personas","5 cm","Rustico",
    "15000 pesos"
)

mesa_comedor_imperial.armar()
mesa_comedor_imperial.desarmar()
mesa_comedor_imperial.soportar()
mesa_comedor_imperial.limpiar()
mesa_comedor_imperial.mover()  