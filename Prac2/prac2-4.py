from UserString import MutableString

cadena=raw_input("inserte una cadena: ")
cadenanueva = MutableString(cadena.replace(cadena[0],'$'))
cadaux = MutableString(cadena)
cadenanueva[0] = cadaux[0]
print cadenanueva