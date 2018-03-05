from lxml import etree
import os
import funciones

os.system('clear')

arbol = etree.parse('daydream.xml')

menu = '¡Bienvenido! Estas son las opciones:\n1.- Muestra los efectos empleados.\
		\n2.- ¿Cuántas pistas de Audio y MIDI hay en total?\
		\n3.- Muestra las pistas que contienen una cadena.\
		\n4.- Muestra las pistas que tienen algún efecto que contenga una cadena.\
		\n5.- Contar cuántas pistas (Audio o MIDI) tienen un efecto que contenga una cadena.\
		\n0.- Salir'

print(menu)
opcion = input('Selecciona una opción: ')

while opcion != '0':
	if opcion == '1':
		print('\nLos efectos empleados en el proyecto son: ')
		for i in funciones.nombres_efectos(arbol):
			print(i)

	opcion = input('\nSelecciona otra opción: ')

print('¡Adiós!')