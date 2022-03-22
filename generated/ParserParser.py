# Generated from D:/Sebas/TEC/2022/1 Semestre/Compiladores e Interpretes/MiniPy/miniPython\Parser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3!")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\3\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class ParserParser ( Parser ):

    grammarFileName = "Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "':'", "'['", "']'", "'if'", "'else'", 
                     "'elif'", "'while'", "'const'", "'for'", "'return'", 
                     "'print'", "'len'", "'in'", "'+'", "'-'", "'*'", "'/'", 
                     "'//'", "'>'", "'<'", "'<='", "'>='", "'=='", "'and'", 
                     "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>", "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", 
                      "IF", "ELSE", "ELIF", "WHILE", "CONST", "FOR", "RETURN", 
                      "PRINT", "LEN", "IN", "ADD", "SUB", "MUL", "DIV", 
                      "INTDIV", "GT", "LT", "LET", "GET", "EQUAL", "AND", 
                      "OR", "NOT", "NUM", "ID", "INDENT", "DEDENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    COMMA=1
    COLON=2
    LEFTSQUARE=3
    RIGHTSQUARE=4
    IF=5
    ELSE=6
    ELIF=7
    WHILE=8
    CONST=9
    FOR=10
    RETURN=11
    PRINT=12
    LEN=13
    IN=14
    ADD=15
    SUB=16
    MUL=17
    DIV=18
    INTDIV=19
    GT=20
    LT=21
    LET=22
    GET=23
    EQUAL=24
    AND=25
    OR=26
    NOT=27
    NUM=28
    ID=29
    INDENT=30
    DEDENT=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ParserParser.COMMA, 0)

        def getRuleIndex(self):
            return ParserParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ParserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(ParserParser.COMMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





