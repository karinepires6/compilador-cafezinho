import re

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
    '=',
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
    'carconst',
    'intconst'
]


#Verifica se o token é uma palavra reservada da linguagem
def t_palavraReservada(palavra):
    for reservada in palavras_reservadas:
        if reservada == palavra:
            return True

#Verifica se o token está no array de operadores da linguagem
def t_operador(palavra):
    for i in range(len(t_operadores)):
        if t_operadores[i] == palavra:
            return t_operadores[i]

#Verifica se o token está no array de delimitadores
def t_delimitador(palavra):
    for i in range(len(t_delimitadores)):
        if t_delimitadores[i] == palavra:
            return t_delimitadores[i]

#Verifica se o token é um terminal da gramatica
def t_terminal(palavra):
    for i in range(len(t_terminais)):
        if t_terminais[i] == palavra:
            return t_terminais[i]

#Verifica se é um identificador
def t_id(palavra):
    if re.fullmatch("[a-zA-Z]+\w*", palavra):
        return palavra
    else:
        return None

'''Verifica se a string passada possui comentario
Retorna uma lista das posições de inicio e fim dos comentarios
def t_comentario(palavra):
    p = re.compile('\/\*(\*(?!\/)|[^*])*\*\/')
    iterator = p.finditer(palavra)
    listValues = []
    for match in iterator:
        listValues.append(match.group(0))
    return listValues
'''
def removeComentarios(palavra):
    return re.sub('\/\*(\*(?!\/)|[^*])*\*\/', '', palavra)

#Verifica se o token é um integer
def t_integer(palavra):
    if re.fullmatch("[0-9]+", palavra):
        return palavra
    else:
        return None

#Verifica se o token é um float
def t_float(palavra):
    if re.fullmatch("[0-9]+.[0-9]+", palavra):
        return palavra
    else:
        return None

#Faz a analise dos tokens
def analisador(palavra):
    if t_palavraReservada(palavra):
        return print("Palavra Reservada: {}".format(palavra))
    elif t_id(palavra):
        return print("Identificador: {}".format(t_id(palavra)))
    elif t_operador(palavra):
        return print("Operador: {}".format(palavra))
    elif palavra == '':
        return
    elif t_delimitador(palavra):
        return print("Delimitador: {}".format(palavra))
    elif t_integer(palavra):
        return print("Integer: {}".format(palavra))
    elif t_float(palavra):
        return print("Float: {}".format(palavra))
    else:
        return print("Terminal: {}".format(palavra))

def main():
    #Abre arquivo com o codigo
    filepath = 'guru99.txt'
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        #Lê linha por linha no arquivo e separa os tokens
        while line:
            #print("Line {}: {}".format(cnt, line.strip()))
            #antes de fazer o split do texto, verificar se o mesmo possui comentarios
            newText = removeComentarios(line)
            splitted_text = re.split("\s", newText)
            #para cada token verifica qual a qual classe de lexema ele esta inserido
            for word in splitted_text:
                analisador(word)
            line = fp.readline()
            cnt += 1

if __name__== "__main__":
  main()


