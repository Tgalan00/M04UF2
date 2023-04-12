
import math
import random

random = math.floor(random.random()*100)+1
print (random)

numero = -1

while numero != random:
	numero = input("Adivina el numero: ")
	numero = int(numero)
	if  numero > random:
		print("El numero es mas pequeño")
	elif  numero < random: 
		print ("El numero es mas grande")
	elif numero == random: 
		print ("Felisidades")
	
