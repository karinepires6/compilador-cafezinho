import re

'''
Analisador Léxico - Disciplina de Compiladores 2019/2
Alunos: Karine Pires de Araújo
        Guilherme Sampaio
'''

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
        listValues.append(match.span())
    return listValues
'''

def verificaComentario(filePath):
    with open(filePath) as fp:
        line = fp.readline()
        cnt = 1
        abriuNaLinha = 1
        countCmt = 0
        #Lê linha por linha no arquivo e separa os tokens
        while line:
            if re.search(r"/\*", line):
                countCmt = 1
                abriuNaLinha = cnt
            if re.search(r"\*\/", line):
                countCmt = 2
            line = fp.readline()
            cnt += 1

        if countCmt == 2:
            countCmt = 0
            return False, 'abriu e fechou o comentario'
        else:
            return True, 'ERRO: COMENTARIO NÃO TERMINA, LINHA {}'.format(abriuNaLinha)

def removeComentarios(palavra):
    return re.sub('/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/', '', palavra)

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
        return print("ERRO: CARACTERE INVALIDO NA LINHA {} ::{}::".format(None, palavra))

def main():
    #Abre arquivo
    filepath = 'guru99.txt'
    found, p = verificaComentario(filepath)
    if found:
        print(p)
    else:
        f = open(filepath, "r")
        newText = removeComentarios(f.read())
        splitted_text = re.split("\s", newText)
        #para cada token verifica qual a qual classe de lexema ele esta inserido
        for word in splitted_text:
            analisador(word)
        '''
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
                    analisador(word, cnt)
                line = fp.readline()
                cnt += 1'''

if __name__== "__main__":
  main()


