#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys, json
from argparse import ArgumentParser

INFLACION = 3

def imprime_json(libreria):
	print "Ref.     Precio   Descripción"
	print "---------------------------------------"
	for elemento in libreria:
		imprime_elemento(elemento)

def imprime_elemento(elemento):
	print str(elemento[u"ref"]).ljust(8),
	print str(elemento[u"precio"] * (1 + (INFLACION * 0.01))).ljust(8),
	print elemento[u"descripcion"]

def main():
	parser = ArgumentParser()
	parser.add_argument("fichero", help="Documento JSON", metavar="JSON")

	argumentos = parser.parse_args()

	try:
		fich = open(argumentos.fichero, "r")
	except IOError:
		sys.stderr.write("No se puede leer el fichero\n")
		raise SystemExit

	libreria = json.loads(fich.read());

	imprime_json(libreria)

	try:
		fich.close()
	except IOError:
		sys.stderr.write("No se puede cerrar el fichero\n")
		raise SystemExit

if __name__ == "__main__":
	main()
