class Transporte:
    
    def __init__(self, tipo, marca, modelo, tipo_de_combustible, capacidad_de_pasajeros, estado, velocidad_actual, color, uso, numero_de_ruedas):
        
       
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.tipo_de_combustible = tipo_de_combustible
        self.capacidad_de_pasajeros = capacidad_de_pasajeros
        self.estado = estado
        self.velocidad_actual = velocidad_actual
        self.color = color
        self.uso = uso 
        self.numero_de_ruedas = numero_de_ruedas
        
       
        print(f"Tipo de Transporte: {self.tipo}")
        print(f"Marca de Transporte: {self.marca}")
        print(f"Modelo de Transporte: {self.modelo}")
        print(f"Tipo de Combustible: {self.tipo_de_combustible}")
        print(f"Capacidad de Pasajeros: {self.capacidad_de_pasajeros}")
        print(f"Estado de Transporte: {self.estado}")
        print(f"Velocidad Actual: {self.velocidad_actual}")
        print(f"Color de Transporte: {self.color}")
        print(f"Uso de Transporte: {self.uso}")
        print(f"Numero de Ruedas: {self.numero_de_ruedas}")
   
    def arrancar(self):
        print(f"Estoy arrancando el autobus")
    def acelerar(self):
        print(f"Estoy acelerando el autobus")
    def frenar(self):
        print(f"Estoy Frenando el autobus") 
    def girar(self):
        print(f"Yo estoy girando el autobus")
    def apagar(self):
        print(f"Yo apago el autobus")                  

autobus = Transporte(
    "Autobus Dao", "Terrestre", "Mercedes", "Diesel", 
    "44 pasajeros", "En ruta", "90 km\h", "Blanco con Rojo", "Publico", "6 Ruedas"
)

autobus.arrancar()
autobus.acelerar()
autobus.frenar()
autobus.girar()
autobus.apagar()