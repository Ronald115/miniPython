# Generated from D:/Sebas/TEC/2022/1 Semestre/Compiladores e Interpretes/ProyectoCompiladores/miniPython\miParser.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from miParserParser import miParserParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2/")
        buf.write("\u013c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\5\13|\n\13\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\5%\u00d8\n%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\5\'\u00e7\n\'\3(\3(\3(\3(\3(\5(\u00ee")
        buf.write("\n(\3(\3(\3)\3)\3)\3)\3)\7)\u00f7\n)\f)\16)\u00fa\13)")
        buf.write("\3)\3)\3*\3*\7*\u0100\n*\f*\16*\u0103\13*\3+\3+\3+\3+")
        buf.write("\7+\u0109\n+\f+\16+\u010c\13+\3,\5,\u010f\n,\3,\3,\7,")
        buf.write("\u0113\n,\f,\16,\u0116\13,\3-\3-\3-\3-\3.\3.\5.\u011e")
        buf.write("\n.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\7\62\u012d\n\62\f\62\16\62\u0130\13\62\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\7\63\u0138\n\63\f\63\16\63\u013b")
        buf.write("\13\63\3\u012e\2\64\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\2a\2c\2e\2\3\2\t")
        buf.write("\3\2))\4\2\13\13\"\"\6\2\13\f\17\17\"\"--\3\2\62;\4\2")
        buf.write("C\\c|\7\2\"\"&\'./<=aa\4\2\f\f\17\17\2\u0149\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\3g\3\2\2\2\5i\3")
        buf.write("\2\2\2\7k\3\2\2\2\tm\3\2\2\2\13o\3\2\2\2\rq\3\2\2\2\17")
        buf.write("s\3\2\2\2\21u\3\2\2\2\23w\3\2\2\2\25{\3\2\2\2\27}\3\2")
        buf.write("\2\2\31\u0080\3\2\2\2\33\u0085\3\2\2\2\35\u008a\3\2\2")
        buf.write("\2\37\u0090\3\2\2\2!\u0096\3\2\2\2#\u009a\3\2\2\2%\u00a1")
        buf.write("\3\2\2\2\'\u00a7\3\2\2\2)\u00ab\3\2\2\2+\u00ae\3\2\2\2")
        buf.write("-\u00b2\3\2\2\2/\u00b4\3\2\2\2\61\u00b6\3\2\2\2\63\u00b9")
        buf.write("\3\2\2\2\65\u00bb\3\2\2\2\67\u00bd\3\2\2\29\u00bf\3\2")
        buf.write("\2\2;\u00c1\3\2\2\2=\u00c3\3\2\2\2?\u00c6\3\2\2\2A\u00c9")
        buf.write("\3\2\2\2C\u00cc\3\2\2\2E\u00cf\3\2\2\2G\u00d2\3\2\2\2")
        buf.write("I\u00d7\3\2\2\2K\u00d9\3\2\2\2M\u00e6\3\2\2\2O\u00e8\3")
        buf.write("\2\2\2Q\u00f1\3\2\2\2S\u00fd\3\2\2\2U\u0104\3\2\2\2W\u010e")
        buf.write("\3\2\2\2Y\u0117\3\2\2\2[\u011d\3\2\2\2]\u0121\3\2\2\2")
        buf.write("_\u0123\3\2\2\2a\u0125\3\2\2\2c\u0127\3\2\2\2e\u0135\3")
        buf.write("\2\2\2gh\7.\2\2h\4\3\2\2\2ij\7<\2\2j\6\3\2\2\2kl\7]\2")
        buf.write("\2l\b\3\2\2\2mn\7_\2\2n\n\3\2\2\2op\7*\2\2p\f\3\2\2\2")
        buf.write("qr\7+\2\2r\16\3\2\2\2st\7?\2\2t\20\3\2\2\2uv\t\2\2\2v")
        buf.write("\22\3\2\2\2wx\7$\2\2x\24\3\2\2\2y|\5\21\t\2z|\5\23\n\2")
        buf.write("{y\3\2\2\2{z\3\2\2\2|\26\3\2\2\2}~\7k\2\2~\177\7h\2\2")
        buf.write("\177\30\3\2\2\2\u0080\u0081\7g\2\2\u0081\u0082\7n\2\2")
        buf.write("\u0082\u0083\7u\2\2\u0083\u0084\7g\2\2\u0084\32\3\2\2")
        buf.write("\2\u0085\u0086\7g\2\2\u0086\u0087\7n\2\2\u0087\u0088\7")
        buf.write("k\2\2\u0088\u0089\7h\2\2\u0089\34\3\2\2\2\u008a\u008b")
        buf.write("\7y\2\2\u008b\u008c\7j\2\2\u008c\u008d\7k\2\2\u008d\u008e")
        buf.write("\7n\2\2\u008e\u008f\7g\2\2\u008f\36\3\2\2\2\u0090\u0091")
        buf.write("\7e\2\2\u0091\u0092\7q\2\2\u0092\u0093\7p\2\2\u0093\u0094")
        buf.write("\7u\2\2\u0094\u0095\7v\2\2\u0095 \3\2\2\2\u0096\u0097")
        buf.write("\7h\2\2\u0097\u0098\7q\2\2\u0098\u0099\7t\2\2\u0099\"")
        buf.write("\3\2\2\2\u009a\u009b\7t\2\2\u009b\u009c\7g\2\2\u009c\u009d")
        buf.write("\7v\2\2\u009d\u009e\7w\2\2\u009e\u009f\7t\2\2\u009f\u00a0")
        buf.write("\7p\2\2\u00a0$\3\2\2\2\u00a1\u00a2\7r\2\2\u00a2\u00a3")
        buf.write("\7t\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6")
        buf.write("\7v\2\2\u00a6&\3\2\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9")
        buf.write("\7g\2\2\u00a9\u00aa\7p\2\2\u00aa(\3\2\2\2\u00ab\u00ac")
        buf.write("\7k\2\2\u00ac\u00ad\7p\2\2\u00ad*\3\2\2\2\u00ae\u00af")
        buf.write("\7f\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1\7h\2\2\u00b1,\3")
        buf.write("\2\2\2\u00b2\u00b3\7-\2\2\u00b3.\3\2\2\2\u00b4\u00b5\7")
        buf.write("/\2\2\u00b5\60\3\2\2\2\u00b6\u00b7\7,\2\2\u00b7\u00b8")
        buf.write("\7,\2\2\u00b8\62\3\2\2\2\u00b9\u00ba\7,\2\2\u00ba\64\3")
        buf.write("\2\2\2\u00bb\u00bc\7\61\2\2\u00bc\66\3\2\2\2\u00bd\u00be")
        buf.write("\7\'\2\2\u00be8\3\2\2\2\u00bf\u00c0\7@\2\2\u00c0:\3\2")
        buf.write("\2\2\u00c1\u00c2\7>\2\2\u00c2<\3\2\2\2\u00c3\u00c4\7>")
        buf.write("\2\2\u00c4\u00c5\7?\2\2\u00c5>\3\2\2\2\u00c6\u00c7\7@")
        buf.write("\2\2\u00c7\u00c8\7?\2\2\u00c8@\3\2\2\2\u00c9\u00ca\7?")
        buf.write("\2\2\u00ca\u00cb\7?\2\2\u00cbB\3\2\2\2\u00cc\u00cd\7#")
        buf.write("\2\2\u00cd\u00ce\7?\2\2\u00ceD\3\2\2\2\u00cf\u00d0\7^")
        buf.write("\2\2\u00d0\u00d1\7p\2\2\u00d1F\3\2\2\2\u00d2\u00d3\7^")
        buf.write("\2\2\u00d3\u00d4\7v\2\2\u00d4H\3\2\2\2\u00d5\u00d8\5E")
        buf.write("#\2\u00d6\u00d8\5G$\2\u00d7\u00d5\3\2\2\2\u00d7\u00d6")
        buf.write("\3\2\2\2\u00d8J\3\2\2\2\u00d9\u00da\5S*\2\u00da\u00db")
        buf.write("\7\60\2\2\u00db\u00dc\5S*\2\u00dcL\3\2\2\2\u00dd\u00de")
        buf.write("\7V\2\2\u00de\u00df\7t\2\2\u00df\u00e0\7w\2\2\u00e0\u00e7")
        buf.write("\7g\2\2\u00e1\u00e2\7H\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4")
        buf.write("\7n\2\2\u00e4\u00e5\7u\2\2\u00e5\u00e7\7g\2\2\u00e6\u00dd")
        buf.write("\3\2\2\2\u00e6\u00e1\3\2\2\2\u00e7N\3\2\2\2\u00e8\u00ed")
        buf.write("\5\21\t\2\u00e9\u00ee\5_\60\2\u00ea\u00ee\5]/\2\u00eb")
        buf.write("\u00ee\5a\61\2\u00ec\u00ee\5I%\2\u00ed\u00e9\3\2\2\2\u00ed")
        buf.write("\u00ea\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ec\3\2\2\2")
        buf.write("\u00ee\u00ef\3\2\2\2\u00ef\u00f0\5\21\t\2\u00f0P\3\2\2")
        buf.write("\2\u00f1\u00f8\5\25\13\2\u00f2\u00f7\5_\60\2\u00f3\u00f7")
        buf.write("\5]/\2\u00f4\u00f7\5a\61\2\u00f5\u00f7\5I%\2\u00f6\u00f2")
        buf.write("\3\2\2\2\u00f6\u00f3\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f5\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2")
        buf.write("\u00f8\u00f9\3\2\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00f8\3")
        buf.write("\2\2\2\u00fb\u00fc\5\25\13\2\u00fcR\3\2\2\2\u00fd\u0101")
        buf.write("\5]/\2\u00fe\u0100\5]/\2\u00ff\u00fe\3\2\2\2\u0100\u0103")
        buf.write("\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102")
        buf.write("T\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u010a\5_\60\2\u0105")
        buf.write("\u0109\5_\60\2\u0106\u0109\5]/\2\u0107\u0109\7a\2\2\u0108")
        buf.write("\u0105\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0107\3\2\2\2")
        buf.write("\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3")
        buf.write("\2\2\2\u010bV\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010f")
        buf.write("\7\17\2\2\u010e\u010d\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write("\u0110\3\2\2\2\u0110\u0114\7\f\2\2\u0111\u0113\t\3\2\2")
        buf.write("\u0112\u0111\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0112\3")
        buf.write("\2\2\2\u0114\u0115\3\2\2\2\u0115X\3\2\2\2\u0116\u0114")
        buf.write("\3\2\2\2\u0117\u0118\t\4\2\2\u0118\u0119\3\2\2\2\u0119")
        buf.write("\u011a\b-\2\2\u011aZ\3\2\2\2\u011b\u011e\5c\62\2\u011c")
        buf.write("\u011e\5e\63\2\u011d\u011b\3\2\2\2\u011d\u011c\3\2\2\2")
        buf.write("\u011e\u011f\3\2\2\2\u011f\u0120\b.\2\2\u0120\\\3\2\2")
        buf.write("\2\u0121\u0122\t\5\2\2\u0122^\3\2\2\2\u0123\u0124\t\6")
        buf.write("\2\2\u0124`\3\2\2\2\u0125\u0126\t\7\2\2\u0126b\3\2\2\2")
        buf.write("\u0127\u0128\7$\2\2\u0128\u0129\7$\2\2\u0129\u012a\7$")
        buf.write("\2\2\u012a\u012e\3\2\2\2\u012b\u012d\13\2\2\2\u012c\u012b")
        buf.write("\3\2\2\2\u012d\u0130\3\2\2\2\u012e\u012f\3\2\2\2\u012e")
        buf.write("\u012c\3\2\2\2\u012f\u0131\3\2\2\2\u0130\u012e\3\2\2\2")
        buf.write("\u0131\u0132\7$\2\2\u0132\u0133\7$\2\2\u0133\u0134\7$")
        buf.write("\2\2\u0134d\3\2\2\2\u0135\u0139\7%\2\2\u0136\u0138\n\b")
        buf.write("\2\2\u0137\u0136\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137")
        buf.write("\3\2\2\2\u0139\u013a\3\2\2\2\u013af\3\2\2\2\u013b\u0139")
        buf.write("\3\2\2\2\21\2{\u00d7\u00e6\u00ed\u00f6\u00f8\u0101\u0108")
        buf.write("\u010a\u010e\u0114\u011d\u012e\u0139\3\b\2\2")
        return buf.getvalue()


class miParserLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMA = 1
    COLON = 2
    LEFTSQUARE = 3
    RIGHTSQUARE = 4
    LEFTP = 5
    RIGHTP = 6
    ASSIGN = 7
    SQUOTES = 8
    DQUOTES = 9
    QUOTES = 10
    IF = 11
    ELSE = 12
    ELIF = 13
    WHILE = 14
    CONST = 15
    FOR = 16
    RETURN = 17
    PRINT = 18
    LEN = 19
    IN = 20
    DEF = 21
    ADD = 22
    SUB = 23
    POW = 24
    MUL = 25
    DIV = 26
    MOD = 27
    GT = 28
    LT = 29
    LET = 30
    GET = 31
    EQUAL = 32
    NOTEQUAL = 33
    BSN = 34
    BST = 35
    ES = 36
    FLOAT = 37
    BOOL = 38
    CHAR = 39
    STRING = 40
    NUM = 41
    ID = 42
    NEWLINE = 43
    WS = 44
    SKIPP = 45

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "':'", "'['", "']'", "'('", "')'", "'='", "'\"'", "'if'", 
            "'else'", "'elif'", "'while'", "'const'", "'for'", "'return'", 
            "'print'", "'len'", "'in'", "'def'", "'+'", "'-'", "'**'", "'*'", 
            "'/'", "'%'", "'>'", "'<'", "'<='", "'>='", "'=='", "'!='", 
            "'\\n'", "'\\t'" ]

    symbolicNames = [ "<INVALID>",
            "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", "LEFTP", "RIGHTP", 
            "ASSIGN", "SQUOTES", "DQUOTES", "QUOTES", "IF", "ELSE", "ELIF", 
            "WHILE", "CONST", "FOR", "RETURN", "PRINT", "LEN", "IN", "DEF", 
            "ADD", "SUB", "POW", "MUL", "DIV", "MOD", "GT", "LT", "LET", 
            "GET", "EQUAL", "NOTEQUAL", "BSN", "BST", "ES", "FLOAT", "BOOL", 
            "CHAR", "STRING", "NUM", "ID", "NEWLINE", "WS", "SKIPP" ]

    ruleNames = [ "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", "LEFTP", 
                  "RIGHTP", "ASSIGN", "SQUOTES", "DQUOTES", "QUOTES", "IF", 
                  "ELSE", "ELIF", "WHILE", "CONST", "FOR", "RETURN", "PRINT", 
                  "LEN", "IN", "DEF", "ADD", "SUB", "POW", "MUL", "DIV", 
                  "MOD", "GT", "LT", "LET", "GET", "EQUAL", "NOTEQUAL", 
                  "BSN", "BST", "ES", "FLOAT", "BOOL", "CHAR", "STRING", 
                  "NUM", "ID", "NEWLINE", "WS", "SKIPP", "DIGIT", "LETTER", 
                  "SYMBOLS", "COMMENT", "LINECOMMENT" ]

    grammarFileName = "miParser.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class MyCoolDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: miParserLexer = lexer

        def pull_token(self):
            return super(miParserLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.MyCoolDenter(self, self.NEWLINE, miParserParser.INDENT, miParserParser.DEDENT, False)
        return self.denter.next_token()


