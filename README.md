# Repositorio de Programación Orientada a Objetos con Python

Repositorios con ejercicios de Programacion orientada a Objetos

## 1. Crear .gitignore

Crear el archivo .gitignore para comfigurar los archivos y carpetas que no deseamos que se guardan en el repositorio

 ````shell
 *.pyc
 _pycache_/
 ````

 ## 2. Indexar archivos y carpetas

 Indexa todos los directorios y carpetas en busca de archivos nuevos

 ````shell
 git add .
 ````

 ## 3. Crear un COMMIT

 Crea un commit o punto de control de los cambios realizados en el proyecto.

 ````shell
 git commit -m "CREATED .gitignore"
 ````

 * CREATED - Se crearon nuevas carpetas o arcivos.
 * UPDATED - Se actualizaron o agregaron nuevas funciones.
 * FIXED - Se corrigieron errores.

 ## 4. Realizar el COMMIT

 Sincroniza los cambios realizados en el repositorio.

 ````shell
 git push -u origin main
 ````

 ##5. Agregar Documentacion a los metodos

 Agregar un **Docstring** a los metodos generados

 ````python
(""")  def metodoDos(self, variable_uno, variable_dos:float)->int:
        
     Este metodo recibe 2 variables enteras, las suma y regresa 
     el resultado de la suma se enfoca en los metodos de el codigo

     : args - Argumentos

     variable_uno : int - Primer numero entero - Ejemplo de Argumentos
     variable_dos : int - Segundo numero entero - Ejemplo de Argumentos

     Return: - Regresa el resultado de los argumentos

      suma =variable_uno + variable_dos - suma las dos variables
      return int(suma) - El resturn regresa el resultado el int dicta que sea entero osea la suma un numero entero
(""")
   

````        
