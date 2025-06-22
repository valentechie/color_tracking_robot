# Shell Scripting

### *Scripts* de Shell
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

### Control de Flujo y otros elementos
- **Sentencia if**: comienza con **if**, luego sigue **elif** o **else** y termina con **fi**
```bash
#!/bin/bash

### Control de Flujo y otros elementos

# Definimos la ruta al archivo directamente usando $HOME
archivo="$HOME/Escritorio/example.txt"

# Comprobamos si el archivo existe
if [ -f $archivo ]; then
    echo "El archivo $archivo existe."

    # Contar líneas que contengan la palabra 'error'
    errores=$(grep -i "error" $archivo | wc -l)

    # Evaluar si hay errores
    if [ "$errores" -gt 0 ]; then
        echo "Se encontraron $errores líneas con 'error'."
    else
        echo "No se encontraron errores en el archivo."
    fi

elif [ -d "$archivo" ]; then
    echo "$archivo es un directorio, no un archivo."

else
    echo "El archivo $archivo no existe."
    echo "Creando archivo de ejemplo..."
    mkdir -p "$HOME/Escritorio"
    echo "Este es un archivo de ejemplo sin errores." > $archivo
    echo "Archivo creado: $archivo"
fi
```
- **Sentencia case (switch)**: empieza con **case** y termina con **esac**
```bash
#!/bin/bash

# Pedimos una acción al usuario
echo "¿Qué quieres hacer? (crear, borrar, listar)"
read accion

# Evaluamos la acción usando 'case'
case $accion in
    crear)
        echo "Creando archivo de ejemplo..."
        touch ejemplo.txt
        echo "Archivo ejemplo.txt creado."
        ;;
    
    borrar | eliminar)
        echo "Borrando archivo de ejemplo..."
        rm -f ejemplo.txt
        echo "Archivo ejemplo.txt eliminado (si existía)."
        ;;

    listar)
        echo "Mostrando archivos en el directorio actual:"
        ls -lh
        ;;

    *)  # patrón por defecto si no coincide con ninguno
        echo "Opción no reconocida: $accion"
        echo "Opciones válidas: crear, borrar/eliminar, listar"
        ;;
esac
```
