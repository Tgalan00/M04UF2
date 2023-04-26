#!/usr/bin/python3
import xmltodict

def obten_datos ():
	print("Crea un enemigo")
	print("---------------")
	nombre = input("Por favor ingrese el nombre del personaje: ")
	strength = int(input("Por favor ingrese la fuerza del personaje: "))
	health = int(input("Por favor ingrese la vida del personaje: "))
	
	return {
			"name": nombre, 
			"damage": strength,
			"health": health
		}

exit = 0
enemyArray = []


while exit != 1:
	exit = int(input("¿Quieres añadir un enemigo? --> 0 == SÍ | 1 == NO : "))
	if exit == 0:
		enemy = obten_datos()
		enemyArray.append(enemy)

	elif exit == 1:
		print("Decidiste salir, ondá a tomar chocomel!")
	else:
		print("No es un numero válido")

enemies_export = {
	"enemies": {
	"enemy": enemyArray
	}
}


for e in enemyArray:
	enemy_xml = xmltodict.unparse(e, pretty=True)
	archivoXML = open("enemyCreado.xml", mode="a")
	archivoXML.write(enemy_xml)

archivoXML.close()
