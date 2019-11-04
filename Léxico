```python

################################################################################
#                                                                              #
#  Representação dos símbolos de acordo com as colunas da tabela de transição  #
#																		
################################################################################
# simbolo D (digitos) : coluna 0
# simbolo L (letras) : coluna 1
# simbolo " (aspas) : coluna 2
# simbolo { (abre Chaves) : coluna 3
# simbolo } (fecha Chaves) : coluna 4
# simbolo ' ' (espaço em branco) : coluna 5
# simbolo EOF (fim de arquivo) : coluna 6
# simbolo < (sinal menor) : coluna 7
# simbolo > (sinal maior) : coluna 8
# simbolo = (sinal igual) : coluna 9
# simbolo - (sinal menos) : coluna 10
# simbolo + (sinal mais) : coluna 11
# simbolo * (sinal multiplicação) : coluna 12
# simbolo / (sinal divisão) : coluna 13
# simbolo . (ponto) : coluna 14
# simbolo ( (abre parenteses) : coluna 15
# simbolo ) (fecha parenteses) : coluna 16
# simbolo ; (sinal delimitador) : coluna 17
# simbolo ERRO (sinal de erro ou qualquer caracter não previsto): coluna 18
# simbolo e (nº cientifico) : coluna 19
# simbolo E (nº cientifico) : coluna 20
# simbolo _ (underline) : coluna 21
# simbolo /n (quebra de linha) : coluna 5
# simbolo /t (tabulação) : coluna 5
################################################################################

import sys
import string


'''*********************** ETAPA 1: ANALISADOR LÉXICO ************************'''

### TABELA DE SIMBOLOS INICIALIZADA COM AS PALAVRAS RESERVADAS DA LINGUAGEM ### 
symbolTable = {}
symbolTable ['inicio'] = 'inicio', 'inicio', 'Delimitador'
symbolTable ['varinicio'] = 'varinicio', 'varinicio', 'Delimitador'
symbolTable ['varfim'] = 'varfim', 'varfim', 'Delimitador'
symbolTable ['escreva'] = 'escreva', 'escreva', 'Função'
symbolTable ['leia'] = 'leia', 'leia', 'Função'
symbolTable ['se'] = 'se', 'se', 'Condicional'
symbolTable ['entao'] = 'entao', 'entao', 'Condicional'
symbolTable ['senao'] = 'senao', 'senao', 'Condicional'
symbolTable ['fimse'] = 'fimse', 'fimse', 'Delimitador'
symbolTable ['fim'] = 'fim', 'fim', 'Delimitador'
symbolTable ['inteiro'] = 'int', 'inteiro', 'Numerico'
symbolTable ['literal'] = 'lit', 'literal', 'Literal'
symbolTable ['real'] = 'real', 'real', 'Numerico'


### TABELA DE TRANSIÇÃO DO AUTOMATO FINITO DETERMINISTICO ###
tableTrasition = [
	[ 1,  8,  6, 21, -1,  0,  9, 11, 14, 10, 20, 20, 20, 20,  0, 19, 18, 16, 17,  8,  8, -1],
	[ 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  2, -1, -1, -1, -1,  4,  4, -1],
	[ 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[ 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  4,  4, -1],
	[22, -1, -1, -1, -1, -1, -1, -1, -1, -1,  5,  5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[ 6,  6,  7,  6,  6,  6, -1,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[ 8,  8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  8,  8,  8],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, 12, 15, 13, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	[21, 21, 21, 21,  0, 21, -1, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
	[22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
]


## Retorna o número correspondente ao símbolo ##
def symbol(currentChar, prevState):
	if currentChar.isdigit():
		return 0 # É um digito
	elif currentChar == 'e' and prevState == 1 or currentChar == 'e' and prevState == 3: # Número Científico
		return 19
	elif currentChar == 'E' and prevState == 1 or currentChar == 'E' and prevState == 3: # Número Científico
		return 20
	elif currentChar.isalpha() :
		return 1 # É uma letra
	elif currentChar == '"':
		return 2
	elif currentChar == '{':
		return 3
	elif currentChar == '}':
		return 4
	elif currentChar == ' ' or currentChar == '\n' or currentChar == '\t':
		return 5
	elif currentChar == 'EOF':
		return 6
	elif currentChar == '<':
		return 7
	elif currentChar == '>':
		return 8
	elif currentChar == '=':
		return 9
	elif currentChar == '-':
		return 10
	elif currentChar == '+':
		return 11
	elif currentChar == '*':
		return 12
	elif currentChar == '/':
		return 13
	elif currentChar == '.':
		return 14
	elif currentChar == '(':
		return 15
	elif currentChar == ')':
		return 16
	elif currentChar == ';':
		return 17
	elif currentChar == '_':
		return 21
	else:
		return 18  # Qualquer caracter diferente 
	
		
# Retorna o token correspondente ao símbolo 
def token(finalState):
		if finalState == 1 or finalState == 3 or finalState == 22:
			return 'num' # Constante Numerica

		elif finalState == 7:
			return 'literal' # Constante Literal ou comentário 

		elif finalState == 8:
			return 'id' # Identificador

		elif finalState == 9:
			return 'EOF' # Fim de arquivo

		elif finalState == 10 or finalState == 11 or finalState == 12 or finalState == 14 or finalState == 15:
			return 'OPR' # Operador relacional

		elif finalState == 13:
			return 'RCB' # Atribuição

		elif finalState == 20:
			return 'OPM' # Operador aritmético

		elif finalState == 19:
			return 'AB_P' # Abre parênteses

		elif finalState == 18:
			return 'FC_P' # Fecha parênteses
		
		elif finalState == 16:
			return 'PT_V' # Ponto vírgula

		elif finalState == 17:
			return 'ERRO' 

# Verifica se o estado atual é um estado final
def isFinalStates(state):
	# String contendo os estados finais da tabela de transição
	finalState = [1, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22]
	size = len(finalState)
	i = 0
	while i < size:
		if state == finalState[i]:
			return True
		i += 1
	return False


# Faz a analise lexica e retorna o token correspondente
def lexico():
	global cursor
	global line
	global arquivo
	global numChar
	global position

	typeToken = {} # Dicionario usado para auxiliar quando for enviar tokens de outros tipos que nao seja um tipo "id"

	if cursor == numChar:
		bufferInput = ''
		typeToken[bufferInput] = ['EOF', bufferInput, 'Fim de arquivo']
		return typeToken[bufferInput]

	currentState = 0
	prevState = 0
	bufferInput = ''
	char = arquivo[cursor]
	flag = 0

	nextState = tableTrasition[currentState][symbol(char, prevState)]

	while nextState != -1:
		currentState = nextState # Atualiza o estado atual

		if char == '\n':
			line += 1 # Inidica a linha do arquivo atual
			position = 1 

		if char != '\n' and char != '\t' and char != ' ': # Ignora quebra de linha, tabulação e espaço em branco
			bufferInput += char # Adiciona o caracter lido no buffer de entrada 
			if '{' in bufferInput:
				if '}' in bufferInput:
					bufferInput = ''
				
		cursor += 1 # Indica a posição do cursor no arquivo
		position += 1 

		if cursor < numChar: # Verfica se o cursor chegou no final do arquivo
			char = arquivo[cursor] # Pega o proximo caracter
			prevState = currentState # Atualiza o estado anterior

		else:
			flag = 1 # Sinaliza que chegou no final do arquivo 

		if flag != 1:
			nextState = tableTrasition[currentState][symbol(char, prevState)] # Retorna proximo estado
		else:
			# Caso seja o último caracter lido do arquivo o cursor não estará apontando para 
			# a proxima posição, logo próximo estado recebe -1 para o loop parar, para análise
			# do que está no buffer de entrada seja feita
			nextState = -1 


	if isFinalStates(currentState):
		if bufferInput not in symbolTable and token(currentState) == 'id':
			symbolTable[bufferInput] = 'id', bufferInput, ' '

			#print('\n\t\tTABELA DE SÍMBOLOS')
			#print('\n\t|  TOKEN   |   LEXEMA   |   TIPO   |')
			#print('\t------------------------------------')

			#aux = symbolTable[bufferInput]
			#typeToken = str(aux[0])
			return symbolTable[bufferInput] #typeToken
			#print('\t------------------------------------')


			#print('\n\nTABELA DE SÍMBOLOS ATUALIZADA\n')
			#for x in symbolTable.items():
			#	print(x)
		
		elif bufferInput in symbolTable:
			#aux = symbolTable[bufferInput]
			#typeToken = str(aux[0])
			return symbolTable[bufferInput] #typeToken
			#print('\t------------------------------------')

		
		else:
			if token(currentState) == 'ERRO': # Caracter inválido lido 
				print('\n\nERRO ECONTRADO!!')
				print('Linha: {} | Posição: {}'.format(line, position-2))
				print('Caracter "{}" não é permitido pela linguagem'.format(bufferInput[len(bufferInput)-1]))
				sys.exit()
			else:
				if token(currentState) == 'num':
					typeToken[bufferInput] = ['num', bufferInput, bufferInput]
					return typeToken[bufferInput]
				elif token(currentState) == 'literal':
					typeToken[bufferInput] = ['literal', bufferInput, 'Constante Literal']
					return typeToken[bufferInput]
				elif token(currentState) == 'OPR':
					typeToken[bufferInput] = ['opr', bufferInput, bufferInput]
					return typeToken[bufferInput]
				elif token(currentState) == 'RCB':
					typeToken[bufferInput] = ['rcb', bufferInput, '=']
					return typeToken[bufferInput]
				elif token(currentState) == 'OPM':
					typeToken[bufferInput] = ['opm', bufferInput, bufferInput]
					return typeToken[bufferInput]
				elif token(currentState) == 'AB_P':
					typeToken[bufferInput] = ['AB_P', bufferInput, 'Abre Parênteses']
					return typeToken[bufferInput]
				elif token(currentState) == 'FC_P':
					typeToken[bufferInput] = ['FC_P', bufferInput, 'Fecha Parênteses']
					return typeToken[bufferInput]
				elif token(currentState) == 'PT_V':
					typeToken[bufferInput] = ['PT_V', bufferInput, 'Ponto Vírgula']
					return typeToken[bufferInput]

	# Verifica a condição que gerou o erro
	else:
		print('\n\nERRO LEXICO ECONTRADO!!')
		print('Linha: {} | Posição: {}'.format(line, position-2))
		
		if currentState == 0 and char == '}':
			print('Tipo de erro: Fechamento de chave sem ter uma chave aberta')
			sys.exit()
		elif currentState == 2:
			print('Tipo de erro: Esperava número após o ponto!')
			sys.exit()
		elif currentState == 4:
			print('Tipo de erro: Notação de número cíentifico inválido')
			sys.exit()
		elif currentState == 5:
			print('Tipo de erro: Esperava número após notação científica!')
			sys.exit()
		elif currentState == 6:
			print('Tipo de erro: Esperava fechamento da aspas!')
			sys.exit()
		elif currentState == 21:
			print('Tipo de erro: Esperava fechamento da chave!')
			sys.exit()
		else:
			print('Erro inesperado!')
sys.exit()
```
