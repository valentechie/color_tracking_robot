# Shell Scripting

## Scripts para Bourne Again Shell (bash)
- ``#!/bin/bash/sh``: Programa interpretado mediante el mecanismo **hash bang** (#!)
- ``bash -x file.sh``: Ejecuta el programa paso a paso para detectar errores
- **POSIX**: Conjunto de **características comunes** a todas las Shell

### Ejecución de scripts de Shell
- **``chmod +x script.sh``**: Para dar permisos de ejecución
- **``exit 0``**: Para comprobar que haya finalizado correctamente
- **$?**: Muestra el estado con el que acabó la ejecución del último comando

### Parámetros posicionales
- **$0**: nombre del script
- **$#**: numero de parámetros (no cuenta el cero)
- **$***: parámetros posicionales
- **$@**: devuelve los parámetros separados en varias cadenas
- **shift**: desplaza los parámetros, **$3 ==> $2** y actualiza **$#**

### Control de Flujo
- **Sentencia if**: comienza con **if**, luego sigue **elif** o **else** y termina con **fi**
```bash
#!/bin/bash

archivo="$HOME/Escritorio/example.txt"

if [ -f $archivo ]; then
    if [ -r $archivo ]; then
        echo "El archivo $archivo existe y es legible."
    else
        echo "El archivo $archivo existe, pero no tienes permiso de lectura."
    fi
elif [ -d "$archivo" ]; then
    echo "$archivo es un directorio, no un archivo."
else
    echo "El archivo $archivo no existe."
fi
```
- **Sentencia case (switch)**: empieza con **case** y termina con **esac**
```bash
#!/bin/bash

# Script de menú usando 'case'

echo "Elige una opción:"
echo "1) Mostrar la fecha"
echo "2) Mostrar el contenido del directorio actual"
echo "3) Salir"

read opcion

case "$opcion" in
    1)
        echo "Fecha actual:"
        date
        ;;
    2)
        echo "Contenido del directorio:"
        ls -lh
        ;;
    3)
        echo "Saliendo del programa. ¡Hasta luego!"
        ;;
    *)  # Valor por defecto si no coincide con ningún caso
        echo "Opción no válida. Debes elegir entre 1 y 4."
        ;;
esac
```
- **Sentencia while**: empieza con **while**, luego sigue **do** y termina con **done**
```bash
#!/bin/bash

# Contador desde 1 hasta un número que indique el usuario

echo "¿Hasta qué número quieres contar?"
read limite

contador=1

while [ "$contador" -le "$limite" ]; do
    echo "Contando: $contador"
    contador=$((contador + 1))
done

echo "¡Listo! Contamos hasta $limite."
```
- **Sentencia for**: empieza con **for...in**, luego sigue **do** y termina con **done**
```bash
#!/bin/bash

# Script que cuenta las líneas de todos los archivos .txt en el directorio actual

echo "Analizando archivos .txt en el directorio actual..."

for archivo in *.txt; do
    if [ -f "$archivo" ]; then
        lineas=$(wc -l < "$archivo")
        echo "$archivo: $lineas líneas"
    else
        echo "No hay archivos .txt para analizar."
    fi
done
```

### Otros elementos
- **``read``**: permite leer una línea desde su entrada estandar y guardarla en una variable que pasa como argumento
- **``IFS``**: contiene los caracteres reconocidos como separadores entre campos **\t**: tabulador, **\n**: salto de línea, **''**: espacio en blanco
- **``alias <nombre> = <comandos>``**: Define una etiqueta para invocar un comando o conjunto de comandos
- **Uso de test**:
    - **test (ficheros)**: ``-f fichero`` (existe), ``-d directorio`` (existe), ``-e fichero`` (comprueba si existe ya sea fichero o no)
    - **test (cadenas)**: ``-n string`` (longitud != 0), ``-z string`` (longitud = 0), ``str1 = str2`` (iguales), ``str1 != str2`` (diferentes), ``string`` (cadena no nula)
    - **test (enteros)**: 
        - ``int1 -eq int2`` **(iguales)**
        - ``int1 -ne int2`` **(diferentes)**
        - ``int1 -gt int2`` **(mayor que)**
        - ``int1 -ge int2`` **(mayor o igual que)**
        - ``int1 -lt int2`` **(menor que)**
        - ``int1 -le int2`` **(menor o igual que)**
- **Sintaxis para test**: ``[ $a -eq $b ] == test $a -eq $b``
- **``bc``**: Permite realizar operaciones que involucran números enteros, ``echo "3+4" | bc``
- **``du -a y find .``**: Para recorrer un árbol de ficheros
- **``join``**: Calcula la intersección de valores presentes en dos columnas previamente ordenadas
- **``xargs``**: Usa lo que nos viene por la entrada estándar como argumento de entrada al ejecutar otro comando

------------------------------------

## Filtros y expresiones regulares
### Filtros útiles
- ``sort``: Ordena las líneas de diversas formas
- **Comandos de filtros**:
    - ``uniq``: Elimina las líneas contiguas repetidas
    - ``head``: Primeras líneas 
    - ``tail``: Últimas líneas
- **Comparación de ficheros**: 
    - ``diff``: Fichero de texto línea a línea
    - ``vimdiff``: Version mejorada, más visual
    - ``cmp``: Ficheros binarios byte a byte
- ``tr``: Traductor un conjunto de caracteres, ``-d``: Borra el conjunto de caracteres pasado como argumento

### Expresiones regulares
- **.** Cualquier caracter
- **[conjunto]**: Cualquier caracter dentro del conjunto
- **[^conjunto]**: Cualquier caracter que no esté dentro del conjunto
- **^**: Principio de línea
- **$**: Final de línea
- **exp***: aparece cero o más veces
- **exp+**: una o más veces
- **exp$**: cero o una vez
- **(exp)**: agrupa
- \ **barra inclinada**: evita que un simbolo pierda su significado especial
- **|**: condición lógica OR
- ``egrep``: Filtra lineas usando expresiones regulares

### SED
- ``sed (opciones)``:
    - **-E**: uso de regex extendidas
    - **q**: sale del programa
    - **d**: borra la linea
    - **p**: imprime la linea
    - **r**: lee e inserta un fichero
    - **s**: sustituye
- ``sed (direcciones)``:
    - **número**: actúa en la línea numero
    - **/ /**: lineas que coinciden con exp
    - **$**: última linea 
- ``sed (intervalos)``:
    - **numero,numero**: de linea numero hasta linea numero
    - **numero,$**: desde linea numero hasta la ultima linea
    - **numero,/ /**: desde la linea numero hasta la primera linea que encaja con exp

- ``sed -E '3,6d'``: borra la linea desde 3 hasta 6
- ``j
  
### AWK
