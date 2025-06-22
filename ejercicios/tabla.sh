#!/bin/bash

# Definimos la variable
num=$1

# Realizamos multiplicaciones
for numero in {0..10}; do
	resultado=$(($num*$numero))
	echo "$numero x $num = $resultado"
done

exit 0
