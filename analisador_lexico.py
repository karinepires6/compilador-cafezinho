import re
#Tokens
palavras_reservadas = [
    'programa', 
    'car', 
    'int', 
    'retorne', 
    'leia', 
    'escreva', 
    'novalinha', 
    'se', 
    'entao', 
    'senao', 
    'enquanto',
    'execute'
]

t_operadores = [
    '+',
    '-',
    '*',
    '/',
    '%',
    '==',
    '!=',
    '>=',
    '<=',
    '<',
    '>',
    '!',
    '?',
    ':',
    'e',
    'ou'
]

t_delimitadores = [
    '(',
    ')',
    '[',
    ']',
    '{',
    '}',
    ';',
    ','
]

t_terminais = [
    'id',
    'carconst',
    'intconst'
]



def t_palavraReservada(palavra):
    for reservada in palavras_reservadas:
        if reservada == palavra:
            return True

def t_operador(palavra):
    for i, operador in t_operadores:
        if operador == palavra:
            return t_operadores[i]

def t_delimitador(palavra):
    for i, deli in t_delimitadores:
        if deli == palavra:
            return t_delimitadores[i]

def t_terminal(palavra):
    for i, ter in t_terminais:
        if ter == palavra:
            return t_terminais[i]

def t_id(palavra):
    if re.fullmatch("[a-zA-Z]+\w*", palavra):
        return palavra
    else:
        return None

def verificaComentario(palavra):
    if re.fullmatch("//*/w+*/"):
        return True
    else:
        return False

def palavraReservadaOuIdentificador(palavra):
    if t_palavraReservada(palavra):
        return print("Palavra Reservada: {}".format(palavra))
    else:
        return print("Identificador: {}".format(t_id(palavra)))

text = "programa1"
palavraReservadaOuIdentificador(text)


