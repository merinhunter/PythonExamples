#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys, json
import xml.etree.cElementTree as ET
from argparse import ArgumentParser

def py2xml(root, libreria):
	for elemento in libreria:
		libro = ET.SubElement(root, u"libro")
		ref = str(elemento[u"ref"])
		precio = str(elemento[u"precio"])
		desc = elemento[u"descripcion"]
		atributos = {u"ref": ref, u"precio": precio, u"descripcion": desc}
		libro.attrib = atributos

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

	root = ET.Element(u"libreria")

	py2xml(root, libreria)

	print ET.tostring(root, encoding="utf-8", method="xml")

	try:
		fich.close()
	except IOError:
		sys.stderr.write("No se puede cerrar el fichero\n")
		raise SystemExit

if __name__ == "__main__":
	main()
