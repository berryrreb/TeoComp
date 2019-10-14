#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re  
patron = re.compile(r'\bfoo\b')  # busca la palabra foo
texto = """ bar foo bar
foo barbarfoo
foofoo foo bar
"""
print(patron.match(texto))
m = patron.match('foo bar')
m
s = patron.search(texto)
s
fa = patron.findall(texto)
fa
fi = patron.finditer(texto)
fi
next(fi)
next(fi)
m.group(), m.start(), m.end(), m.span()
s.group(), s.start(), s.end(), s.span()
mail = re.compile(r"""
\b             # comienzo de delimitador de palabra
[\w.%+-]       # usuario: Cualquier caracter alfanumerico mas los signos (.%+-)
+@             # seguido de @
[\w.-]         # dominio: Cualquier caracter alfanumerico mas los signos (.-)
+\.            # seguido de .
[a-zA-Z]{2,6}  # dominio de alto nivel: 2 a 6 letras en minúsculas o mayúsculas.
\b             # fin de delimitador de palabra
""", re.X)
mails = """raul.lopez@relopezbriega.com, Raul Lopez Briega,
foo bar, relopezbriega@relopezbriega.com.ar, raul@github.io, 
https://relopezbriega.com.ar, https://relopezbriega.github.io, 
python@python, river@riverplate.com.ar, pythonAR@python.pythonAR
"""
mail.findall(mails)

url = re.compile(r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$")

# vemos que https://relopezbriega.com.ar lo acepta como una url válida.
url.search("https://relopezbriega.com.ar")
print(url.search("https://google.com/un/archivo!.html"))

patron = ('^(?:(?:25[0-5]|2[0-4][0-9]|'
          '[01]?[0-9][0-9]?)\.){3}'
          '(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

ip = re.compile(patron)

# la ip 73.60.124.136 es valida
ip.search("73.60.124.136")
print(ip.search("256.60.124.136"))

fecha = re.compile(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\d\d)$')

# validando 13/02/1982
fecha.search("13/02/1982")
print(fecha.search("13-02-1982"))
print(fecha.search("32/12/2015"))
print(fecha.search("30/14/2015"))


#RFC
RFC=re.compile(r'/^([A-ZÑ&]{3,4}) ?(?:- ?)?(\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])) ?(?:- ?)?([A-Z\d]{2})([A\d])$/')
print(RFC.search('MEPM9404182C2'))

#CURP
curp=re.compile(r'/^([A-ZÑ&]{3,4}) ?(?:- ?)?(\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])) ?(?:- ?)?([A-Z\d]{2})([A\d])$/')
print(curp.search('MEPM940418HDFLDR08'))