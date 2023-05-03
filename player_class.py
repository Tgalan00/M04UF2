#!/usr/bin/python3

import xmltodict
import random

class Player:

	def __init__(self, name="", health=100, strength=10, level=1, xp=0):
		self.name = name
		self.health = health
		self.strength = strength
		self.level = level
		self.xp = xp
		
		xml_file = open("levels.xml","r")
		levels = xmltodict.parse(xml_file.read())
		
		xml_file.close()
		
		tmp = levels["levels"]["level"]

		print(tmp)

		self.levels = {}

		for level in tmp:
			self.levels[ level["@num"] ] = int(level["@xp"])
		
		print(self.levels)

	def set_health (self, health):
		self.health = health


	def set_strength (self, strenght):
		self.strength = strength


	def set_level (self, level):
		self.level = level

	def set_xp (self, xp):
		self.xp = xp

	def hurt (self):
		self.health -= damage

		if self.health > 0:
			return False

		return True


		if self.health > 0:
			return False

		return level_cur
	
	def attack (self):
		return random.randint(0, self.strenght)

	def get_level (self, xp = -1)

		if xp == -1:
			return self.level

		level_cur = self.level

		for level in self.levels:
			if self.levels[level] < xp:
				level_cur = level
		
		return level_cur

	def show_info(self):
		print("Name: "+self.name)
		print("Health: "+str(self.health))
		print("Strength: "+str(self.strength))
		print("Level: "+str(self.level))
		print("XP: "+str(self.xp))

  
	def write_info(self):
		diccionario = {
			"name": self.name,
			"health": self.health,
			"strength": self.strength,
			"level": self.level,
			"xp": self.xp
		}

	def read_info(self):
		xml_file = open("player.xml","r")

		player_dict = xmltodict.parse(xml_file.read())

		info = player_dict["player"]
		
		self.name = info["name"]
		self.health= int(info["health" +)
		self.strength = int(info["strength"])
		self.level = int(info["level"])
		self.xp = int(info["xp"])


    


if __name__ == "__main__":
	player = Player("Juan Ramón")

	print(player.get_level(100))
