#!/usr/bin/python3

import xmltodict

class Enemies:
	def_init_(self):
		xml_file = open("enemies.xml", "r")
		enemies_tmp = xmltodict.parse(xml_file.read())

		enemies_list = enemies_tmp['enemies']['enemy']

		self.enemies = []

		for e in enemies_list:
			#tmp = Enemy(e["name"], e["health"], e["damage"], "TEST")

			self.enemies.append(Enemy(e["name"], e["health"], e["damage"]))


