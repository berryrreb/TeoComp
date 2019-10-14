#!/usr/bin/env python
# -- coding: utf-8 --

Q=['q1', 'q2', 'q3', 'q4']
#Estado inicial
s='q1'
Sigma=['a','b']
Gamma=['A','B']
z='A'
F=['q4']
delta={
    ('q1','a','A'):('q2','BA'),
    ('q1','ε','A'):('q4','ε'),
    ('q2','a','B'):('q2','BB'),
    ('q2','b','B'):('q3','ε'),
    ('q3','ε','A'):('q4','A'),
    ('q3','b','B'):('q3','ε')
}
stack=[z]

def transicion(estado, sigma):
    global Sigma, delta, Gamma, stack
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


top=stack.pop()


#Prueba
w='aaaaaab'
estado=s
for sigma in w:
    estado, STATUS=transicion(estado, sigma)
    if(not STATUS):
        break
if((STATUS) and (estado in F)):
    print w, "sí está en el lenguaje"
else:
    print w, "no está en el lenguaje"

def push (w, stack):
    for s in w:
        stack.append(s)
    return
def print_stack(stack):
    print ''.join(stack[::-1])
    return