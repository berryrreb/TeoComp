# -*- coding: utf-8 -*-

cadena=raw_input("inserte una cadena: ")
if len(cadena)>=4:
    print cadena[:2]+cadena[-2:]
else:    
    print "ϵ"