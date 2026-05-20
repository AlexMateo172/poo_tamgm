class NombreClase:

    def __init__(self):
        print("Constructor")

    def metodoUno(self):
        print("Meotodo Uno") 
    
    def metodoDos(self, variable_uno, variable_dos:float)->int:
        """
        Este metodo recibe 2 variables enteras, las suma y regresa 
        el resultado de la suma

        :args

        variable_uno : int - Primer numero entero
        variable_dos : int - Segundo numero entero

        Return:

        suma : int - Suma de los dos numeros enteros

        """
        suma =variable_uno + variable_dos
        return int(suma)       
   
    def metodoTres(self, variable_tres:str)->None:
        print(f"Numero de Caracteres: {len(variable_tres)}")

nombre_objeto = NombreClase()
nombre_objeto.metodoUno()
