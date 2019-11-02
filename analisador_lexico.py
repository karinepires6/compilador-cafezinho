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

# ignorar tabulação
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_palavraReservada(palavra):
    for reservada in palavras_reservadas:
        if reservada == palavra:
            return True

def t_id(palavra):
    if re.fullmatch("[a-zA-Z]+\w*", palavra):
        return palavra
    else:
        return None

def palavraReservadaOuIdentificador(palavra):
    if t_palavraReservada(palavra):
        return print("Palavra Reservada: {}".format(palavra))
    else:
        return print("Identificador: {}".format(t_id(palavra)))

text = "programa1"
palavraReservadaOuIdentificador(text)


