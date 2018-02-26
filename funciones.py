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

arbol = etree.parse('daydream.xml')

for i in nombres_efectos(arbol):
	print(i)