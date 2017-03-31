#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys, datetime, pytz, calendar, json, string
import xml.etree.cElementTree as ET
from argparse import ArgumentParser

timezones = ["utc", "epoch", "madrid", "londres", "moscu", "tokio", "new_york"]

mod_json = False
mod_ascii = False
mod_xml = False

fechas = {}
root = None

def getTZ(tz):
	if tz == "madrid":
		return pytz.timezone("Europe/Madrid")
	elif tz == "londres":
		return pytz.timezone("Europe/London")
	elif tz == "moscu":
		return pytz.timezone("Europe/Moscow")
	elif tz == "tokio":
		return pytz.timezone("Asia/Tokyo")
	elif tz == "new_york":
		return pytz.timezone("America/New_York")
	elif tz == "utc" or tz == "epoch":
		return pytz.utc

def getNumlinea(line):
	miembro = line.split(" ")
	return miembro[0]

def getDateTime(date, hour, tz):
	date = date.split("-")
	hour = hour.split(":")
	year = int(date[0])
	month = int(date[1])
	day = int(date[2])
	hora = int(hour[0])
	minutes = int(hour[1])
	seconds = int(hour[2])
	tz = getTZ(tz.lower())
	dt = datetime.datetime(year, month, day, hora, minutes, seconds)
	dt = tz.localize(dt)
	return dt

def getTime(line):
	miembro = line.split(" ")

	if len(miembro) == 2:
		try:
			ts = int(miembro[1].split("\n")[0])
		except ValueError:
			sys.stderr.write("Formato incorrecto\n")
			raise SystemExit
	elif len(miembro) == 4:
		date = miembro[1]
		hour = miembro[2].split(",")[0]
		tz = miembro[3].split("\n")[0]
		dt = getDateTime(date, hour, tz)
		ts = calendar.timegm(dt.utctimetuple())
	else:
		sys.stderr.write("Formato incorrecto\n")
		raise SystemExit

	return ts

def printTime(numlinea, ts, tz):
	global fechas
	utc = pytz.utc

	if tz == "epoch":
		if mod_json:
			fechas[numlinea] = ts
		if mod_ascii:
			print numlinea, ts
		if mod_xml:
			instant = ET.SubElement(root, u"instant")
			instant.attrib = {u"date": str(ts), u"ordinal": numlinea}
	else:
		tz = getTZ(tz)
		dt = datetime.datetime.utcfromtimestamp(ts)
		dt = utc.localize(dt)
		dt = dt.astimezone(tz)
		if mod_json:
			fechas[numlinea] = str(dt)
		if mod_ascii:
			print numlinea, dt
		if mod_xml:
			instant = ET.SubElement(root, u"instant")
			instant.attrib = {u"date": str(dt), u"ordinal": numlinea}

def main():
	global mod_json
	global mod_ascii
	global mod_xml
	global root

	parser = ArgumentParser()
	parser.add_argument("-t", "--timezone", action="store",
						dest="tz", default="utc", help="Time Zone")
	parser.add_argument("-j", "--json", action="store_true",
						dest="json", help="Muestra la salida en formato JSON")
	parser.add_argument("-a", "--ascii", action="store_true",
						dest="ascii", help="Muestra la salida en texto plano")
	parser.add_argument("fichero", help="Fichero de fechas", metavar="FICH")

	argumentos = parser.parse_args()

	if argumentos.tz not in timezones:
		sys.stderr.write("Timezone no permitida\n")
		raise SystemExit

	try:
		fich = open(argumentos.fichero, "r")
	except IOError:
		sys.stderr.write("No se puede leer el fichero\n")
		raise SystemExit

	mod_json = argumentos.json
	mod_ascii = argumentos.ascii

	if not mod_json and not mod_ascii:
		mod_xml = True

	if mod_xml:
		root = ET.Element(u"instants")
		if argumentos.tz == "epoch":
			city = "timestamp"
		elif argumentos.tz == "utc":
			city = "UTC"
		else:
			city = string.capitalize(argumentos.tz)

		root.attrib = {u"city": city}

	lines = fich.readlines()
	for line in lines:
		numlinea = getNumlinea(line)
		ts = getTime(line)
		printTime(numlinea, ts, argumentos.tz)

	if mod_json:
		print json.dumps(fechas, sort_keys=True, indent=4)

	if mod_xml:
		print ET.tostring(root, encoding="utf-8", method="xml")

	try:
		fich.close()
	except IOError:
		sys.stderr.write("No se puede cerrar el fichero\n")
		raise SystemExit

if __name__ == "__main__":
	main()
