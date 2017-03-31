#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import flask, requests, json, sys
from time import time

app = flask.Flask(__name__)

url_btcchina = "https://data.btcchina.com/data/ticker?market=btccny"
url_cny = "http://api.fixer.io/latest?base=CNY"

btc_date = 0.0
cny_date = 0.0
btc_delay = 300.0
cny_delay = 86400.0

btc_request = None
cny_request = None

def xbtcny():
	global btc_date
	global btc_request

	if((btc_date + btc_delay) < time()):
		btc_date = time()
		btc_request = requests.get(url_btcchina)

	if btc_request.status_code != 200:
		sys.stderr.write("Error " + str(btc_request.status_code) + "\n")
		return 0.0

	return float(btc_request.json()["ticker"]["buy"])

def cnyconv(currency):
	global cny_date
	global cny_request

	if((cny_date + cny_delay) < time()):
		cny_date = time()
		cny_request = requests.get(url_cny)

	if cny_request.status_code != 200:
		sys.stderr.write("Error " + str(cny_request.status_code) + "\n")
		return 0.0

	return float(cny_request.json()["rates"][currency])

@app.route("/exchange/XBTEUR")
def xbteur():
	query_string = flask.request.args
	xbteur = cnyconv("EUR") * xbtcny()
	respuesta = {u"XBTEUR": xbteur}

	try:
		if "amount" in query_string:
			amount = float(query_string["amount"])
			respuesta[u"XBT"] = amount
			respuesta[u"EUR"] = xbteur * amount
	except:
		return json.dumps(0.0), 404

	return json.dumps(respuesta)

@app.route("/exchange/XBTUSD")
def xbtusd():
	query_string = flask.request.args
	xbtusd = cnyconv("USD") * xbtcny()
	respuesta = {u"XBTUSD": xbtusd}

	try:
		if "amount" in query_string:
			amount = float(query_string["amount"])
			respuesta[u"XBT"] = amount
			respuesta[u"USD"] = xbtusd * amount
	except:
		return json.dumps(0.0), 404

	return json.dumps(respuesta)

@app.route("/exchange/XBTGBP")
def xbtgbp():
	query_string = flask.request.args
	xbtgbp = cnyconv("GBP") * xbtcny()
	respuesta = {u"XBTGBP": xbtgbp}

	try:
		if "amount" in query_string:
			amount = float(query_string["amount"])
			respuesta[u"XBT"] = amount
			respuesta[u"GBP"] = xbtgbp * amount
	except:
		return json.dumps(0.0), 404

	return json.dumps(respuesta)

@app.route("/exchange/XBTCAD")
def xbtcad():
	query_string = flask.request.args
	xbtcad = cnyconv("CAD") * xbtcny()
	respuesta = {u"XBTCAD": xbtcad}

	try:
		if "amount" in query_string:
			amount = float(query_string["amount"])
			respuesta[u"XBT"] = amount
			respuesta[u"CAD"] = xbtcad * amount
	except:
		return json.dumps(0.0), 404

	return json.dumps(respuesta)

@app.route("/exchange/XBTJPY")
def xbtjpy():
	query_string = flask.request.args
	xbtjpy = cnyconv("JPY") * xbtcny()
	respuesta = {u"XBTJPY": xbtjpy}

	try:
		if "amount" in query_string:
			amount = float(query_string["amount"])
			respuesta[u"XBT"] = amount
			respuesta[u"JPY"] = xbtjpy * amount
	except:
		return json.dumps(0.0), 404

	return json.dumps(respuesta)

@app.route("/exchange/XBTAUD")
def xbtaud():
	query_string = flask.request.args
	xbtaud = cnyconv("AUD") * xbtcny()
	respuesta = {u"XBTAUD": xbtaud}

	try:
		if "amount" in query_string:
			amount = float(query_string["amount"])
			respuesta[u"XBT"] = amount
			respuesta[u"AUD"] = xbtaud * amount
	except:
		return json.dumps(0.0), 404

	return json.dumps(respuesta)

@app.route("/exchange/XBTCHF")
def xbtchf():
	query_string = flask.request.args
	xbtchf = cnyconv("CHF") * xbtcny()
	respuesta = {u"XBTCHF": xbtchf}

	try:
		if "amount" in query_string:
			amount = float(query_string["amount"])
			respuesta[u"XBT"] = amount
			respuesta[u"CHF"] = xbtchf * amount
	except:
		return json.dumps(0.0), 404

	return json.dumps(respuesta)

@app.route("/exchange/XBTRUB")
def xbtrub():
	query_string = flask.request.args
	xbtrub = cnyconv("RUB") * xbtcny()
	respuesta = {u"XBTRUB": xbtrub}

	try:
		if "amount" in query_string:
			amount = float(query_string["amount"])
			respuesta[u"XBT"] = amount
			respuesta[u"RUB"] = xbtrub * amount
	except:
		return json.dumps(0.0), 404

	return json.dumps(respuesta)

if __name__ == "__main__":
	app.run(debug = True)
