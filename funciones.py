from lxml import etree

def nombres_efectos(arbol):
	audio = []
	group = []
	midi = []
	lista = []
	for i in arbol.xpath('//Tracks//AudioTrack//DeviceChain//Devices//PluginDevice//PluginDesc//VstPluginInfo//PlugName//@Value'):
		if i not in audio:
			audio.append(i.rstrip('_x64'))
	for i in arbol.xpath('//Tracks//GroupTrack//DeviceChain//Devices//PluginDevice//PluginDesc//VstPluginInfo//PlugName//@Value'):
		if i not in group:
			group.append(i.rstrip('_x64'))
	for i in arbol.xpath('//Tracks//MidiTrack//DeviceChain//Devices//PluginDevice//PluginDesc//VstPluginInfo//PlugName//@Value'):
		if i not in midi:
			midi.append(i.rstrip('_x64'))
	lista = list(set(audio + group + midi))
	return lista

def cuenta_pistas(arbol):
	audio = []
	midi = []
	for i in arbol.xpath('//Tracks/AudioTrack/Name/EffectiveName/@Value'):
		audio.append(i)
	for i in arbol.xpath('//Tracks/MidiTrack/Name/EffectiveName/@Value'):
		midi.append(i)
	return ('Hay {} pistas de audio y {} de MIDI.'.format(len(audio), len(midi)))

def pistas_por_cadena(arbol):
	audio = []
	midi = []
	lista = []
	l_final = []
	cadena = input('\nIntroduce una cadena: ')
	encontrado = False
	for i in arbol.xpath('//Tracks/AudioTrack/Name/EffectiveName/@Value'):
		audio.append(i)
	for i in arbol.xpath('//Tracks/MidiTrack/Name/EffectiveName/@Value'):
		midi.append(i)
	lista = audio + midi
	for i in lista:
		if i.find(cadena) >= 0:
			encontrado = True
			l_final.append(i)
	if encontrado:
		return l_final
	else:
		return 0

def pistas_por_efecto(arbol):
	audio = []
	midi = []
	group = []
	lista = []
	cadena = input('\nIntroduce una cadena: ')
	dic = {}
	for i in arbol.xpath('//Tracks/AudioTrack/Name/EffectiveName/@Value'):
		audio.append(i)
	for i in audio:
		dic['{}'.format(i)] = arbol.xpath('//*[@Value = "{}"]/../..//DeviceChain//Devices//PluginDevice//PluginDesc//VstPluginInfo//PlugName//@Value'.format(i))
	for i in arbol.xpath('//Tracks/MidiTrack/Name/EffectiveName/@Value'):
		midi.append(i)
	for i in midi:
		dic['{}'.format(i)] = arbol.xpath('//*[@Value = "{}"]/../..//DeviceChain//Devices//PluginDevice//PluginDesc//VstPluginInfo//PlugName//@Value'.format(i))
	for i in arbol.xpath('//Tracks/GroupTrack/Name/EffectiveName/@Value'):
		group.append(i)
	for i in group:
		dic['{}'.format(i)] = arbol.xpath('//*[@Value = "{}"]/../..//DeviceChain//Devices//PluginDevice//PluginDesc//VstPluginInfo//PlugName//@Value'.format(i))
	for c, v in dic.items():
		for i in v:
			if i.find(cadena) >= 0:
				lista.append(c)
	return lista

def num_pistas_efecto(arbol, cadena):
	cad = input('¿Quieres buscar en las pistas de audio o en las de MIDI? ')
	if cad.title() == 'Audio':
		dic = {}
		lista = []
		audio = []
		for i in arbol.xpath('//Tracks/AudioTrack/Name/EffectiveName/@Value'):
			audio.append(i)
		for i in audio:
			dic['{}'.format(i)] = arbol.xpath('//*[@Value = "{}"]/../..//DeviceChain//Devices//PluginDevice//PluginDesc//VstPluginInfo//PlugName//@Value'.format(i))
		for c, v in dic.items():
			for i in v:
				if i.find(cadena) >= 0:
					lista.append(c)
		return lista
	if cad.title() == 'Midi':
		dic = {}
		lista = []
		midi = []
		for i in arbol.xpath('//Tracks/MidiTrack/Name/EffectiveName/@Value'):
			midi.append(i)
		for i in midi:
			dic['{}'.format(i)] = arbol.xpath('//*[@Value = "{}"]/../..//DeviceChain//Devices//PluginDevice//PluginDesc//VstPluginInfo//PlugName//@Value'.format(i))
	
		for c, v in dic.items():
			for i in v:
				if i.find(cadena) >= 0:
					lista.append(c)
		return lista