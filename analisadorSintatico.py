# -*- coding:utf8 -*-

from AnaLex import *
a = "C = 8 ** 5 + 10 - 4.5 * ( 7 / 5 )"
b = "Z - 10"
c = "A = 10 + ( 5 * 2.5 ) ; B = B + 2"
d = "A = ( 5 + 2"
lex = AnaLex(d)
lex.analex()

def program():
    print("Entrou em program com token:", lex.nextToken(), "Operador:", lex.nextLexema())
    if lex.nextToken() == "BEGIN":
        lex.lex()
        flag = stmt_list()
    else:
        print("Erro: inicio do programa nao encontrado!")
    if lex.nextToken() == "FIM" and flag:
        if lex.token < len(lex.tokens)-1:
            print("Erro: programa invalido")
        else:
            print("Programa executou com sucesso")
    else:
        print("Erro: programa invalido, EOF nao encontrado!")
    

def stmt_list():
    print("Entrou em stmt_list com token:", lex.nextToken(), "Operador:", lex.nextLexema())
    stmt()
    if lex.nextToken() == "PONTO_VIRGULA":
        lex.lex()
        if lex.nextToken() == "FIM":
            return False
        return stmt_list()
    print("Saiu de stmt_list com token:", lex.nextToken(), "Operador:", lex.nextLexema())
    return True
    

def stmt():
    print("Entrou em stmt com token:", lex.nextToken(), "Operador:", lex.nextLexema())
    if lex.nextToken() == "IDENTIFICADOR":
        lex.lex()
        if lex.nextToken() == "OPERADOR_ATRIB":
            lex.lex()
            expression()
        else:
            print("Erro: esperado OPERADOR_ATRIB")
    else:
        print("Erro: esperado um IDENTIFICADOR")
    print("Saiu de stmt com token:", lex.nextToken(), "Operador:", lex.nextLexema())


def exp():
    print("Entrou em exp com token:", lex.nextToken(), "Operador:", lex.nextLexema())
    if lex.nextToken() == "IDENTIFICADOR":
        lex.lex()
    elif lex.nextToken() == "LITERAL_INTEIRO":
        lex.lex()
    elif lex.nextToken() == "LITERAL_FLOAT":
        lex.lex()
    elif lex.nextToken() == "PARENTESIS_ESQ":
        lex.lex()
        expression()
        if lex.nextToken() == "PARENTESIS_DIR":
            lex.lex()
        else:
            print("Erro: esperado parentese direito!")
    else:
        print("Erro: esperado um identificador <exp>!")
    print("Saiu de exp com token:", lex.nextToken(), "Operador:", lex.nextLexema())

def expression():
    print("Entrou em expression com token:", lex.nextToken(), "Operador:", lex.nextLexema())
    term()
    while lex.nextToken() == "OPERADOR_SOMA" or lex.nextToken() == "OPERADOR_SUBT":
        lex.lex()
        term()
    print("Saiu de expression com token:", lex.nextToken(), "Operador:", lex.nextLexema())

def term():
    print("Entrou em term com token:", lex.nextToken(), "Operador:", lex.nextLexema())
    factor()
    while lex.nextToken() == "OPERADOR_MULT" or lex.nextToken() == "OPERADOR_DIVI": 
        lex.lex()
        factor()
    print("Saiu de term com token:", lex.nextToken(), "Operador:", lex.nextLexema())

def factor():
    print("Entrou em factor com token:", lex.nextToken(), "Operador:", lex.nextLexema())
    exp()
    if(lex.nextToken() == 'OPERADOR_EXPO'):
        lex.lex()
        factor()
    print("Saiu de factor com token:", lex.nextToken(), "Operador:", lex.nextLexema())



program()