#!/usr/bin/python3


#importamos enemies_clas y player_class
from enemies_class import Enemies
from player_class import Player

#inicializamos la variable en 0 para que sea global
choosejsonxml = 0
#inicializamos tambien para situarnos con el primer jugador
player = Player(0)
#Declaramos dos variables diferentes para Enemies para que detecte que formato hemos escogido si es con json o xml
enemigosjson = Enemies(choosejsonxml)
enemigosxml = Enemies(choosejsonxml)

#Declaramos la variable para ir ubicando el enemigo en el que estamos
current_enemy = 0

#Declaramos la primera funcion para hacer el juego con el formato json


def juegojson (enemigou):
#Declaramos el conjunto de variables que usaremos para realizar el programa
	exit =  False
	global guardar
	guardar = 1
	current_enemy = enemigou

#Hacemos un bucle que no finalizará hasta que exit sea True
	while not exit:

#LLamamos a las dos funciones que es tan en las clases Enemies y Player
		enemykill = enemigosjson.muerte(current_enemy)
		badending = player.dead()


#Hacemos las 3 distintas combinaciones que podemos tener segun la vida del enemigo o la del jugador
		if enemykill:
			current_enemy = current_enemy + 1

			print("\nFelicidades te has cargao al bicho")
			print("")

		if badending < 0:
			print("\nHas muerto, vuelve a intentarlo")
			print("")
			break

		if current_enemy >= 3:
			print("\nFelicidades loquete, has derrotado a todos los bichos y has ganado la partida")
			print("")

			break

#Aqui empieza el proceso de que atacan al jugador y al enemigo
#Mostraremos al usuario el enemigo al que se ha de enfrentar
		print("\nTe ataca un enemigo: ")
		enemigosjson.show_info(current_enemy)

#Damos a elegir al usuario si quiere atacar o guardar partida

		opcion = input("Quieres atacar (1) o guardar (A)? ")

#Aqui simplemente salimos del bucle ya que realmente el formato ya lo guardamos cuando escoge si quiere guardar al principio con json o xml

		if opcion == "A":
			print("\nGuardando: ")
			print("")
			break


#Ataca al enemigo y el jugador tambien es atacado

		if opcion == "1":
			danio = player.attack()
			print("\nPUM! Atacas al enemigo, le has quitado "+str(danio))
			print("")

			danioenemy = enemigosjson.hurt(danio,current_enemy)
			ataquenemigo = enemigosjson.attack(current_enemy)
			print("El enemigo te ataca")
			print("Te ha quitado  "+str(ataquenemigo))
			player.hurt(ataquenemigo)

#Realizamos el mismo proceso que con la funcion que hemos creado para json

def juegoxml (enemigou):
	exit =  False
	global guardar
	guardar = 2
	current_enemy = enemigou

#Hacemos un bucle que no finalizará hasta que exit sea True

	while not exit:

#LLamamos a las dos funciones que es tan en las clases Enemies y Player
		enemykill = enemigosxml.muerte
		badending = player.dead()

#Hacemos las 3 distintas combinaciones que podemos tener segun la vida del enemigo o la del jugador

		if enemykill:
			current_enemy = current_enemy + 1

			print("Felicidades te has cargao al bicho")
			print("")

		if badending < 0:
			print("Has muerto, vuelve a intentarlo")
			break

		if current_enemy >= 3:
			print("Felicidades loquete, has derrotado a todos los bichos y has ganado la partida")
			print("")

			break

#Aqui empieza el proceso de que atacan al jugador y al enemigo
#Mostraremos al usuario el enemigo al que se ha de enfrentar

		print("Te ataca un enemigo: ")
		enemigosxml.show_info(current_enemy)

#Damos a elegir al usuario si quiere atacar o guardar partida

		opcion = input("Quieres atacar (1) o guardar (A)? ")


#Aqui simplemente salimos del bucle ya que realmente el formato ya lo guardamos cuando escoge si quiere guardar al principio con json o xml

		if opcion == "A":
			print("Guardando: ")
			break


#Ataca al enemigo y el jugador tambien es atacado

		if opcion == "1":
			danio = player.attack()

			print("PUM! Atacas al enemigo, le has quitado "+str(danio))
			print("")

			danioenemy = enemigosxml.hurt(danio,current_enemy)
			ataquenemigo = enemigosxml.attack(current_enemy)

			print("El enemigo te ataca")
			print("Te ha quitado  "+str(danioenemy))
			player.hurt(ataquenemigo)



#Aqui realizaremos el inicio del juego dando la bienvenido y dando a escoger al usuario las distintas opciones que tiene disponibles

if __name__ == "__main__":

#Damos la bienvenida

	print("Bienvenido al juego de la piton:")
	print("Tu objetivo es derrotar a todos lo enemigos de la dungeon")
	print("!!IMPORTANTE, SI QUIERES GUARDAR PULSA LA LETRA A!!")
	print("¿Estas listo?")
	print("")


#Realizamos este bucle infinito que saldra cuando el usuario pulse 3
	while True:


		print("Tienes 3 opciones: ")
		print("Nueva Partida: (1)")
		print("Cargar partida ya guardada: (2)")
		print("Salir: (3)")
		print("")


#Preguntamos al usuario que quiere hacer

		opcion = input("¿Que quieres hacer? ")
		print("")


		if opcion == "1":


#Preguntamos al usuario que formato guardará el formato, esto nos permitirá desplazarnos a una funcion u otra segun lo que haya escogido

			escoge = input("Cuando guardes que formato querrás escoger, ¿json (1) o xml (2)?  ")

#Si escoge json nos iremos a la funcion juegojson
			if escoge == "1":

				current_enemy = 0

				print("Empecemos ")
				player.input_info()
				player.write_info()
				juegojson(current_enemy )

#Si escoge xml nos iremos a la funcion juegoxml

			if escoge == "2":

				current_enemy = 0

				print("Empecemos ")
				player.input_info()
				player.write_info()
				juegoxml(current_enemy )

#Cargaremos la partida en caso de que antes se haya guardado

		if opcion == "2":
			print("Cargando partida: ")

#Como ha tenido que entrar previamente en una de las dos funciones anteriores, como nos detecta la variable que teniamos guardadas, volveremos
# a llamar a la funcion correspondiente en el estado en el que se habia quedado
			if guardar == 1:
				juegojson(current_enemy)

			if guardar == 2:
				juegoxml(current_enemy)


#Salimos del juego

		if opcion == "3":
			print("Gracias por jugar")
			print("---------------------")
			print("CREADO POR TONI GALAN")
			print("---------------------")
			break


