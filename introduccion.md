# Órdenes básicas
## Uso básico de la Shell
- **ls**: Lista el contenido de un directorio (ficheros y subdirectorios)
	- **ls -l**: Salida más larga
- **cd**: Cambia de directorio (va al home)
- **mkdir**: Crea directorios
	- **mkdir ~/fpi**: crea la carpeta en home 
- **exit**: Finaliza la Shell actual
- **clear**: Limpia la terminal
- **cat > file** y **nano file**: Creación y modificación de ficheros
- **more file** y **cat file**: Muestran el contenido de un fichero
- **wc file**: Muestra el número de líneas, palabras y caracteres
- **cut**: Trocea un fichero en los rangos indicados
- **head**: Muestra el principio de un fichero
- **tail**: Muestra el final de un fichero
- **grep "patron" file**: Busca un patrón en un fichero (muestra la línea)
- **sort file**: Ordena un conjunto de caracteres
- **mv**: Mueve un fichero a otro lugar

------------------------------------
## Uso básico del Command-Line Interface
- **Foreground**: Ejecución de órdenes externas interactivas, **(fg)**: trae a primer plano un proceso que estaba en segundo plano
- **Background**: Programa no interactivo (&), **(bg)**: pasa a segundo plano un proceso suspendido (Ctrl+Z)
- **jobs**: Lista los procesos que se están ejecutando en segundo plano
- **kill %(n de tarea)**: Termina la ejecución de un proceso en background

### Variables y aritmética
- **Operaciones**: ``$((expresión))``
	- ``$ hola_mundo="Hola mundo"``			# debe estar todo junto
 	- ``$ echo $hola_mundo``			# imprime en pantalla el contenido de la variable, similar a *print*
- **Órdenes**: ``$(orden)``
	- ``nombre=$(whoami)``
 	- ``echo $nombre``				# Devuelve valentechie  
- **Export**: Convierte una variable normal en una variable de entorno ``export``
- **Expansión de nombres de ficheros**: ``ls ^a?[a-zA-Z]*.txt$``
	- ``*``: corresponde a *'cualquier cadena de caracteres'*
 	- ``?``: corresponde a *'cualquier carácter'*
  	- ``[conjunto]``: corresponde a *'cualquier carácter dentro del conjunto'*
  	- ``^``: corresponde a *'empieza por'*
  	- ``$``: corresponde a *'termina por'*

### Redirecciones
- **Descriptores de ficheros**:
	- h





 
