class Universidad:
    def __init__(self, logo, oferta_educativa, localidad, sistema_informativo, modalidad, servicios, ubicacion, talleres, cantidad_salones, rector):
    
        self.logo = logo
        self.oferta_educativa = oferta_educativa
        self.localidad = localidad
        self.sistema_informativo = sistema_informativo
        self.modalidad = modalidad
        self.servicios = servicios
        self.ubicacion = ubicacion
        self.talleres = talleres
        self.cantidad_salones = cantidad_salones
        self.rector = rector

        print(f"Logotipo de la Universidad: {self.logo}")
        print(f"Oferta educativa: {self.oferta_educativa}")
        print(f"Localidad: {self.localidad}")
        print(f"Sistema Informativo: {self.sistema_informativo}")
        print(f"Modalidad: {self.modalidad}")
        print(f"Servicios:  {self.servicios}")
        print(f"Ubicacion: {self.ubicacion}")
        print(f"Talleres: {self.talleres}")
        print(f"Salones: {self.cantidad_salones}")
        print(f"Rector {self.rector}")

    def enseñar(self):
        print(f"Me estan enseñando en la Universidad")
    def aprender(self):
        print(f"Estoy aprendiendo en la Universidad")
    def estudiar(self): 
        print(f"Estoy Estudiando para la Universidad")
    def practicar(self):
        print(f"Estoy Practicando para la Universidad")
    def capacitar(self):
        print(f"Me estoy capacitando para la Universidad")

unideh = Universidad("Logo.jpg","Ing.Software,Turismo Alternativo","San Miguel","CADU",
                     "Virtual","Biblioteca digital","Santa Caterina",None,None,
                     "Octacvio castillo"
                      )                       
unideh.enseñar()
unideh.aprender()
unideh.estudiar()
unideh.practicar()
unideh.capacitar()