#!/usr/bin/env python
# -- coding: utf-8 --

tokens = ('a' , 'b')
t_a = r'a'
t_b = r'b'

def t_error(t):
    print("Caracter ilegal '%s'"% t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()

def p_S(p):
    ''' S : A 
          | T '''
    pass

def p_A(p):
    ''' A : b empty
          | a A '''
    pass

def p_T(p):
    ''' T : a empty
          | b T '''
    pass

def p_empty(p):
    ''' empty : '''
    pass

w=''

def p_error(p):
    global w
    if p:
        print("Error de sintaxis en '%s'"% p.value)
        print w, 'no está en el lenguaje'
    else:
        print('Error de sintaxis en EOF')
        print w, 'no está en el lenguaje'

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        w = raw_input('> ')
    except EOFError:
        break
    t = yacc.parse(w)