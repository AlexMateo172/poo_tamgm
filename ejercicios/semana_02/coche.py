class Coche:
    
    def __init__(self, tipo, marca, modelo, año, motor, color, transmision, placa):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.motor = motor
        self.color = color
        self.transmision = transmision
        self.placa = placa
        
      
        print(f"Tipo de Coche: {self.tipo}")
        print(f"Marca del Coche: {self.marca}")
        print(f"Modelo del Coche: {self.modelo}")
        print(f"Año del Coche: {self.año}")
        print(f"Motor del Coche: {self.motor}")
        print(f"Color del Coche: {self.color}")
        print(f"Transmisión: {self.transmision}")
        print(f"Placa del Coche: {self.placa}") 
        
    def encender(self):
        print("Estoy encendiendo el coche")
        """
        Este metodo se encarga de iniciar el motor de el coche, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def apagar(self):
        print("Estoy apagando el coche")
        """
        Este metodo realiza la accion de apagar el motor de el coche, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def acelerar(self):
        print("Estoy acelerando el coche") 
        """
        Este metodo incrementa la velocidad de el coche, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def derrapar(self):
        print("Estoy derrapando el coche")
        """
        Este metodo simula la perdida de traccion de el coche al deslizarse, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def cambiarvelocidad(self):
        print("Estoy cambiando de velocidad")  
        """
        Este metodo realiza el cambio de marcha o velocidad de el coche, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """  
    def tocarclaxon(self):
        print("Estoy tocando el claxon del coche")  
        """
        Este metodo emite el sonido de advertencia de el claxon del coche, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """                



mustang_del_96_gt = Coche(
    "Deportivo", "Ford", "Mustang GT", "1996", "V8 4.6L", "Rojo Cobalto", "Manual", "ust-96-u8"
)


mustang_del_96_gt.encender()
mustang_del_96_gt.apagar()
mustang_del_96_gt.acelerar()
mustang_del_96_gt.derrapar()
mustang_del_96_gt.cambiarvelocidad()
mustang_del_96_gt.tocarclaxon()