from lxml import etree

def nombres_efectos(arbol):
	audio = []
	group = []
	midi = []
	for i in arbol.xpath('//Tracks/AudioTrack/DeviceChain/Devices/PluginDevice/PluginDesc/VstPluginInfo'):
		if i not in audio:
			audio.append(i)
	return audio

arbol = etree.parse('daydream.xml')

for i in nombres_efectos(arbol):
	print(i)