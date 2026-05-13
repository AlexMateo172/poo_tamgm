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