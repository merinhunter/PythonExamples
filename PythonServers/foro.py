#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import requests, sys, json
from argparse import ArgumentParser

url = "http://jsonplaceholder.typicode.com"

def validName(name):
	return unicode(name.capitalize())

def getUsersID():
	r = requests.get(url + "/users")
	users = {}

	if r.status_code != 200:
		sys.stderr.write("Error " + str(r.status_code) + "\n")
		raise SystemExit

	for user in r.json():
		users[user[u"username"]] = user[u"id"]

	return users

def printMessages(users, username):
	r = requests.get(url + "/posts?userId=" + str(users[username]))

	if r.status_code != 200:
		sys.stderr.write("Error " + str(r.status_code) + "\n")
		raise SystemExit

	for message in r.json():
		printMessage(username, message[u"title"], message[u"body"])

def printMessage(username, tittle, body):
	print "De: " + username
	print tittle
	print "-----------------------"
	print body
	print

def main():
	parser = ArgumentParser()
	parser.add_argument("-u", "--user", action="store",
						dest="user", default=u"all", help="Username")

	argumentos = parser.parse_args()

	users = getUsersID()
	user = validName(argumentos.user)

	if user != u"All":
		if user not in users:
			sys.stderr.write("El usuario no existe.\n")
			raise SystemExit

		printMessages(users, user)
	else:
		for user in users:
			printMessages(users, user)

if __name__ == "__main__":
	main()
