from UserString import MutableString

def calcularLongitudDeCadena(cadena):
	return len(cadena)

def contarNumeroDeCaracter(cadena):
	miDiccionario = {}
	for caracter in cadena:
		if miDiccionario.has_key(caracter):
			miDiccionario[caracter] += 1
		else:
			miDiccionario[caracter]= 1
	return miDiccionario

def obtenerNuevaCadena(cadena):
	return cadena[:2]+cadena[-2:]

def reemplazarCaracter(cadena):
	cadenanueva = MutableString(cadena.replace(cadena[0],'$'))
	cadaux = MutableString(cadena)
	cadenanueva[0] = cadaux[0]
 	return cadenanueva

def obtenerInicioDeCadena(miCadena):
	return miCadena[:2]

def obtenerNuevaCadenaCinco(miCadenaUno, miCadenaDos):
	cadena = MutableString(miCadenaUno)
	cadena[0] = ''
	cadena[0] = ''
	cadenaaux = obtenerInicioDeCadena(miCadenaDos) + cadena
	return cadenaaux

def obtenerCadenaMasLarga(miLista):
	r = ''
	for i in miLista:
		if len(i)>len(r):
			r = i
	return r

def eliminarCaracter(indice, cadena):
	miCadena = MutableString(cadena)
	miCadena[indice]=''
	return miCadena

def invertirCaracter(cadena):
	aux = MutableString(cadena)
	aux[0] = cadena[-1]
	aux[-1] = cadena[0]
	return aux

def eliminarIndiceImpar(cadena):
	cad = MutableString(cadena)
	for i in range(len(cadena)):
		if i%2!=0:
			cad[i]=''

	return cad

def contarOcurrenciaDeOracion(cadena):
	miLista = cadena.upper().split()
	miDiccionario = {}	
	for cadena in miLista:
		if miDiccionario.has_key(cadena):
		 	miDiccionario[cadena] += 1
		else:
			miDiccionario[cadena]= 1
	return miDiccionario
	
def probadorDeAplicacion():

	miLista = ["Uno", "Dos", "Tres"]

	print (calcularLongitudDeCadena("HOLA"))  #1

	print (contarNumeroDeCaracter("AABBCCDDEEFF")) #2

	print (obtenerNuevaCadena("w3resource")) #3

	print(reemplazarCaracter("regresar")) #4

	print(obtenerNuevaCadenaCinco("abc","xyz")) #5

	print(obtenerCadenaMasLarga(miLista)) #6

	print(eliminarCaracter(0, "HOLA")) #7

	print(invertirCaracter("Python")) #8

	print(eliminarIndiceImpar("Imp")) #9
	
	print(contarOcurrenciaDeOracion("No he visto un billete de 500 euros en mi vida He tenido que recurrir a la wikipedia para consultar su color")) #10


probadorDeAplicacion()



