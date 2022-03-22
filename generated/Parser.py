# Generated from D:/Sebas/TEC/2022/1 Semestre/Compiladores e Interpretes/MiniPy/miniPython\Parser.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\37")
        buf.write("\u00b1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\7\35\u00a0\n\35\f\35\16\35\u00a3\13\35")
        buf.write("\3\36\3\36\3\36\3\36\7\36\u00a9\n\36\f\36\16\36\u00ac")
        buf.write("\13\36\3\37\3\37\3 \3 \2\2!\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37=\2?\2\3\2\4\3\2\62;\5\2\"\"C\\c|\2\u00b2\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\3A\3\2\2\2\5C\3\2\2\2\7E\3\2\2")
        buf.write("\2\tG\3\2\2\2\13I\3\2\2\2\rL\3\2\2\2\17Q\3\2\2\2\21V\3")
        buf.write("\2\2\2\23\\\3\2\2\2\25b\3\2\2\2\27f\3\2\2\2\31m\3\2\2")
        buf.write("\2\33s\3\2\2\2\35w\3\2\2\2\37z\3\2\2\2!|\3\2\2\2#~\3\2")
        buf.write("\2\2%\u0080\3\2\2\2\'\u0082\3\2\2\2)\u0085\3\2\2\2+\u0087")
        buf.write("\3\2\2\2-\u0089\3\2\2\2/\u008c\3\2\2\2\61\u008f\3\2\2")
        buf.write("\2\63\u0092\3\2\2\2\65\u0096\3\2\2\2\67\u0099\3\2\2\2")
        buf.write("9\u009d\3\2\2\2;\u00a4\3\2\2\2=\u00ad\3\2\2\2?\u00af\3")
        buf.write("\2\2\2AB\7.\2\2B\4\3\2\2\2CD\7<\2\2D\6\3\2\2\2EF\7]\2")
        buf.write("\2F\b\3\2\2\2GH\7_\2\2H\n\3\2\2\2IJ\7k\2\2JK\7h\2\2K\f")
        buf.write("\3\2\2\2LM\7g\2\2MN\7n\2\2NO\7u\2\2OP\7g\2\2P\16\3\2\2")
        buf.write("\2QR\7g\2\2RS\7n\2\2ST\7k\2\2TU\7h\2\2U\20\3\2\2\2VW\7")
        buf.write("y\2\2WX\7j\2\2XY\7k\2\2YZ\7n\2\2Z[\7g\2\2[\22\3\2\2\2")
        buf.write("\\]\7e\2\2]^\7q\2\2^_\7p\2\2_`\7u\2\2`a\7v\2\2a\24\3\2")
        buf.write("\2\2bc\7h\2\2cd\7q\2\2de\7t\2\2e\26\3\2\2\2fg\7t\2\2g")
        buf.write("h\7g\2\2hi\7v\2\2ij\7w\2\2jk\7t\2\2kl\7p\2\2l\30\3\2\2")
        buf.write("\2mn\7r\2\2no\7t\2\2op\7k\2\2pq\7p\2\2qr\7v\2\2r\32\3")
        buf.write("\2\2\2st\7n\2\2tu\7g\2\2uv\7p\2\2v\34\3\2\2\2wx\7k\2\2")
        buf.write("xy\7p\2\2y\36\3\2\2\2z{\7-\2\2{ \3\2\2\2|}\7/\2\2}\"\3")
        buf.write("\2\2\2~\177\7,\2\2\177$\3\2\2\2\u0080\u0081\7\61\2\2\u0081")
        buf.write("&\3\2\2\2\u0082\u0083\7\61\2\2\u0083\u0084\7\61\2\2\u0084")
        buf.write("(\3\2\2\2\u0085\u0086\7@\2\2\u0086*\3\2\2\2\u0087\u0088")
        buf.write("\7>\2\2\u0088,\3\2\2\2\u0089\u008a\7>\2\2\u008a\u008b")
        buf.write("\7?\2\2\u008b.\3\2\2\2\u008c\u008d\7@\2\2\u008d\u008e")
        buf.write("\7?\2\2\u008e\60\3\2\2\2\u008f\u0090\7?\2\2\u0090\u0091")
        buf.write("\7?\2\2\u0091\62\3\2\2\2\u0092\u0093\7c\2\2\u0093\u0094")
        buf.write("\7p\2\2\u0094\u0095\7f\2\2\u0095\64\3\2\2\2\u0096\u0097")
        buf.write("\7q\2\2\u0097\u0098\7t\2\2\u0098\66\3\2\2\2\u0099\u009a")
        buf.write("\7p\2\2\u009a\u009b\7q\2\2\u009b\u009c\7v\2\2\u009c8\3")
        buf.write("\2\2\2\u009d\u00a1\5=\37\2\u009e\u00a0\5=\37\2\u009f\u009e")
        buf.write("\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1")
        buf.write("\u00a2\3\2\2\2\u00a2:\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4")
        buf.write("\u00aa\5? \2\u00a5\u00a9\5? \2\u00a6\u00a9\5=\37\2\u00a7")
        buf.write("\u00a9\7a\2\2\u00a8\u00a5\3\2\2\2\u00a8\u00a6\3\2\2\2")
        buf.write("\u00a8\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3")
        buf.write("\2\2\2\u00aa\u00ab\3\2\2\2\u00ab<\3\2\2\2\u00ac\u00aa")
        buf.write("\3\2\2\2\u00ad\u00ae\t\2\2\2\u00ae>\3\2\2\2\u00af\u00b0")
        buf.write("\t\3\2\2\u00b0@\3\2\2\2\6\2\u00a1\u00a8\u00aa\2")
        return buf.getvalue()


class Parser(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMA = 1
    COLON = 2
    LEFTSQUARE = 3
    RIGHTSQUARE = 4
    IF = 5
    ELSE = 6
    ELIF = 7
    WHILE = 8
    CONST = 9
    FOR = 10
    RETURN = 11
    PRINT = 12
    LEN = 13
    IN = 14
    ADD = 15
    SUB = 16
    MUL = 17
    DIV = 18
    INTDIV = 19
    GT = 20
    LT = 21
    LET = 22
    GET = 23
    EQUAL = 24
    AND = 25
    OR = 26
    NOT = 27
    NUM = 28
    ID = 29

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "':'", "'['", "']'", "'if'", "'else'", "'elif'", "'while'", 
            "'const'", "'for'", "'return'", "'print'", "'len'", "'in'", 
            "'+'", "'-'", "'*'", "'/'", "'//'", "'>'", "'<'", "'<='", "'>='", 
            "'=='", "'and'", "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>",
            "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", "IF", "ELSE", 
            "ELIF", "WHILE", "CONST", "FOR", "RETURN", "PRINT", "LEN", "IN", 
            "ADD", "SUB", "MUL", "DIV", "INTDIV", "GT", "LT", "LET", "GET", 
            "EQUAL", "AND", "OR", "NOT", "NUM", "ID" ]

    ruleNames = [ "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", "IF", "ELSE", 
                  "ELIF", "WHILE", "CONST", "FOR", "RETURN", "PRINT", "LEN", 
                  "IN", "ADD", "SUB", "MUL", "DIV", "INTDIV", "GT", "LT", 
                  "LET", "GET", "EQUAL", "AND", "OR", "NOT", "NUM", "ID", 
                  "DIGIT", "LETTER" ]

    grammarFileName = "Parser.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


