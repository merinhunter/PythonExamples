#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

#Diseñado para discoteca.01
import sys
import xml.etree.cElementTree as ET
from argparse import ArgumentParser

def imprime_xml(root):
	for elemento in root.iter("disco"):
		print elemento.get("autor"), "/",
		print elemento.get("titulo")
		print "--------------------------------"
		i = 1
		for subelement in elemento.iter("cancion"):
			print str(i).ljust(3),
			imprime_elemento(subelement)
			i += 1
		print

def imprime_elemento(elemento):
	print elemento.get("titulo") + " ",
	print elemento.get("duracion")

def main():
	parser = ArgumentParser()
	parser.add_argument("fichero", help="Documento XML",
						metavar="XML", default=sys.stdin, nargs="?")

	argumentos = parser.parse_args()

	root = ET.ElementTree(file=argumentos.fichero).getroot()
	imprime_xml(root)

if __name__ == "__main__":
	main()
