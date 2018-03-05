from lxml import etree
import os
import funciones as f

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
		for i in f.nombres_efectos(arbol):
			print(i)
	if opcion == '2':
		print('\n{}'.format(f.cuenta_pistas(arbol)))
	if opcion == '3':
		if f.pistas_por_cadena(arbol) == 0:
			print('No se ha encontrado ninguna pista que contenga la cadena introducida.')
		for i in f.pistas_por_cadena(arbol):
			print(i)
	opcion = input('\nSelecciona otra opción: ')

print('¡Adiós!')