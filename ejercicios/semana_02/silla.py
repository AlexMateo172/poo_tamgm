class Silla:
    def __init__(self, tipo_madera, color, altura_total, altura_asiento, ancho, peso_silla, capacidad_carga, material_cojin, estilo, precio):

        self.tipo_madera = tipo_madera
        self.color = color
        self.altura_total = altura_total
        self.altura_asiento = altura_asiento
        self.ancho = ancho
        self.peso_silla = peso_silla
        self.capacidad_carga = capacidad_carga
        self.material_cojin = material_cojin
        self.estilo = estilo
        self.precio = precio

        print(f"Tipo de Madera: {self.tipo_madera}")
        print(f"Color de la Silla: {self.color}")
        print(f"Altura Total: {self.altura_total}")
        print(f"Ancho del Asiento: {self.altura_asiento}")
        print(f"Ancho de la Silla: {self.ancho}")
        print(f"Peso de la Silla: {self.peso_silla}")
        print(f"Capacidad de Carga: {self.capacidad_carga}")
        print(f"Material del cojin {self.material_cojin}")
        print(f"Estilo de la Silla: {self.estilo}")
        print(f"Precio de la Silla: {self.precio}")

    def equilibrar(self):
        print(f"Estoy equilibrando la Silla")
    def pintar(self):
        print(f"Estoy pintando la silla")
    def reparar(self):
        print(f"Estoy reparando la silla")
    def tapizar(self):
        print(f"Estoy tapizando la silla")
    def barnizar(self):
        print(f"Estoy barnizando la silla")

silla_comedor_imperial = Silla(
    "Roble Europeo","Marron","1.10 Metros","0.45 metros",
    "0.50 metros","8 kg","150 kg","Cuero Sintetico","Rustico",
    "1500 pesos"
)

silla_comedor_imperial.equilibrar()
silla_comedor_imperial.pintar()
silla_comedor_imperial.reparar()
silla_comedor_imperial.tapizar()
silla_comedor_imperial.barnizar()  