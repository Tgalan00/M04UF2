#!/usr/bin/python3

import xmltodict
import pprint

xml_file = open("clashroyale.xml","r")

diccionario = xmltodict.parse(xml_file.read())


pp = pprint.PrettyPrinter(indent=4)

pp.pprint(diccionario)

#print(diccionario["characters"]["character"][0]["name"])

character_num = input ("Introduce un numero del 0 al 2: ")

character = diccionario["characters"]["character"][int(character_num)]

print("Name: "+character["name"])

print("Health: "+character["health"])

print("Damage: "+character["damage"])

print("Level: "+character["level"])
