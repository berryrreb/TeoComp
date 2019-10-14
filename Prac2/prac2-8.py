from UserString import MutableString

cadena=raw_input("inserte una cadena: ")
cadena = MutableString(cadena)
for i in range(len(cadena)):
	if i%2 == 0:
		cadena[i]=' '
print cadena