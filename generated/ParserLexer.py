# Generated from D:/Sebas/TEC/2022/1 Semestre/Compiladores e Interpretes/MiniPy/miniPython\Parser.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from ParserParser import ParserParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2(")
        buf.write("\u00ff\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\7\"\u00c7\n\"\f\"\16\"\u00ca\13\"\3#\3#\3#\3")
        buf.write("#\7#\u00d0\n#\f#\16#\u00d3\13#\3$\3$\3%\3%\3&\5&\u00da")
        buf.write("\n&\3&\3&\7&\u00de\n&\f&\16&\u00e1\13&\3\'\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3(\3(\7(\u00ec\n(\f(\16(\u00ef\13(\3(\3(\3(")
        buf.write("\3(\3(\3(\3)\3)\7)\u00f9\n)\f)\16)\u00fc\13)\3)\3)\3\u00ed")
        buf.write("\2*\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G\2I\2")
        buf.write("K%M&O\'Q(\3\2\7\3\2\62;\5\2\"\"C\\c|\4\2\13\13\"\"\6\2")
        buf.write("\13\f\17\17\"\"--\4\2\f\f\17\17\2\u0104\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\3S\3\2\2\2\5W\3\2\2\2\7]\3\2\2\2\tb\3\2\2\2\13")
        buf.write("i\3\2\2\2\rk\3\2\2\2\17m\3\2\2\2\21o\3\2\2\2\23q\3\2\2")
        buf.write("\2\25s\3\2\2\2\27u\3\2\2\2\31w\3\2\2\2\33z\3\2\2\2\35")
        buf.write("\177\3\2\2\2\37\u0084\3\2\2\2!\u008a\3\2\2\2#\u0090\3")
        buf.write("\2\2\2%\u0094\3\2\2\2\'\u009b\3\2\2\2)\u00a1\3\2\2\2+")
        buf.write("\u00a5\3\2\2\2-\u00a8\3\2\2\2/\u00ac\3\2\2\2\61\u00ae")
        buf.write("\3\2\2\2\63\u00b0\3\2\2\2\65\u00b2\3\2\2\2\67\u00b4\3")
        buf.write("\2\2\29\u00b7\3\2\2\2;\u00b9\3\2\2\2=\u00bb\3\2\2\2?\u00be")
        buf.write("\3\2\2\2A\u00c1\3\2\2\2C\u00c4\3\2\2\2E\u00cb\3\2\2\2")
        buf.write("G\u00d4\3\2\2\2I\u00d6\3\2\2\2K\u00d9\3\2\2\2M\u00e2\3")
        buf.write("\2\2\2O\u00e6\3\2\2\2Q\u00f6\3\2\2\2ST\7k\2\2TU\7p\2\2")
        buf.write("UV\7v\2\2V\4\3\2\2\2WX\7h\2\2XY\7n\2\2YZ\7q\2\2Z[\7c\2")
        buf.write("\2[\\\7v\2\2\\\6\3\2\2\2]^\7e\2\2^_\7j\2\2_`\7c\2\2`a")
        buf.write("\7t\2\2a\b\3\2\2\2bc\7U\2\2cd\7v\2\2de\7t\2\2ef\7k\2\2")
        buf.write("fg\7p\2\2gh\7i\2\2h\n\3\2\2\2ij\7.\2\2j\f\3\2\2\2kl\7")
        buf.write("<\2\2l\16\3\2\2\2mn\7]\2\2n\20\3\2\2\2op\7_\2\2p\22\3")
        buf.write("\2\2\2qr\7*\2\2r\24\3\2\2\2st\7+\2\2t\26\3\2\2\2uv\7?")
        buf.write("\2\2v\30\3\2\2\2wx\7k\2\2xy\7h\2\2y\32\3\2\2\2z{\7g\2")
        buf.write("\2{|\7n\2\2|}\7u\2\2}~\7g\2\2~\34\3\2\2\2\177\u0080\7")
        buf.write("g\2\2\u0080\u0081\7n\2\2\u0081\u0082\7k\2\2\u0082\u0083")
        buf.write("\7h\2\2\u0083\36\3\2\2\2\u0084\u0085\7y\2\2\u0085\u0086")
        buf.write("\7j\2\2\u0086\u0087\7k\2\2\u0087\u0088\7n\2\2\u0088\u0089")
        buf.write("\7g\2\2\u0089 \3\2\2\2\u008a\u008b\7e\2\2\u008b\u008c")
        buf.write("\7q\2\2\u008c\u008d\7p\2\2\u008d\u008e\7u\2\2\u008e\u008f")
        buf.write("\7v\2\2\u008f\"\3\2\2\2\u0090\u0091\7h\2\2\u0091\u0092")
        buf.write("\7q\2\2\u0092\u0093\7t\2\2\u0093$\3\2\2\2\u0094\u0095")
        buf.write("\7t\2\2\u0095\u0096\7g\2\2\u0096\u0097\7v\2\2\u0097\u0098")
        buf.write("\7w\2\2\u0098\u0099\7t\2\2\u0099\u009a\7p\2\2\u009a&\3")
        buf.write("\2\2\2\u009b\u009c\7r\2\2\u009c\u009d\7t\2\2\u009d\u009e")
        buf.write("\7k\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7v\2\2\u00a0(\3")
        buf.write("\2\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4")
        buf.write("\7p\2\2\u00a4*\3\2\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7,\3\2\2\2\u00a8\u00a9\7f\2\2\u00a9\u00aa")
        buf.write("\7g\2\2\u00aa\u00ab\7h\2\2\u00ab.\3\2\2\2\u00ac\u00ad")
        buf.write("\7-\2\2\u00ad\60\3\2\2\2\u00ae\u00af\7/\2\2\u00af\62\3")
        buf.write("\2\2\2\u00b0\u00b1\7,\2\2\u00b1\64\3\2\2\2\u00b2\u00b3")
        buf.write("\7\61\2\2\u00b3\66\3\2\2\2\u00b4\u00b5\7\61\2\2\u00b5")
        buf.write("\u00b6\7\61\2\2\u00b68\3\2\2\2\u00b7\u00b8\7@\2\2\u00b8")
        buf.write(":\3\2\2\2\u00b9\u00ba\7>\2\2\u00ba<\3\2\2\2\u00bb\u00bc")
        buf.write("\7>\2\2\u00bc\u00bd\7?\2\2\u00bd>\3\2\2\2\u00be\u00bf")
        buf.write("\7@\2\2\u00bf\u00c0\7?\2\2\u00c0@\3\2\2\2\u00c1\u00c2")
        buf.write("\7?\2\2\u00c2\u00c3\7?\2\2\u00c3B\3\2\2\2\u00c4\u00c8")
        buf.write("\5G$\2\u00c5\u00c7\5G$\2\u00c6\u00c5\3\2\2\2\u00c7\u00ca")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("D\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00d1\5I%\2\u00cc")
        buf.write("\u00d0\5I%\2\u00cd\u00d0\5G$\2\u00ce\u00d0\7a\2\2\u00cf")
        buf.write("\u00cc\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2")
        buf.write("\u00d0\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3")
        buf.write("\2\2\2\u00d2F\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d5")
        buf.write("\t\2\2\2\u00d5H\3\2\2\2\u00d6\u00d7\t\3\2\2\u00d7J\3\2")
        buf.write("\2\2\u00d8\u00da\7\17\2\2\u00d9\u00d8\3\2\2\2\u00d9\u00da")
        buf.write("\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00df\7\f\2\2\u00dc")
        buf.write("\u00de\t\4\2\2\u00dd\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2")
        buf.write("\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0L\3\2\2")
        buf.write("\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\t\5\2\2\u00e3\u00e4")
        buf.write("\3\2\2\2\u00e4\u00e5\b\'\2\2\u00e5N\3\2\2\2\u00e6\u00e7")
        buf.write("\7$\2\2\u00e7\u00e8\7$\2\2\u00e8\u00e9\7$\2\2\u00e9\u00ed")
        buf.write("\3\2\2\2\u00ea\u00ec\13\2\2\2\u00eb\u00ea\3\2\2\2\u00ec")
        buf.write("\u00ef\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ed\u00eb\3\2\2\2")
        buf.write("\u00ee\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f1\7")
        buf.write("$\2\2\u00f1\u00f2\7$\2\2\u00f2\u00f3\7$\2\2\u00f3\u00f4")
        buf.write("\3\2\2\2\u00f4\u00f5\b(\2\2\u00f5P\3\2\2\2\u00f6\u00fa")
        buf.write("\7%\2\2\u00f7\u00f9\n\6\2\2\u00f8\u00f7\3\2\2\2\u00f9")
        buf.write("\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2")
        buf.write("\u00fb\u00fd\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00fe\b")
        buf.write(")\2\2\u00feR\3\2\2\2\n\2\u00c8\u00cf\u00d1\u00d9\u00df")
        buf.write("\u00ed\u00fa\3\b\2\2")
        return buf.getvalue()


class ParserLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER = 1
    FLOAT = 2
    CHARCONST = 3
    STRING = 4
    COMMA = 5
    COLON = 6
    LEFTSQUARE = 7
    RIGHTSQUARE = 8
    LEFTP = 9
    RIGHTP = 10
    ASSIGN = 11
    IF = 12
    ELSE = 13
    ELIF = 14
    WHILE = 15
    CONST = 16
    FOR = 17
    RETURN = 18
    PRINT = 19
    LEN = 20
    IN = 21
    DEF = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    INTDIV = 27
    GT = 28
    LT = 29
    LET = 30
    GET = 31
    EQUAL = 32
    NUM = 33
    ID = 34
    NEWLINE = 35
    WS = 36
    COMMENT = 37
    LINECOMMENT = 38

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'char'", "'String'", "','", "':'", "'['", 
            "']'", "'('", "')'", "'='", "'if'", "'else'", "'elif'", "'while'", 
            "'const'", "'for'", "'return'", "'print'", "'len'", "'in'", 
            "'def'", "'+'", "'-'", "'*'", "'/'", "'//'", "'>'", "'<'", "'<='", 
            "'>='", "'=='" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "FLOAT", "CHARCONST", "STRING", "COMMA", "COLON", 
            "LEFTSQUARE", "RIGHTSQUARE", "LEFTP", "RIGHTP", "ASSIGN", "IF", 
            "ELSE", "ELIF", "WHILE", "CONST", "FOR", "RETURN", "PRINT", 
            "LEN", "IN", "DEF", "ADD", "SUB", "MUL", "DIV", "INTDIV", "GT", 
            "LT", "LET", "GET", "EQUAL", "NUM", "ID", "NEWLINE", "WS", "COMMENT", 
            "LINECOMMENT" ]

    ruleNames = [ "INTEGER", "FLOAT", "CHARCONST", "STRING", "COMMA", "COLON", 
                  "LEFTSQUARE", "RIGHTSQUARE", "LEFTP", "RIGHTP", "ASSIGN", 
                  "IF", "ELSE", "ELIF", "WHILE", "CONST", "FOR", "RETURN", 
                  "PRINT", "LEN", "IN", "DEF", "ADD", "SUB", "MUL", "DIV", 
                  "INTDIV", "GT", "LT", "LET", "GET", "EQUAL", "NUM", "ID", 
                  "DIGIT", "LETTER", "NEWLINE", "WS", "COMMENT", "LINECOMMENT" ]

    grammarFileName = "Parser.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class Denter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: ParserLexer = lexer

        def pull_token(self):
            return super(ParserLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.Denter(self, self.NEWLINE, ParserParser.INDENT, ParserParser.DEDENT, False)
        return self.denter.next_token()


