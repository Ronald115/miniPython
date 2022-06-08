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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2.")
        buf.write("\u0138\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\5\13z\n\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\5$")
        buf.write("\u00d4\n$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u00e3")
        buf.write("\n&\3\'\3\'\3\'\3\'\3\'\5\'\u00ea\n\'\3\'\3\'\3(\3(\3")
        buf.write("(\3(\3(\7(\u00f3\n(\f(\16(\u00f6\13(\3(\3(\3)\3)\7)\u00fc")
        buf.write("\n)\f)\16)\u00ff\13)\3*\3*\3*\3*\7*\u0105\n*\f*\16*\u0108")
        buf.write("\13*\3+\5+\u010b\n+\3+\3+\7+\u010f\n+\f+\16+\u0112\13")
        buf.write("+\3,\3,\3,\3,\3-\3-\5-\u011a\n-\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\61\7\61\u0129\n\61\f\61\16")
        buf.write("\61\u012c\13\61\3\61\3\61\3\61\3\61\3\62\3\62\7\62\u0134")
        buf.write("\n\62\f\62\16\62\u0137\13\62\3\u012a\2\63\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("\2]\2_\2a\2c\2\3\2\t\3\2))\4\2\13\13\"\"\6\2\13\f\17\17")
        buf.write("\"\"--\3\2\62;\4\2C\\c|\7\2\"\"&\'./<=aa\4\2\f\f\17\17")
        buf.write("\2\u0145\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\3e\3\2")
        buf.write("\2\2\5g\3\2\2\2\7i\3\2\2\2\tk\3\2\2\2\13m\3\2\2\2\ro\3")
        buf.write("\2\2\2\17q\3\2\2\2\21s\3\2\2\2\23u\3\2\2\2\25y\3\2\2\2")
        buf.write("\27{\3\2\2\2\31~\3\2\2\2\33\u0083\3\2\2\2\35\u0088\3\2")
        buf.write("\2\2\37\u008e\3\2\2\2!\u0094\3\2\2\2#\u0098\3\2\2\2%\u009f")
        buf.write("\3\2\2\2\'\u00a5\3\2\2\2)\u00a9\3\2\2\2+\u00ac\3\2\2\2")
        buf.write("-\u00b0\3\2\2\2/\u00b2\3\2\2\2\61\u00b4\3\2\2\2\63\u00b6")
        buf.write("\3\2\2\2\65\u00b8\3\2\2\2\67\u00bb\3\2\2\29\u00bd\3\2")
        buf.write("\2\2;\u00bf\3\2\2\2=\u00c2\3\2\2\2?\u00c5\3\2\2\2A\u00c8")
        buf.write("\3\2\2\2C\u00cb\3\2\2\2E\u00ce\3\2\2\2G\u00d3\3\2\2\2")
        buf.write("I\u00d5\3\2\2\2K\u00e2\3\2\2\2M\u00e4\3\2\2\2O\u00ed\3")
        buf.write("\2\2\2Q\u00f9\3\2\2\2S\u0100\3\2\2\2U\u010a\3\2\2\2W\u0113")
        buf.write("\3\2\2\2Y\u0119\3\2\2\2[\u011d\3\2\2\2]\u011f\3\2\2\2")
        buf.write("_\u0121\3\2\2\2a\u0123\3\2\2\2c\u0131\3\2\2\2ef\7.\2\2")
        buf.write("f\4\3\2\2\2gh\7<\2\2h\6\3\2\2\2ij\7]\2\2j\b\3\2\2\2kl")
        buf.write("\7_\2\2l\n\3\2\2\2mn\7*\2\2n\f\3\2\2\2op\7+\2\2p\16\3")
        buf.write("\2\2\2qr\7?\2\2r\20\3\2\2\2st\t\2\2\2t\22\3\2\2\2uv\7")
        buf.write("$\2\2v\24\3\2\2\2wz\5\21\t\2xz\5\23\n\2yw\3\2\2\2yx\3")
        buf.write("\2\2\2z\26\3\2\2\2{|\7k\2\2|}\7h\2\2}\30\3\2\2\2~\177")
        buf.write("\7g\2\2\177\u0080\7n\2\2\u0080\u0081\7u\2\2\u0081\u0082")
        buf.write("\7g\2\2\u0082\32\3\2\2\2\u0083\u0084\7g\2\2\u0084\u0085")
        buf.write("\7n\2\2\u0085\u0086\7k\2\2\u0086\u0087\7h\2\2\u0087\34")
        buf.write("\3\2\2\2\u0088\u0089\7y\2\2\u0089\u008a\7j\2\2\u008a\u008b")
        buf.write("\7k\2\2\u008b\u008c\7n\2\2\u008c\u008d\7g\2\2\u008d\36")
        buf.write("\3\2\2\2\u008e\u008f\7e\2\2\u008f\u0090\7q\2\2\u0090\u0091")
        buf.write("\7p\2\2\u0091\u0092\7u\2\2\u0092\u0093\7v\2\2\u0093 \3")
        buf.write("\2\2\2\u0094\u0095\7h\2\2\u0095\u0096\7q\2\2\u0096\u0097")
        buf.write("\7t\2\2\u0097\"\3\2\2\2\u0098\u0099\7t\2\2\u0099\u009a")
        buf.write("\7g\2\2\u009a\u009b\7v\2\2\u009b\u009c\7w\2\2\u009c\u009d")
        buf.write("\7t\2\2\u009d\u009e\7p\2\2\u009e$\3\2\2\2\u009f\u00a0")
        buf.write("\7r\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3")
        buf.write("\7p\2\2\u00a3\u00a4\7v\2\2\u00a4&\3\2\2\2\u00a5\u00a6")
        buf.write("\7n\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7p\2\2\u00a8(\3")
        buf.write("\2\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab\7p\2\2\u00ab*\3")
        buf.write("\2\2\2\u00ac\u00ad\7f\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af")
        buf.write("\7h\2\2\u00af,\3\2\2\2\u00b0\u00b1\7-\2\2\u00b1.\3\2\2")
        buf.write("\2\u00b2\u00b3\7/\2\2\u00b3\60\3\2\2\2\u00b4\u00b5\7,")
        buf.write("\2\2\u00b5\62\3\2\2\2\u00b6\u00b7\7\61\2\2\u00b7\64\3")
        buf.write("\2\2\2\u00b8\u00b9\7\61\2\2\u00b9\u00ba\7\61\2\2\u00ba")
        buf.write("\66\3\2\2\2\u00bb\u00bc\7@\2\2\u00bc8\3\2\2\2\u00bd\u00be")
        buf.write("\7>\2\2\u00be:\3\2\2\2\u00bf\u00c0\7>\2\2\u00c0\u00c1")
        buf.write("\7?\2\2\u00c1<\3\2\2\2\u00c2\u00c3\7@\2\2\u00c3\u00c4")
        buf.write("\7?\2\2\u00c4>\3\2\2\2\u00c5\u00c6\7?\2\2\u00c6\u00c7")
        buf.write("\7?\2\2\u00c7@\3\2\2\2\u00c8\u00c9\7#\2\2\u00c9\u00ca")
        buf.write("\7?\2\2\u00caB\3\2\2\2\u00cb\u00cc\7^\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cdD\3\2\2\2\u00ce\u00cf\7^\2\2\u00cf\u00d0")
        buf.write("\7v\2\2\u00d0F\3\2\2\2\u00d1\u00d4\5C\"\2\u00d2\u00d4")
        buf.write("\5E#\2\u00d3\u00d1\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4H")
        buf.write("\3\2\2\2\u00d5\u00d6\5Q)\2\u00d6\u00d7\7\60\2\2\u00d7")
        buf.write("\u00d8\5Q)\2\u00d8J\3\2\2\2\u00d9\u00da\7V\2\2\u00da\u00db")
        buf.write("\7t\2\2\u00db\u00dc\7w\2\2\u00dc\u00e3\7g\2\2\u00dd\u00de")
        buf.write("\7H\2\2\u00de\u00df\7c\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1")
        buf.write("\7u\2\2\u00e1\u00e3\7g\2\2\u00e2\u00d9\3\2\2\2\u00e2\u00dd")
        buf.write("\3\2\2\2\u00e3L\3\2\2\2\u00e4\u00e9\5\21\t\2\u00e5\u00ea")
        buf.write("\5]/\2\u00e6\u00ea\5[.\2\u00e7\u00ea\5_\60\2\u00e8\u00ea")
        buf.write("\5G$\2\u00e9\u00e5\3\2\2\2\u00e9\u00e6\3\2\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb")
        buf.write("\u00ec\5\21\t\2\u00ecN\3\2\2\2\u00ed\u00f4\5\25\13\2\u00ee")
        buf.write("\u00f3\5]/\2\u00ef\u00f3\5[.\2\u00f0\u00f3\5_\60\2\u00f1")
        buf.write("\u00f3\5G$\2\u00f2\u00ee\3\2\2\2\u00f2\u00ef\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3\u00f6\3\2\2\2")
        buf.write("\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7\3")
        buf.write("\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f8\5\25\13\2\u00f8")
        buf.write("P\3\2\2\2\u00f9\u00fd\5[.\2\u00fa\u00fc\5[.\2\u00fb\u00fa")
        buf.write("\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd")
        buf.write("\u00fe\3\2\2\2\u00feR\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100")
        buf.write("\u0106\5]/\2\u0101\u0105\5]/\2\u0102\u0105\5[.\2\u0103")
        buf.write("\u0105\7a\2\2\u0104\u0101\3\2\2\2\u0104\u0102\3\2\2\2")
        buf.write("\u0104\u0103\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3")
        buf.write("\2\2\2\u0106\u0107\3\2\2\2\u0107T\3\2\2\2\u0108\u0106")
        buf.write("\3\2\2\2\u0109\u010b\7\17\2\2\u010a\u0109\3\2\2\2\u010a")
        buf.write("\u010b\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u0110\7\f\2\2")
        buf.write("\u010d\u010f\t\3\2\2\u010e\u010d\3\2\2\2\u010f\u0112\3")
        buf.write("\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111V")
        buf.write("\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0114\t\4\2\2\u0114")
        buf.write("\u0115\3\2\2\2\u0115\u0116\b,\2\2\u0116X\3\2\2\2\u0117")
        buf.write("\u011a\5a\61\2\u0118\u011a\5c\62\2\u0119\u0117\3\2\2\2")
        buf.write("\u0119\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c\b")
        buf.write("-\2\2\u011cZ\3\2\2\2\u011d\u011e\t\5\2\2\u011e\\\3\2\2")
        buf.write("\2\u011f\u0120\t\6\2\2\u0120^\3\2\2\2\u0121\u0122\t\7")
        buf.write("\2\2\u0122`\3\2\2\2\u0123\u0124\7$\2\2\u0124\u0125\7$")
        buf.write("\2\2\u0125\u0126\7$\2\2\u0126\u012a\3\2\2\2\u0127\u0129")
        buf.write("\13\2\2\2\u0128\u0127\3\2\2\2\u0129\u012c\3\2\2\2\u012a")
        buf.write("\u012b\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u012d\3\2\2\2")
        buf.write("\u012c\u012a\3\2\2\2\u012d\u012e\7$\2\2\u012e\u012f\7")
        buf.write("$\2\2\u012f\u0130\7$\2\2\u0130b\3\2\2\2\u0131\u0135\7")
        buf.write("%\2\2\u0132\u0134\n\b\2\2\u0133\u0132\3\2\2\2\u0134\u0137")
        buf.write("\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write("d\3\2\2\2\u0137\u0135\3\2\2\2\21\2y\u00d3\u00e2\u00e9")
        buf.write("\u00f2\u00f4\u00fd\u0104\u0106\u010a\u0110\u0119\u012a")
        buf.write("\u0135\3\b\2\2")
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
    MUL = 24
    DIV = 25
    INTDIV = 26
    GT = 27
    LT = 28
    LET = 29
    GET = 30
    EQUAL = 31
    NOTEQUAL = 32
    BSN = 33
    BST = 34
    ES = 35
    FLOAT = 36
    BOOL = 37
    CHAR = 38
    STRING = 39
    NUM = 40
    ID = 41
    NEWLINE = 42
    WS = 43
    SKIPP = 44

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "':'", "'['", "']'", "'('", "')'", "'='", "'\"'", "'if'", 
            "'else'", "'elif'", "'while'", "'const'", "'for'", "'return'", 
            "'print'", "'len'", "'in'", "'def'", "'+'", "'-'", "'*'", "'/'", 
            "'//'", "'>'", "'<'", "'<='", "'>='", "'=='", "'!='", "'\\n'", 
            "'\\t'" ]

    symbolicNames = [ "<INVALID>",
            "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", "LEFTP", "RIGHTP", 
            "ASSIGN", "SQUOTES", "DQUOTES", "QUOTES", "IF", "ELSE", "ELIF", 
            "WHILE", "CONST", "FOR", "RETURN", "PRINT", "LEN", "IN", "DEF", 
            "ADD", "SUB", "MUL", "DIV", "INTDIV", "GT", "LT", "LET", "GET", 
            "EQUAL", "NOTEQUAL", "BSN", "BST", "ES", "FLOAT", "BOOL", "CHAR", 
            "STRING", "NUM", "ID", "NEWLINE", "WS", "SKIPP" ]

    ruleNames = [ "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", "LEFTP", 
                  "RIGHTP", "ASSIGN", "SQUOTES", "DQUOTES", "QUOTES", "IF", 
                  "ELSE", "ELIF", "WHILE", "CONST", "FOR", "RETURN", "PRINT", 
                  "LEN", "IN", "DEF", "ADD", "SUB", "MUL", "DIV", "INTDIV", 
                  "GT", "LT", "LET", "GET", "EQUAL", "NOTEQUAL", "BSN", 
                  "BST", "ES", "FLOAT", "BOOL", "CHAR", "STRING", "NUM", 
                  "ID", "NEWLINE", "WS", "SKIPP", "DIGIT", "LETTER", "SYMBOLS", 
                  "COMMENT", "LINECOMMENT" ]

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


