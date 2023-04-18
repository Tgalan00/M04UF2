#!/usr/bin/python3

import xmltodict
import pprint
import random

xml_file = open("clashroyale.xml","r")

enemy_file = open("enemy.xml","r")



diccionario = xmltodict.parse(xml_file.read())

diccionario2 = xmltodict.parse(enemy_file.read())

health = 100

final = false

while !final:

    ataque = random.randint(0,5)
    
    ataqueenemigo = random.randint(0,2)

    print ("ENEMIGO INCOMING:")

    print ("Name: "+diccionario2["enemy"]["name"])

    print ("HP: "+diccionario2["enemy"]["health"])

    print ("Strength: "+diccionario2["enemy"]["strength"])

    print ("Description: "+diccionario2["enemy"]["description"])

    print ("Nuestra vida: "+health")

    opcion = input ("Que quieres hacer? Atacar (1) o no hacer nada (2): ")

    if  opcion = 1:
            print ("Atacas al enemigo: Vida que le has quitado: "+ataque) 
            diccionario2["enemy"]["health"] = diccionario2["enemy"]["health"] - ataque

    print ("El enemigo te ataca: ")

    health = health - ataqueenemigo
    
    if diccionario2["enemy"]["health"] = 0 || health = 0:
        final = true

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(diccionario)

#print(diccionario["characters"]["character"][0]["name"])

character_num = input ("Introduce un numero del 0 al 2: ")

character = diccionario["characters"]["character"][int(character_num)]

print("Name: "+character["name"])

print("Health: "+character["health"])

print("Damage: "+character["damage"])

print("Level: "+character["level"])
