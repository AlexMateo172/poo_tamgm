class Alumno:
    def __init__(self, nombre, matricula, carrera, cuatrimestre, promedio_general, edad, correo, universidad, estado_inscripcion, cantidad_materias):
       
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.cuatrimestre = cuatrimestre
        self.promedio_general = promedio_general
        self.edad = edad
        self.correo = correo
        self.universidad = universidad
        self.estado_inscripcion = estado_inscripcion
        self.cantidad_materias = cantidad_materias
        
       
        print(f"Nombre del Alumno: {self.nombre}")
        print(f"Matrícula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        print(f"Cuatrimestre: {self.cuatrimestre}")
        print(f"Promedio General del Alumno: {self.promedio_general}")
        print(f"Edad del Alumno:{self.edad}")
        print(f"Correo del Alumno: {self.correo}")
        print(f"Universidad del Alumnio: {self.universidad}")
        print(f"Estado de Inscripcion del Alumno: {self.estado_inscripcion}")
        print(f"Cantidad de Materias: {self.cantidad_materias}")
    
    def administrar_actividades(self):
        print("Estoy administrando mis actividades")
    """
        Este metodo se encarga de gestionar y organizar las tareas diarias, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def estudiar(self):
        print("Estoy estudiando")
    """
        Este metodo simula la accion de repasar o adquirir conocimientos, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """    

    def hacer_tarea(self):
        print("Estoy haciendo la tarea")
    """
        Este metodo realiza las obligaciones academicas o pendientes asignados, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def preguntar_dudas(self):
        print("Estoy preguntando mis dudas")
    """
        Este metodo permite resolver las inquietudes o preguntas pendientes, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
    def realizar_examen(self):
        print("Estoy realizando un examen")
    """
        Este metodo ejecuta la evaluacion de los conocimientos adquiridos, se enfoca en los metodos de el codigo
        
        : args - Argumentos
        
        Ninguno : - No recibe parametros de entrada
        
        Return: - No regresa ningun valor, solo imprime un mensaje en pantalla
        """
   


mateo = Alumno(
    "Mateo","17200","TIC","2do Cuatrimestre",
    "9.5","19","mateo@alumno","UTEC tulancingo",
    "Activo","7"
   
)


mateo.administrar_actividades()
mateo.estudiar()
mateo.hacer_tarea()
mateo.preguntar_dudas()
mateo.realizar_examen()
