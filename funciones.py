from lxml import etree

def nombres_efectos(arbol):
	audio = []
	group = []
	midi = []
	lista = []
	for i in arbol.xpath('//Tracks//AudioTrack//DeviceChain//Devices//PluginDevice//PluginDesc//VstPluginInfo//PlugName//@Value'):
		if i not in audio:
			audio.append(i)
	for i in arbol.xpath('//Tracks//GroupTrack//DeviceChain//Devices//PluginDevice//PluginDesc//VstPluginInfo//PlugName//@Value'):
		if i not in group:
			group.append(i)
	for i in arbol.xpath('//Tracks//MidiTrack//DeviceChain//Devices//PluginDevice//PluginDesc//VstPluginInfo//PlugName//@Value'):
		if i not in midi:
			midi.append(i)
	lista = audio + group + midi
	for i in lista:
		if lista.count(i) > 1:
			lista.remove(i)
	return lista

def cuenta_pistas(arbol):
	audio = []
	midi = []
	lista =[]
	for i in arbol.xpath('//Tracks/AudioTrack/Name/EffectiveName/@Value'):
		audio.append(i)
	for i in arbol.xpath('//Tracks/MidiTrack/Name/EffectiveName/@Value'):
		midi.append(i)
	lista = audio + midi
	return ('Hay {} pistas en total.'.format(len(lista)))

def pistas_por_cadena(arbol):
	audio = []
	midi = []
	lista = []
	l_final = []
	cadena = input('Introduce una cadena: ')
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
		return 'No se ha encontrado ninguna pista que contenga la cadena introducida.'

arbol = etree.parse('daydream.xml')

print(pistas_por_cadena(arbol))