cadena=raw_input("inserte una cadena: ")
miDiccionario = {}
for caracter in cadena:
	if miDiccionario.has_key(caracter):
		miDiccionario[caracter] += 1
	else:
		miDiccionario[caracter]= 1
print miDiccionario