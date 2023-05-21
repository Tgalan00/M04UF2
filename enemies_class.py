#!/usr/bin/python3

import json
import xmltodict
import random
from enemy_class import Enemy

class Enemies:



	def __init__(self,choosejsonxml):
		self.enemies = []
		if choosejsonxml % 2 != 0:
			xml_file = open("enemies.xml","r")
			enemies_tmp = xmltodict.parse(xml_file.read())
			self.enemies_list = enemies_tmp["enemies"]["enemy"]

			for e in self.enemies_list:
				self.enemies.append(Enemy(e["name"], e["strength"], e["health"], e["description"]))

		if choosejsonxml % 2 == 0:
			with open("enemies.json") as f:
				data = json.load(f)
				self.enemies_list = data["enemies"]["enemy"]


			for e in self.enemies_list:
				self.enemies.append(Enemy(e["name"], e["strength"], e["health"], e["description"]))


	def show_info(self,current_enemy):
		self.enemies[current_enemy].show_info()

	def attack(self,enemy_counter):
		enemy = self.enemies[enemy_counter]
		strength = int(enemy.strength)
		return random.randint(0, strength)

	def finpartida (self, enemy_counter):
		length = len(self.enemies)

		if self.enemies[enemy_counter] >= str(length):
			return True

	def muerte(self, enemy_counter):
		vida = int(self.enemies[enemy_counter].health)
		if vida < 0:
			return True

	def hurt(self, damagep, enemy_counter):
		vida_actual = self.enemies[enemy_counter].health = int(self.enemies[enemy_counter].health) - int(damagep)
		
		return vida_actual

	def guarda_info (self, enemy_counter):
		vida = self.enemies[enemy_counter].health

		nombre = self.enemies[enemy_counter].name

		descripcion = self.enemies[enemy_counter].description



if __name__ == "__main__":

	enemies = Enemies();


