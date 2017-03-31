#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

#1
caja01 = []
caja02 = []

#2
caja01.append("Lorena")
caja02.append("Marta")
caja01.append("Sergio")
caja01.append("Miguel")
caja02.append("Pedro")
caja02.append("Olga")
print "En la caja01 se encuentran", caja01
print "En la caja02 se encuentran", caja02
print

#3
caja02.remove("Pedro")
print "En la caja01 se encuentran", caja01
print "En la caja02 se encuentran", caja02
print

#4
caja01.insert(0, "Ernesto")
print "En la caja01 se encuentran", caja01
print "En la caja02 se encuentran", caja02
print

#5
caja03 = []
caja03.append(caja02[1])
caja02.remove(caja02[1])
print "En la caja01 se encuentran", caja01
print "En la caja02 se encuentran", caja02
print "En la caja03 se encuentran", caja03
print

#6
caja01.reverse()
print "En la caja01 se encuentran", caja01
print "En la caja02 se encuentran", caja02
print "En la caja03 se encuentran", caja03
print

#7
if "Ernesto" in caja01:
	pos = caja01.index("Ernesto") + 1
	caja01.remove("Ernesto")
	caja01.insert(0, "Ernesto")
	print "Ernesto pasa de la posición", pos, "a la 1"

print "En la caja01 se encuentran", caja01
print "En la caja02 se encuentran", caja02
print "En la caja03 se encuentran", caja03
print

#8
linea_de_cajas = [caja01, caja02, caja03]

#9
for x in linea_de_cajas:
	print "Caja con", len(x), "cliente/s:",
	for client in x:
		print client,
		if x.index(client) != len(x) - 1:
			print ",",
	print
print

#10
linea_de_cajas = ["; ".join(caja01), "; ".join(caja02), "; ".join(caja03)]
print "Linea de cajas:", linea_de_cajas
