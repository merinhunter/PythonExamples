#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys, os, string
from argparse import ArgumentParser

unpermitted_chars = string.punctuation.replace("-","").replace(".","").replace("_","")

mod_spaces = False
mod_case = False
mod_enne = False
mod_accent = False
mod_weird = False

def main():
	"""Programa principal"""
	global mod_spaces
	global mod_case
	global mod_enne
	global mod_accent
	global mod_weird

	parser = ArgumentParser()
	parser.add_argument("-r", "--recursive", action="store_true",
						dest="recursive", default=False,
						help="Recorrer los directorios recursivamente")
	parser.add_argument("-s", "--spaces", action="store_true",
						dest="spaces", default=False,
						help="Reemplazar los espacios por barra baja")
	parser.add_argument("-c", "--case", action="store_true",
						dest="case", default=False,
						help="Reemplazar las mayúsculas por minúsculas")
	parser.add_argument("-n", "--enne", action="store_true",
						dest="enne", default=False,
						help="Reemplazar la ñ por nn")
	parser.add_argument("-t", "--accent", action="store_true",
						dest="accent", default=False,
						help="Reemplazar las vocales con acento")
	parser.add_argument("-w", "--weird", action="store_true",
						dest="weird", default=False,
						help="Reemplazar los caracteres 'raros'")
	parser.add_argument("directorios", help="Directorios",
						metavar="DIR", default=u".", nargs="*")

	argumentos = parser.parse_args()

	if not argumentos.spaces and not argumentos.case and not argumentos.enne and not argumentos.accent and not argumentos.weird:
		mod_spaces = True
		mod_case = True
		mod_enne = True
		mod_accent = True
		mod_weird = True
	else:
		mod_spaces = argumentos.spaces
		mod_case = argumentos.case
		mod_enne = argumentos.enne
		mod_accent = argumentos.accent
		mod_weird = argumentos.weird

	for directorio in argumentos.directorios:
		if not os.path.exists(directorio) or not os.path.isdir(directorio):
			sys.stderr.write("ERROR: Directory does not exist\n")
			raise SystemExit

		walkDirectory(unicode(directorio), argumentos.recursive)

def changeName(fich_name):
	"""Devuelve una cadena adecuada a un sistema de ficheros"""
	if mod_spaces:
		fich_name = fich_name.replace(u" ", u"_")
	if mod_case:
		fich_name = fich_name.lower()
	if mod_enne:
		fich_name = fich_name.replace(u"ñ", u"nn")
		fich_name = fich_name.replace(u"Ñ", u"NN")
	if mod_accent:
		fich_name = fich_name.replace(u"á", u"a")
		fich_name = fich_name.replace(u"à", u"a")
		fich_name = fich_name.replace(u"é", u"e")
		fich_name = fich_name.replace(u"è", u"e")
		fich_name = fich_name.replace(u"í", u"i")
		fich_name = fich_name.replace(u"ì", u"i")
		fich_name = fich_name.replace(u"ó", u"o")
		fich_name = fich_name.replace(u"ò", u"o")
		fich_name = fich_name.replace(u"ú", u"u")
		fich_name = fich_name.replace(u"ù", u"u")
	if mod_weird:
		for x in fich_name:
			if x in list(unpermitted_chars):
				fich_name = fich_name.replace(x, u".")
	return fich_name

def get_name(name, n):
	"""Añade un identificador numérico a un nombre"""
	aux = name.split(".")

	if len(aux) > 1:
		if n >= 100:
			aux.insert(-1, str(n))
		elif n >= 10:
			aux.insert(-1, "0" + str(n))
		else:
			aux.insert(-1, "00" + str(n))
		aux = ".".join(aux)
	else:
		aux = "".join(aux)

		if n >= 100:
			aux += str(n)
		elif n >= 10:
			aux += ".0" + str(n)
		else:
			aux += ".00" + str(n)

	return aux

def collision(name, names_changed, collision_list):
	"""Procesa la colisión de un fichero"""
	if os.path.exists(changeName(name)):
		aux = get_name(changeName(name), 1)
		os.rename(changeName(name), aux)
		names_changed.append(aux)

	i = 1
	while 1:
		if get_name(changeName(name), i) in names_changed:
			i += 1
		else:
			aux = get_name(changeName(name), i)
			os.rename(name, aux)
			names_changed.append(aux)
			break

def walkDirectory(directory, recursive):
	"""Recorre el directorio y modifica el nombre de todos
	los ficheros y carpetas del mismo"""
	list_dir = os.listdir(directory)
	names_changed = []
	collision_list = []
	cwd = os.getcwd()

	os.chdir(directory)
	for x in list_dir:
		if x == changeName(x):
			names_changed.append(x)
	for x in list_dir:
		if x in names_changed:
			continue

		if changeName(x) in names_changed:
			collision_list.append(x)
		else:
			os.rename(x, changeName(x))
			names_changed.append(changeName(x))

	for x in collision_list:
		collision(x, names_changed, collision_list)

	if recursive:
		list_dir = os.listdir(".")
		for x in list_dir:
			if os.path.isdir(x):
				walkDirectory(unicode(x), recursive)

	os.chdir(cwd)

if __name__ == "__main__":
	main()
