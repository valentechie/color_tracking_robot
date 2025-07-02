#!/bin/bash

while [ "$opc" != "4" ]; do
	echo -e "\nSeleccione una opcion: "
	echo "1) Listar información detallada"
	echo "2) Listar solo ficheros .txt"
	echo "3) Listar solo ficheros .rtf"
	echo "4) Salir"
	read -p "Opcion: " opc

	case $opc in
	1)
		ls -l
		;;
	2)
		echo "Ficheros .txt: "
		ls -l *.txt 2>/dev/null || echo "No hay ficheros .txt"
		;;
	3)
		echo "Ficheros .rtf: "
		ls -l *.rtf 2>/dev/null || echo "No hay ficheros .rtf"
		;;
	4)
		echo "Saliendo del programa"
		exit 0
		;;
	*)
		echo "Error de uso, intente de nuevo"
		;;
	esac
done

exit 0
