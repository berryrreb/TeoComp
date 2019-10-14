#!/usr/bin/env python
# -*- coding: utf-8 -*-

Sigma=['a', 'b']
s='q0'
Q=['q0', 'q1']
F=['q1']

DELTA={ ('q0', 'a') : ['q0', 'q1'],
        ('q0', 'b') : ['q1'],
        ('q1', 'b') : ['q0', 'q1']
        }

from itertools import chain, combinations
def powerset(iterable):
    s=list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1)) 

Qprima=list(powerset(Q))

sprima=(s,)

Fprima=[]

print 'Qprima'
print Qprima

#En Fprima van los miembros de Qprima que contengan los estados en F

for q in Qprima:
    for x in q:
        if x in F:
            Fprima.append(q)

print 'Fprima'
print Fprima

#Construir delta

delta={}

print 'Trancisiones'
for q in Qprima:
    for s in Sigma:
        P=[]
        for x in q:
            if (x,s) in DELTA.keys():
                for r in DELTA[(x,s)]:
                    if r not in P:
                        P.append(r)
        P.sort()
        print '(',q,',',s,') -> ',tuple(P)
        delta [(q,s)]=tuple(P)
print 'delta'
print delta
        
def transicion(estado, sigma):
    global Sigma, delta
    STATUS=True
    if(sigma not in Sigma):
        STATUS=False
        return '',STATUS
    if(estado, sigma) not in delta.keys():
        STATUS=False
        return '',STATUS
    estado_siguiente=delta[(estado, sigma)]
    print 'Transición(',estado,',',sigma,')',estado_siguiente
    return estado_siguiente, STATUS
#Prueba
w='baaaa'
estado=sprima
for sigma in w:
    estado, STATUS=transicion(estado, sigma)
    if(not STATUS):
        break
if((STATUS) and (estado in Fprima)):
    print w, "sí está en el lenguaje"
else:
    print w, "no está en el lenguaje"