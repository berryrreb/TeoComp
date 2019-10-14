miLista = ["Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis"]
r = ''
for i in miLista:
	if len(i)>len(r):
		r = i
print r + ' =', len(r)