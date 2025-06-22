#!/bin/bash

# Definiendo variables
num1=$1
num2=$2

# Operaciones
suma=$(($num1+$num2))
resta=$(($num1 - $num2))
producto=$(($num1 * $num2))

# Visualización de resultados
echo "La suma de $num1 y $num2 es igual a $suma"
echo "La resta de $num1 menos $num2 es igual a $resta"
echo "El producto de $num1 y $num2 es igual a $producto"

exit 0
