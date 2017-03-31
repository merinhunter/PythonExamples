#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import xml.etree.cElementTree as ET
from argparse import ArgumentParser

def imprime_xml(root):
	print "Matrícula  Marca    Modelo"
	print "--------------------------"
	for elemento in root.iter("coche"):
		imprime_elemento(elemento.attrib)

def imprime_elemento(elemento):
	print elemento.get("matricula").ljust(10),
	print elemento.get("marca").ljust(8),
	print elemento.get("modelo")

def main():
	parser = ArgumentParser()
	parser.add_argument("fichero", help="Documento XML",
						metavar="XML", default=sys.stdin, nargs="?")

	argumentos = parser.parse_args()

	root = ET.ElementTree(file=argumentos.fichero).getroot()
	imprime_xml(root)

if __name__ == "__main__":
	main()
