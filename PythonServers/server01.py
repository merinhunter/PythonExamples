#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import flask, json

app = flask.Flask(__name__)

posts = [
			{
				u"userId": 1,
				u"id": 1,
				u"title": u"Título 1",
				u"body": u"Mensaje 1"
			},
			{
				u"userId": 1,
				u"id": 2,
				u"title": u"Título 2",
				u"body": u"Mensaje 2"
			},
			{
				u"userId": 1,
				u"id": 3,
				u"title": u"Título 3",
				u"body": u"Mensaje 3"
			},
			{
				u"userId": 1,
				u"id": 4,
				u"title": u"Título 4",
				u"body": u"Mensaje 4"
			},
			{
				u"userId": 1,
				u"id": 5,
				u"title": u"Título 5",
				u"body": u"Mensaje 5"
			},
			{
				u"userId": 2,
				u"id": 6,
				u"title": u"Título 6",
				u"body": u"Mensaje 6"
			},
			{
				u"userId": 2,
				u"id": 7,
				u"title": u"Título 7",
				u"body": u"Mensaje 7"
			},
			{
				u"userId": 2,
				u"id": 8,
				u"title": u"Título 8",
				u"body": u"Mensaje 8"
			},
			{
				u"userId": 2,
				u"id": 9,
				u"title": u"Título 9",
				u"body": u"Mensaje 9"
			},
			{
				u"userId": 2,
				u"id": 10,
				u"title": u"Título 10",
				u"body": u"Mensaje 10"
			},
			{
				u"userId": 3,
				u"id": 11,
				u"title": u"Título 11",
				u"body": u"Mensaje 11"
			},
			{
				u"userId": 3,
				u"id": 12,
				u"title": u"Título 12",
				u"body": u"Mensaje 12"
			},
			{
				u"userId": 3,
				u"id": 13,
				u"title": u"Título 13",
				u"body": u"Mensaje 13"
			},
			{
				u"userId": 3,
				u"id": 14,
				u"title": u"Título 14",
				u"body": u"Mensaje 14"
			},
			{
				u"userId": 3,
				u"id": 15,
				u"title": u"Título 15",
				u"body": u"Mensaje 15"
			}
		]

@app.route("/")
def index():
	return u"Bienvenido a mi servidor REST"

@app.route("/posts")
def getPosts():
	return json.dumps(posts)

@app.route("/posts/<id>")
def getPostsId(id):
	try:
		if (int(id) > len(posts)) or (int(id) < 1):
			return json.dumps({}), 404
		else:
			return json.dumps(posts[int(id) - 1])
	except:
		return json.dumps({}), 404

if __name__ == "__main__":
	app.run(debug = True)
