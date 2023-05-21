#!/usr/bin/python3

import random


class Enemy:
	def __init__(self, name, health, strength, description = ""):

		self.name = name
		self.health = health
		self.strength = strength
		self.description = description


	def attack(self):
		return random.randint(0, self.strength)

	def show_info (self):
		print("NAME: "+self.name)
		print("HEALTH: "+str(self.health))
		print("STRENGTH: "+str(self.strength))
		print("DESCRIPTION: "+self.description)

	def hurt (self,damage):
		self.health = self.health - damage
		if self.health > 0:
			return False

		return True

if __name__ == "__main__":
	enemigo = Enemy("Jacinto", 33, 10, "Es un bicho feo")
	print(enemigo.hurt(enemigo.attack()))
	enemigo.show_info()



