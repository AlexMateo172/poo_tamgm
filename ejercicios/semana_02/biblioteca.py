class LibrodeBiblioteca:
    
    def __init__(self, titulo, editorial, genero, disponibilidad, idioma, año_de_publicacion, estado_fisico, cantidad_de_paginas, tipo_de_tipografia, clasificacion):
        
       
        self.titulo = titulo
        self.editorial = editorial
        self.genero = genero 
        self.disponibilidad = disponibilidad
        self.idioma = idioma
        self.año_de_publicacion = año_de_publicacion
        self.estado_fisico = estado_fisico
        self.cantidad_de_paginas = cantidad_de_paginas
        self.tipo_de_tipografia = tipo_de_tipografia
        self.clasificacion = clasificacion
        
       
        print(f"Título del Libro: {self.titulo}")
        print(f"Editorial del Libro: {self.editorial}")
        print(f"Género del Libro: {self.genero}")
        print(f"Disponibilidad del Libro: {self.disponibilidad}")
        print(f"Idioma del Libro: {self.idioma}")
        print(f"Año de Publicación: {self.año_de_publicacion}")
        print(f"Estado Físico del Libro: {self.estado_fisico}")
        print(f"Cantidad de Páginas: {self.cantidad_de_paginas}")
        print(f"Tipo de Tipografía: {self.tipo_de_tipografia}")
        print(f"Clasificación del Libro: {self.clasificacion}")
        
    def leer(self):
        print(f"Estoy leyendo el Libro")
        """
        Este metodo simula la accion de leer el contenido de el Libro, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def abrir(self):
        print(f"Estoy leyendo el Libro")
        """
        Este metodo realiza la accion de abrir el Libro para su uso, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def aprender(self):
        print(f"Estoy aprendiendo del Libro")
        """
        Este metodo permite adquirir conocimientos a partir de el Libro, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def pensar(self):
        print(f"Estoy pensando con el Libro")
        """
        Este metodo simula el proceso de reflexionar utilizando la informacion de el Libro, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def comprender(self):
        print(f"Estoy comprendiendo con el Libro")                
        """
        Este metodo se encarga de entender y asimilar las ideas de el Libro, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
los_hornos_de_hitler = LibrodeBiblioteca(
    "Los Hornos de Hitler", "Olga Lengyel", "Crónica", "Disponible", 
    "Español", "1947", "Gastado-Sucio", "270", "serif", "+18"
)

los_hornos_de_hitler.leer()
los_hornos_de_hitler.abrir()
los_hornos_de_hitler.aprender()
los_hornos_de_hitler.pensar()
los_hornos_de_hitler.comprender()