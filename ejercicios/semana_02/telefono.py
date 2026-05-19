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
    def apagar(self):
        print(f"Estoy apagando el Telefono")
    def navegar(self):
        print(f"Estoy navegado el Telefono")
    def ejecutando(self):
        print(f"Estoy ejecutando una Aplicacion")
    def cargar(self):
        print(f"Estoy cargando mi tekefono")
    def tomarFotos(self):
        print(f"Estoy tomando fotos")
    def enviarMensajes(self):
        print(f"Estoy enviando mensajes")
    def hacerLlamadas(self):
        print(f"Estoy haciendo una Lamada")
    def refrigerar(self):
        print(f"Se esta refrigerando el telefono")
    def procesar(self):
        print(f"Esta procesando el Telefono")


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