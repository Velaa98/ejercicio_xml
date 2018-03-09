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
		print('\nLos efectos empleados en el proyecto son: ', end = '')
		print(', '.join(f.nombres_efectos(arbol)))
	if opcion == '2':
		print('\n{}'.format(f.cuenta_pistas(arbol)))
	if opcion == '3':
		lista = f.pistas_por_cadena(arbol)
		if lista == 0:
			print('No se han encontrado pistas que contengan la cadena introducida.')
		elif len(lista) == 1:
			print('La pista que contiene la cadena introducida es: ', end = '')
		else:
			print('Las pistas que contienen la cadena introducida son: ', end = '')
		if type(lista) == list:
			print(', '.join(lista))
	if opcion == '4':
		lista = f.pistas_por_efecto(arbol)
		if len(lista) == 1:
			print('La pista que tiene algún efecto que contiene la cadena introducida es: ', end = '')
		elif len(lista)	== 0:
			print('No hay ninguna pista que tenga algún efecto que contenga la cadena introducida.', end = '')
		else:
			print('Las pistas que tienen efectos que contienen la cadena introducida son: ', end = '')
		print(', '.join(lista))
	if opcion == '5':
		num = f.num_pistas_efecto(arbol)
		if num == 0:
			print('No se han encontrado pistas que tengan algún efecto que contenga la cadena introducida.')
		elif num == 1:
			print('Hay una pista que tiene algún efecto que contiene la cadena introducida.')
		else:
			print('Hay {} pistas que tienen algún efecto que contiene la cadena introducida.'.format(num))
	opcion = input('\nSelecciona otra opción: ')

print('¡Adiós!')