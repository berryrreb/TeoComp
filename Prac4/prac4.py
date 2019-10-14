#!/usr/bin/env python
# -*- coding: utf-8 -*-

Q=['q0', 'qi', 'q2']
#Estado inicial
S='q0'
Sigma=['a','b']
F=['q1']
delta={
    ('q0','a'):'q0',
    ('q0','b'):'q1',
    ('q1','a'):'q2',
    ('q1','b'):'q2',
    ('q2','a'):'q2',
    ('q2','b'):'q2'
}
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
w='aaaaaaaaaaab'
estado=S
for sigma in w:
    estado, STATUS=transicion(estado, sigma)
    if(not STATUS):
        break
if((STATUS) and (estado in F)):
    print w, "sí está en el lenguaje"
else:
    print w, "no está en el lenguaje"

def powerset(Q):
    from itertools import chain, combinations
    return chain.from_iterable(
        combinations(Q,r) for r in range(len(Q)+1)
    )
