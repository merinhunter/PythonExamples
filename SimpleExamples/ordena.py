#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import types, sys
from argparse import ArgumentParser

typespermitted = [types.IntType, types.LongType, types.FloatType]

def main():
	parser = ArgumentParser()
	parser.add_argument("-i", "--input", action="store",
						dest="input", default="std_in",
						help="Input File")
	parser.add_argument("-o", "--output", action="store",
						dest="output", default="std_out",
						help="Output File")

	argumentos = parser.parse_args()

	if argumentos.input != "std_in":
		try:
			sys.stdin = open(argumentos.input, "r")
		except IOError:
			sys.stderr.write("No se puede leer el fichero\n")
			raise SystemExit

	if argumentos.output != "std_out":
		try:
			sys.stdout = open(argumentos.output[0], "w")
		except IOError:
			sys.stderr.write("No se puede leer el fichero\n")
			raise SystemExit

	lista = []
	linenumber = 1;
	for line in sys.stdin:
		lista.append(convert(line.split("\n")[0], linenumber))
		linenumber += 1

	for x in sort(lista):
		i = 0
		for y in x:
			print y,
			if(i != (len(x) - 1)):
				sys.stdout.softspace = 0
				print ",",
				sys.stdout.softspace = 0
			i += 1
		print

def sum(l):
	"""Dada una lista, devuelve la suma de sus componentes."""
	tot = 0
	if len(l) == 0:
			raise SystemExit
	for x in l:
		if type(x) not in typespermitted:
			raise SystemExit
		tot += x
	return tot

def convert(line, linenumber):
	"""Devuelve la línea leída en forma de lista."""
	if line == "":
		return

	miembro = line.split(",")
	member = []

	if miembro[-1] == "":
		print "Línea", linenumber, "inválida:", line
		raise SystemExit

	for x in miembro:
		x = x.split("\t")
		while "" in x:
			x.remove("")
		for y in x:
			y = y.split(" ")
			while "" in y:
				y.remove("")
			member.append("".join(y))

	i = 0
	for x in member:
		try:
			member[i] = int(x)
		except ValueError:
			print "Línea", linenumber, "inválida:", line
			raise SystemExit
		if int(x) < 0:
			print "Línea", linenumber, "inválida:", line
			raise SystemExit
		i += 1

	return member

def sort(lista):
	"""Ordena una lista según los criterios del ejercicio."""
	lista_aux = []
	lista_aux2 = []
	for x in lista:
		lista_aux.append([sum(x), len(x), lista.index(x)])
	lista_aux.sort()
	for x in lista_aux:
		lista_aux2.append(lista[x[2]])
	return lista_aux2

if __name__ == "__main__":
	main()
