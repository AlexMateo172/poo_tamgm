class Telefono:
     
    def __init__(self, marca, modelo, capacidad_de_bateria, sistema_operativo, almacenamiento, color, resolucion_de_pantalla, memoria_ram, procesador, refrigeracion):
          
        
        
        self.marca = marca
        self.modelo = modelo
        self.capacidad_de_bateria = capacidad_de_bateria
        self.sistema_operativo = sistema_operativo
        self.almacenamiento = almacenamiento
        self.color = color
        self.resolucion_de_pantalla = resolucion_de_pantalla
        self.memoria_ram = memoria_ram
        self.procesador = procesador
        self.refrigeracion = refrigeracion

        print(f"Marca del Telefono: {self.marca}")
        print(f"Modelo del Telefono: {self.modelo}")
        print(f"Capacidad de la Bateria: {self.capacidad_de_bateria}")
        print(f"Sistema Operativo: {self.sistema_operativo}")
        print(f"Almacenamiento del Telefono: {self.almacenamiento}")
        print(f"Color del Telefono{self.color}")
        print(f"Resolucion de Pantalla: {self.resolucion_de_pantalla}")
        print(f"Memoria Ram: {self.memoria_ram}")
        print(f"Procesador: {self.procesador}")
        print(f"Refrigeracion: {self.refrigeracion}")

    def encender(self):    
        print(f"Estoy encendiendo el Telefono")
        """
        Este metodo se encarga de iniciar el sistema de el Telefono, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def apagar(self):
        print(f"Estoy apagando el Telefono")
        """
        Este metodo realiza la accion de apagar el sistema de el Telefono, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def navegar(self):
        print(f"Estoy navegado el Telefono")
        """
        Este metodo permite explorar la red a traves de el Telefono, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def ejecutando(self):
        print(f"Estoy ejecutando una Aplicacion")
        """
        Este metodo inicia y corre una tarea dentro de el Telefono, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def cargar(self):
        print(f"Estoy cargando mi tekefono")
        """
        Este metodo conecta el Telefono para suministrarle energia, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def tomarFotos(self):
        print(f"Estoy tomando fotos")
        """
        Este metodo utiliza la camara de el Telefono para capturar imagenes, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def enviarMensajes(self):
        print(f"Estoy enviando mensajes")
        """
        Este metodo transmite texto o informacion desde el Telefono, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def hacerLlamadas(self):
        print(f"Estoy haciendo una Lamada")
        """
        Este metodo enlaza una comunicacion por voz usando el Telefono, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def refrigerar(self):
        print(f"Se esta refrigerando el telefono")
        """
        Este metodo reduce la temperatura interna de el telefono, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def procesar(self):
        print(f"Esta procesando el Telefono")
        """
        Este metodo ejecuta las operaciones logicas y calculos de el Telefono, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """


redmagic9_pro = Telefono(
    "Nubia","Red Magic 9 Pro","6500mah","Redmagicios",
    "256 GB","Negro","1116 x 2480px","12 ram","Snapdragon 8 gen3",
    "Ventilador fisico interno"
    )                                            
       
redmagic9_pro.encender()
redmagic9_pro.apagar()
redmagic9_pro.navegar()
redmagic9_pro.ejecutando()
redmagic9_pro.cargar()
redmagic9_pro.tomarFotos()
redmagic9_pro.enviarMensajes()
redmagic9_pro.hacerLlamadas()
redmagic9_pro.refrigerar()
redmagic9_pro.procesar()