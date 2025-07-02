#!/bin/bash

FILE=$1

if [ ! -f $FILE ]; then
	echo "Uso: $0 archivo"
	exit 1
fi

echo "===Nombre de los estudiantes==="
awk '{ print $1 }' $FILE

echo -e "\n===Promedio de los estudiantes"
awk '{  nombre = $1
	suma = $2 + $3 + $4
	promedio = suma / 3
	print nombre " tiene un promedio de: " promedio
     }' $FILE

echo -e "\n===Ordenados alfabeticamente==="
sort $FILE

echo -e "\n===Ordenados por promedio==="
awk '{	nombre = $1
	suma = $2 + $3 +$4
	promedio = suma/3
	print nombre ": " promedio
	}' $FILE | sort -nr

exit 0
