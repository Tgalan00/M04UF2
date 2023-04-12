#!/usr/bin/python3

archivo = open("numeritos.txt")

linea = archivo.readline()

lista = linea.split(";")

print(lista[2])

archivo.close()

archivo = open("textitos.txt", "w")

archivo.write("ola que ase")

archivo.close()

diccionario = {

	"nombre": "Guillermo",
	"apellido": "Granjero",
	"altura": 1.1

}

print(diccionario["altura"])
