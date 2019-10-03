def ehInteiro(lexema):
    return lexema.isdigit()

def ehFloat(lexema):
    if '.' in lexema:
        a = lexema.split('.')
        if a[0].isdigit and a[1].isdigit:
            return True
    return False

class Token:
    def __init__(self, lexema, tipo):
        self.lexema = lexema
        self.tipo = tipo
    def getToken(self):
        return self.tipo

class AnaLex:
    def __init__(self, texto):
        self.lexemas = texto.split(' ')
        self.tokens = []
        self.token = 0
    def analex(self):
        self.tokens.append(Token('begin', "BEGIN"))
        for lexema in self.lexemas:
            if lexema == '(':
                self.tokens.append(Token(lexema, 'PARENTESIS_ESQ'))
            elif lexema == ')':
                self.tokens.append(Token(lexema, 'PARENTESIS_DIR'))
            elif lexema == '+':
                self.tokens.append(Token(lexema, 'OPERADOR_SOMA'))
            elif lexema == '-':
                self.tokens.append(Token(lexema, 'OPERADOR_SUBT'))
            elif lexema == '*':
                self.tokens.append(Token(lexema, 'OPERADOR_MULT'))
            elif lexema == '**':
                self.tokens.append(Token(lexema, 'OPERADOR_EXPO'))
            elif lexema == '/':
                self.tokens.append(Token(lexema, 'OPERADOR_DIVI'))
            elif lexema == '=':
                self.tokens.append(Token(lexema, 'OPERADOR_ATRIB'))
            elif lexema == ';':
                self.tokens.append(Token(lexema, 'PONTO_VIRGULA'))
            elif ehInteiro(lexema):
                self.tokens.append(Token(lexema, 'LITERAL_INTEIRO'))
            elif ehFloat(lexema):
                self.tokens.append(Token(lexema, 'LITERAL_FLOAT'))
            else:
                self.tokens.append(Token(lexema, "IDENTIFICADOR"))
        self.tokens.append(Token("EOF", "FIM"))
    def lex(self):
        self.token += 1
    def nextToken(self):
        return self.tokens[self.token].getToken()
    def nextLexema(self):
        return self.tokens[self.token].lexema
    def seeTokens(self):
        for elem in self.tokens:
            print(elem.lexema, elem.tipo)
