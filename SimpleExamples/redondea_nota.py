#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

def redondea_nota(nota, modo):
	lista = ['normal', 'laxo', 'estricto']
	if modo not in lista:
		return 'Modo inválido'
	if nota < 0 or nota > 10:
		return 'Nota inválida'
	if modo == 'normal':
		if nota < 4.5:
			resultado = 'Suspenso'
		elif nota >= 9:
			resultado = 'Sobresaliente'
		else:
			resultado = 'Aprobado'
	elif modo == 'laxo':
		if nota < 4:
			resultado = 'Suspenso'
		elif nota >= 8:
			resultado = 'Sobresaliente'
		else:
			resultado = 'Aprobado'
	elif modo == 'estricto':
		if nota < 5:
			resultado = 'Suspenso'
		elif nota == 10:
			resultado = 'Sobresaliente'
		else:
			resultado = 'Aprobado'
	return resultado

print redondea_nota(8, 'laxo')
