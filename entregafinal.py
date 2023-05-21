#!/usr/bin/python3

from enemies_class import Enemies
from player_class import Player


choosejsonxml = 0
player = Player(0)
enemigosjson = Enemies(choosejsonxml)
enemigosxml = Enemies(choosejsonxml)
current_enemy = 0


def juegojson (enemigou):
	exit =  False
	global guardar
	guardar = 1
	current_enemy = enemigou

	while not exit:


		enemykill = enemigosjson.muerte(current_enemy)
		badending = player.dead()

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

			print("Gracias por jugar")
			print("---------------------")
			print("CREADO POR TONI GALAN")
			print("---------------------")

		print("\nTe ataca un enemigo: ")
		enemigosjson.show_info(current_enemy)

		opcion = input("Quieres atacar (1) o guardar (A)? ")

		if opcion == "A":
			print("\nGuardando: ")
			print("")
			break

		if opcion == "1":
			danio = player.attack()
			print("\nPUM! Atacas al enemigo, le has quitado "+str(danio))
			print("")

			danioenemy = enemigosjson.hurt(danio,current_enemy)
			ataquenemigo = enemigosjson.attack(current_enemy)
			print("El enemigo te ataca")
			print("Te ha quitado  "+str(ataquenemigo))
			player.hurt(ataquenemigo)

def juegoxml (enemigou):
	exit =  False
	global guardar
	guardar = 2
	current_enemy = enemigou

	while not exit:


		enemykill = enemigosxml.muerte
		badending = player.dead()

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

			print("Gracias por jugar")
			print("---------------------")
			print("CREADO POR TONI GALAN")
			print("---------------------")

		print("Te ataca un enemigo: ")
		enemigosxml.show_info(current_enemy)

		opcion = input("Quieres atacar (1) o guardar (A)? ")

		if opcion == "A":
			print("Guardando: ")
			break

		if opcion == "1":
			danio = player.attack()

			print("PUM! Atacas al enemigo, le has quitado "+str(danio))
			print("")

			danioenemy = enemigosxml.hurt(danio,current_enemy)
			ataquenemigo = enemigosxml.attack(current_enemy)

			print("El enemigo te ataca")
			print("Te ha quitado  "+str(danioenemy))
			player.hurt(ataquenemigo)



if __name__ == "__main__":


	print("Bienvenido al juego de la piton:")
	print("Tu objetivo es derrotar a todos lo enemigos de la dungeon")
	print("!!IMPORTANTE, SI QUIERES GUARDAR PULSA LA LETRA A!!")
	print("¿Estas listo?")
	print("")

	while True:
		print("Tienes 3 opciones: ")
		print("Nueva Partida: (1)")
		print("Cargar partida ya guardada: (2)")
		print("Salir: (3)")
		print("")

		opcion = input("¿Que quieres hacer? ")
		print("")

		if opcion == "1":
			escoge = input("Cuando guardes que formato querrás escoger, ¿json (1) o xml (2)?  ")

			if escoge == "1":

				current_enemy = 0

				print("Empecemos ")
				player.input_info()
				player.write_info()
				juegojson(current_enemy )

			if escoge == "2":

				current_enemy = 0

				print("Empecemos ")
				player.input_info()
				player.write_info()
				juegoxml(current_enemy )


		if opcion == "2":
			print("Cargando partida: ")

			if guardar == 1:
				juegojson(current_enemy)

			if guardar == 2:
				juegoxml(current_enemy)




		if opcion == "3":
			print("Gracias por jugar")
			print("---------------------")
			print("CREADO POR TONI GALAN")
			print("---------------------")
			break


