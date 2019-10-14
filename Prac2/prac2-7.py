from UserString import MutableString

cadena=raw_input("inserte una cadena: ")
indice=input("introduzca el indice: ")
cadena = MutableString(cadena)
cadena[indice]=''
print cadena