#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

#1
diccionario = {'Madrid': ['cocido', 'callos', 'churros'], 'Valencia': ['salmonetes', 'horchata']}
print diccionario
print

#2
diccionario['Galicia'] = ['empanada', 'sidra', 'pote']
print diccionario
print

#3
diccionario['Madrid'].append('caracoles')
print diccionario
print

#4
alcoholicas = ['vino', 'sidra', 'cerveza']
for x in diccionario.keys():
	for y in diccionario[x]:
		if y in alcoholicas:
			diccionario[x].remove(y)
print diccionario
print

#5
comunidad_valenciana = ['Valencia', 'Alicante', 'Castellon']
for x in diccionario.keys():
	if x in comunidad_valenciana:
		diccionario[x].append('paella')
print diccionario
print

#6
for x in diccionario.keys():
	if x in comunidad_valenciana:
		del diccionario[x]
print diccionario
print

#7
def muestra_alfabetico(dic):
	claves = dic.keys()
	claves.sort()
	for x in claves:
		print x, ":",
		for y in dic[x]:
			print y,
			if dic[x].index(y) != len(dic[x]) - 1:
				print ",",
		print
muestra_alfabetico(diccionario)
print

#8
def muestra_por_longitud(dic):
	aux = dic.copy()
	for x in range(len(dic)):
		claves = aux.keys()
		clave = claves[0]
		len1 = len(aux[clave])
		for y in claves:
			len2 = len(aux[y])
			if len1 < len2:
				clave = y
		print clave, ":",
		for z in dic[clave]:
			print z,
			if dic[clave].index(z) != len(dic[clave]) - 1:
				print ",",
		print
		del aux[clave]
muestra_por_longitud(diccionario)
