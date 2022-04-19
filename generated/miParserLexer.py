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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,")
        buf.write("\u0126\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\5\13")
        buf.write("v\n\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\5#\u00cd\n#\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3%\5%\u00d8\n%\3%\3%\3&\3&\3&\3&\3&\7&\u00e1\n&\f")
        buf.write("&\16&\u00e4\13&\3&\3&\3\'\3\'\7\'\u00ea\n\'\f\'\16\'\u00ed")
        buf.write("\13\'\3(\3(\3(\3(\7(\u00f3\n(\f(\16(\u00f6\13(\3)\5)\u00f9")
        buf.write("\n)\3)\3)\7)\u00fd\n)\f)\16)\u0100\13)\3*\3*\3*\3*\3+")
        buf.write("\3+\5+\u0108\n+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3/\3")
        buf.write("/\7/\u0117\n/\f/\16/\u011a\13/\3/\3/\3/\3/\3\60\3\60\7")
        buf.write("\60\u0122\n\60\f\60\16\60\u0125\13\60\3\u0118\2\61\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W\2Y\2[\2]\2_\2\3\2\t\3\2))\4\2\13\13\"\"\6\2\13\f")
        buf.write("\17\17\"\"--\3\2\62;\4\2C\\c|\7\2\"\"&\'./<=aa\4\2\f\f")
        buf.write("\17\17\2\u0132\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\3a\3\2\2\2\5c\3\2\2\2\7e\3")
        buf.write("\2\2\2\tg\3\2\2\2\13i\3\2\2\2\rk\3\2\2\2\17m\3\2\2\2\21")
        buf.write("o\3\2\2\2\23q\3\2\2\2\25u\3\2\2\2\27w\3\2\2\2\31z\3\2")
        buf.write("\2\2\33\177\3\2\2\2\35\u0084\3\2\2\2\37\u008a\3\2\2\2")
        buf.write("!\u0090\3\2\2\2#\u0094\3\2\2\2%\u009b\3\2\2\2\'\u00a1")
        buf.write("\3\2\2\2)\u00a5\3\2\2\2+\u00a8\3\2\2\2-\u00ac\3\2\2\2")
        buf.write("/\u00ae\3\2\2\2\61\u00b0\3\2\2\2\63\u00b2\3\2\2\2\65\u00b4")
        buf.write("\3\2\2\2\67\u00b7\3\2\2\29\u00b9\3\2\2\2;\u00bb\3\2\2")
        buf.write("\2=\u00be\3\2\2\2?\u00c1\3\2\2\2A\u00c4\3\2\2\2C\u00c7")
        buf.write("\3\2\2\2E\u00cc\3\2\2\2G\u00ce\3\2\2\2I\u00d2\3\2\2\2")
        buf.write("K\u00db\3\2\2\2M\u00e7\3\2\2\2O\u00ee\3\2\2\2Q\u00f8\3")
        buf.write("\2\2\2S\u0101\3\2\2\2U\u0107\3\2\2\2W\u010b\3\2\2\2Y\u010d")
        buf.write("\3\2\2\2[\u010f\3\2\2\2]\u0111\3\2\2\2_\u011f\3\2\2\2")
        buf.write("ab\7.\2\2b\4\3\2\2\2cd\7<\2\2d\6\3\2\2\2ef\7]\2\2f\b\3")
        buf.write("\2\2\2gh\7_\2\2h\n\3\2\2\2ij\7*\2\2j\f\3\2\2\2kl\7+\2")
        buf.write("\2l\16\3\2\2\2mn\7?\2\2n\20\3\2\2\2op\t\2\2\2p\22\3\2")
        buf.write("\2\2qr\7$\2\2r\24\3\2\2\2sv\5\21\t\2tv\5\23\n\2us\3\2")
        buf.write("\2\2ut\3\2\2\2v\26\3\2\2\2wx\7k\2\2xy\7h\2\2y\30\3\2\2")
        buf.write("\2z{\7g\2\2{|\7n\2\2|}\7u\2\2}~\7g\2\2~\32\3\2\2\2\177")
        buf.write("\u0080\7g\2\2\u0080\u0081\7n\2\2\u0081\u0082\7k\2\2\u0082")
        buf.write("\u0083\7h\2\2\u0083\34\3\2\2\2\u0084\u0085\7y\2\2\u0085")
        buf.write("\u0086\7j\2\2\u0086\u0087\7k\2\2\u0087\u0088\7n\2\2\u0088")
        buf.write("\u0089\7g\2\2\u0089\36\3\2\2\2\u008a\u008b\7e\2\2\u008b")
        buf.write("\u008c\7q\2\2\u008c\u008d\7p\2\2\u008d\u008e\7u\2\2\u008e")
        buf.write("\u008f\7v\2\2\u008f \3\2\2\2\u0090\u0091\7h\2\2\u0091")
        buf.write("\u0092\7q\2\2\u0092\u0093\7t\2\2\u0093\"\3\2\2\2\u0094")
        buf.write("\u0095\7t\2\2\u0095\u0096\7g\2\2\u0096\u0097\7v\2\2\u0097")
        buf.write("\u0098\7w\2\2\u0098\u0099\7t\2\2\u0099\u009a\7p\2\2\u009a")
        buf.write("$\3\2\2\2\u009b\u009c\7r\2\2\u009c\u009d\7t\2\2\u009d")
        buf.write("\u009e\7k\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7v\2\2\u00a0")
        buf.write("&\3\2\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3\7g\2\2\u00a3")
        buf.write("\u00a4\7p\2\2\u00a4(\3\2\2\2\u00a5\u00a6\7k\2\2\u00a6")
        buf.write("\u00a7\7p\2\2\u00a7*\3\2\2\2\u00a8\u00a9\7f\2\2\u00a9")
        buf.write("\u00aa\7g\2\2\u00aa\u00ab\7h\2\2\u00ab,\3\2\2\2\u00ac")
        buf.write("\u00ad\7-\2\2\u00ad.\3\2\2\2\u00ae\u00af\7/\2\2\u00af")
        buf.write("\60\3\2\2\2\u00b0\u00b1\7,\2\2\u00b1\62\3\2\2\2\u00b2")
        buf.write("\u00b3\7\61\2\2\u00b3\64\3\2\2\2\u00b4\u00b5\7\61\2\2")
        buf.write("\u00b5\u00b6\7\61\2\2\u00b6\66\3\2\2\2\u00b7\u00b8\7@")
        buf.write("\2\2\u00b88\3\2\2\2\u00b9\u00ba\7>\2\2\u00ba:\3\2\2\2")
        buf.write("\u00bb\u00bc\7>\2\2\u00bc\u00bd\7?\2\2\u00bd<\3\2\2\2")
        buf.write("\u00be\u00bf\7@\2\2\u00bf\u00c0\7?\2\2\u00c0>\3\2\2\2")
        buf.write("\u00c1\u00c2\7?\2\2\u00c2\u00c3\7?\2\2\u00c3@\3\2\2\2")
        buf.write("\u00c4\u00c5\7^\2\2\u00c5\u00c6\7p\2\2\u00c6B\3\2\2\2")
        buf.write("\u00c7\u00c8\7^\2\2\u00c8\u00c9\7v\2\2\u00c9D\3\2\2\2")
        buf.write("\u00ca\u00cd\5A!\2\u00cb\u00cd\5C\"\2\u00cc\u00ca\3\2")
        buf.write("\2\2\u00cc\u00cb\3\2\2\2\u00cdF\3\2\2\2\u00ce\u00cf\5")
        buf.write("M\'\2\u00cf\u00d0\7\60\2\2\u00d0\u00d1\5M\'\2\u00d1H\3")
        buf.write("\2\2\2\u00d2\u00d7\5\21\t\2\u00d3\u00d8\5Y-\2\u00d4\u00d8")
        buf.write("\5W,\2\u00d5\u00d8\5[.\2\u00d6\u00d8\5E#\2\u00d7\u00d3")
        buf.write("\3\2\2\2\u00d7\u00d4\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7")
        buf.write("\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\5\21\t")
        buf.write("\2\u00daJ\3\2\2\2\u00db\u00e2\5\25\13\2\u00dc\u00e1\5")
        buf.write("Y-\2\u00dd\u00e1\5W,\2\u00de\u00e1\5[.\2\u00df\u00e1\5")
        buf.write("E#\2\u00e0\u00dc\3\2\2\2\u00e0\u00dd\3\2\2\2\u00e0\u00de")
        buf.write("\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2")
        buf.write("\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e5\3\2\2\2")
        buf.write("\u00e4\u00e2\3\2\2\2\u00e5\u00e6\5\25\13\2\u00e6L\3\2")
        buf.write("\2\2\u00e7\u00eb\5W,\2\u00e8\u00ea\5W,\2\u00e9\u00e8\3")
        buf.write("\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec")
        buf.write("\3\2\2\2\u00ecN\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00f4")
        buf.write("\5Y-\2\u00ef\u00f3\5Y-\2\u00f0\u00f3\5W,\2\u00f1\u00f3")
        buf.write("\7a\2\2\u00f2\u00ef\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2")
        buf.write("\u00f4\u00f5\3\2\2\2\u00f5P\3\2\2\2\u00f6\u00f4\3\2\2")
        buf.write("\2\u00f7\u00f9\7\17\2\2\u00f8\u00f7\3\2\2\2\u00f8\u00f9")
        buf.write("\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fe\7\f\2\2\u00fb")
        buf.write("\u00fd\t\3\2\2\u00fc\u00fb\3\2\2\2\u00fd\u0100\3\2\2\2")
        buf.write("\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ffR\3\2\2")
        buf.write("\2\u0100\u00fe\3\2\2\2\u0101\u0102\t\4\2\2\u0102\u0103")
        buf.write("\3\2\2\2\u0103\u0104\b*\2\2\u0104T\3\2\2\2\u0105\u0108")
        buf.write("\5]/\2\u0106\u0108\5_\60\2\u0107\u0105\3\2\2\2\u0107\u0106")
        buf.write("\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a\b+\2\2\u010a")
        buf.write("V\3\2\2\2\u010b\u010c\t\5\2\2\u010cX\3\2\2\2\u010d\u010e")
        buf.write("\t\6\2\2\u010eZ\3\2\2\2\u010f\u0110\t\7\2\2\u0110\\\3")
        buf.write("\2\2\2\u0111\u0112\7$\2\2\u0112\u0113\7$\2\2\u0113\u0114")
        buf.write("\7$\2\2\u0114\u0118\3\2\2\2\u0115\u0117\13\2\2\2\u0116")
        buf.write("\u0115\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0119\3\2\2\2")
        buf.write("\u0118\u0116\3\2\2\2\u0119\u011b\3\2\2\2\u011a\u0118\3")
        buf.write("\2\2\2\u011b\u011c\7$\2\2\u011c\u011d\7$\2\2\u011d\u011e")
        buf.write("\7$\2\2\u011e^\3\2\2\2\u011f\u0123\7%\2\2\u0120\u0122")
        buf.write("\n\b\2\2\u0121\u0120\3\2\2\2\u0122\u0125\3\2\2\2\u0123")
        buf.write("\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124`\3\2\2\2\u0125")
        buf.write("\u0123\3\2\2\2\20\2u\u00cc\u00d7\u00e0\u00e2\u00eb\u00f2")
        buf.write("\u00f4\u00f8\u00fe\u0107\u0118\u0123\3\b\2\2")
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
    BSN = 32
    BST = 33
    ES = 34
    FLOAT = 35
    CHAR = 36
    STRING = 37
    NUM = 38
    ID = 39
    NEWLINE = 40
    WS = 41
    SKIPP = 42

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "':'", "'['", "']'", "'('", "')'", "'='", "'\"'", "'if'", 
            "'else'", "'elif'", "'while'", "'const'", "'for'", "'return'", 
            "'print'", "'len'", "'in'", "'def'", "'+'", "'-'", "'*'", "'/'", 
            "'//'", "'>'", "'<'", "'<='", "'>='", "'=='", "'\\n'", "'\\t'" ]

    symbolicNames = [ "<INVALID>",
            "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", "LEFTP", "RIGHTP", 
            "ASSIGN", "SQUOTES", "DQUOTES", "QUOTES", "IF", "ELSE", "ELIF", 
            "WHILE", "CONST", "FOR", "RETURN", "PRINT", "LEN", "IN", "DEF", 
            "ADD", "SUB", "MUL", "DIV", "INTDIV", "GT", "LT", "LET", "GET", 
            "EQUAL", "BSN", "BST", "ES", "FLOAT", "CHAR", "STRING", "NUM", 
            "ID", "NEWLINE", "WS", "SKIPP" ]

    ruleNames = [ "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", "LEFTP", 
                  "RIGHTP", "ASSIGN", "SQUOTES", "DQUOTES", "QUOTES", "IF", 
                  "ELSE", "ELIF", "WHILE", "CONST", "FOR", "RETURN", "PRINT", 
                  "LEN", "IN", "DEF", "ADD", "SUB", "MUL", "DIV", "INTDIV", 
                  "GT", "LT", "LET", "GET", "EQUAL", "BSN", "BST", "ES", 
                  "FLOAT", "CHAR", "STRING", "NUM", "ID", "NEWLINE", "WS", 
                  "SKIPP", "DIGIT", "LETTER", "SYMBOLS", "COMMENT", "LINECOMMENT" ]

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


