# Generated from D:/Sebas/TEC/2022/1 Semestre/Compiladores e Interpretes/MiniPy/miniPython\miParser.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\'")
        buf.write("\u010a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \6 \u00bb\n \r \16 \u00bc\3 \3 \3!\3!\3!\3")
        buf.write("!\7!\u00c5\n!\f!\16!\u00c8\13!\3!\3!\3\"\3\"\7\"\u00ce")
        buf.write("\n\"\f\"\16\"\u00d1\13\"\3#\3#\3#\3#\7#\u00d7\n#\f#\16")
        buf.write("#\u00da\13#\3$\5$\u00dd\n$\3$\3$\7$\u00e1\n$\f$\16$\u00e4")
        buf.write("\13$\3%\3%\3%\3%\3&\3&\5&\u00ec\n&\3&\3&\3\'\3\'\3(\3")
        buf.write("(\3)\3)\3*\3*\3*\3*\3*\7*\u00fb\n*\f*\16*\u00fe\13*\3")
        buf.write("*\3*\3*\3*\3+\3+\7+\u0106\n+\f+\16+\u0109\13+\3\u00fc")
        buf.write("\2,\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M\2O\2Q\2S\2U\2\3\2\b\4\2\13\13\"\"\6\2\13\f\17\17\"\"")
        buf.write("--\3\2\62;\4\2C\\c|\6\2\"\"./<=aa\4\2\f\f\17\17\2\u0111")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\3W\3\2\2\2\5Y\3\2\2\2\7[\3\2\2\2\t]\3\2\2")
        buf.write("\2\13_\3\2\2\2\ra\3\2\2\2\17c\3\2\2\2\21e\3\2\2\2\23g")
        buf.write("\3\2\2\2\25j\3\2\2\2\27o\3\2\2\2\31t\3\2\2\2\33z\3\2\2")
        buf.write("\2\35\u0080\3\2\2\2\37\u0084\3\2\2\2!\u008b\3\2\2\2#\u0091")
        buf.write("\3\2\2\2%\u0095\3\2\2\2\'\u0098\3\2\2\2)\u009c\3\2\2\2")
        buf.write("+\u009e\3\2\2\2-\u00a0\3\2\2\2/\u00a2\3\2\2\2\61\u00a4")
        buf.write("\3\2\2\2\63\u00a7\3\2\2\2\65\u00a9\3\2\2\2\67\u00ab\3")
        buf.write("\2\2\29\u00ae\3\2\2\2;\u00b1\3\2\2\2=\u00b4\3\2\2\2?\u00b8")
        buf.write("\3\2\2\2A\u00c0\3\2\2\2C\u00cb\3\2\2\2E\u00d2\3\2\2\2")
        buf.write("G\u00dc\3\2\2\2I\u00e5\3\2\2\2K\u00eb\3\2\2\2M\u00ef\3")
        buf.write("\2\2\2O\u00f1\3\2\2\2Q\u00f3\3\2\2\2S\u00f5\3\2\2\2U\u0103")
        buf.write("\3\2\2\2WX\7.\2\2X\4\3\2\2\2YZ\7<\2\2Z\6\3\2\2\2[\\\7")
        buf.write("]\2\2\\\b\3\2\2\2]^\7_\2\2^\n\3\2\2\2_`\7*\2\2`\f\3\2")
        buf.write("\2\2ab\7+\2\2b\16\3\2\2\2cd\7?\2\2d\20\3\2\2\2ef\7$\2")
        buf.write("\2f\22\3\2\2\2gh\7k\2\2hi\7h\2\2i\24\3\2\2\2jk\7g\2\2")
        buf.write("kl\7n\2\2lm\7u\2\2mn\7g\2\2n\26\3\2\2\2op\7g\2\2pq\7n")
        buf.write("\2\2qr\7k\2\2rs\7h\2\2s\30\3\2\2\2tu\7y\2\2uv\7j\2\2v")
        buf.write("w\7k\2\2wx\7n\2\2xy\7g\2\2y\32\3\2\2\2z{\7e\2\2{|\7q\2")
        buf.write("\2|}\7p\2\2}~\7u\2\2~\177\7v\2\2\177\34\3\2\2\2\u0080")
        buf.write("\u0081\7h\2\2\u0081\u0082\7q\2\2\u0082\u0083\7t\2\2\u0083")
        buf.write("\36\3\2\2\2\u0084\u0085\7t\2\2\u0085\u0086\7g\2\2\u0086")
        buf.write("\u0087\7v\2\2\u0087\u0088\7w\2\2\u0088\u0089\7t\2\2\u0089")
        buf.write("\u008a\7p\2\2\u008a \3\2\2\2\u008b\u008c\7r\2\2\u008c")
        buf.write("\u008d\7t\2\2\u008d\u008e\7k\2\2\u008e\u008f\7p\2\2\u008f")
        buf.write("\u0090\7v\2\2\u0090\"\3\2\2\2\u0091\u0092\7n\2\2\u0092")
        buf.write("\u0093\7g\2\2\u0093\u0094\7p\2\2\u0094$\3\2\2\2\u0095")
        buf.write("\u0096\7k\2\2\u0096\u0097\7p\2\2\u0097&\3\2\2\2\u0098")
        buf.write("\u0099\7f\2\2\u0099\u009a\7g\2\2\u009a\u009b\7h\2\2\u009b")
        buf.write("(\3\2\2\2\u009c\u009d\7-\2\2\u009d*\3\2\2\2\u009e\u009f")
        buf.write("\7/\2\2\u009f,\3\2\2\2\u00a0\u00a1\7,\2\2\u00a1.\3\2\2")
        buf.write("\2\u00a2\u00a3\7\61\2\2\u00a3\60\3\2\2\2\u00a4\u00a5\7")
        buf.write("\61\2\2\u00a5\u00a6\7\61\2\2\u00a6\62\3\2\2\2\u00a7\u00a8")
        buf.write("\7@\2\2\u00a8\64\3\2\2\2\u00a9\u00aa\7>\2\2\u00aa\66\3")
        buf.write("\2\2\2\u00ab\u00ac\7>\2\2\u00ac\u00ad\7?\2\2\u00ad8\3")
        buf.write("\2\2\2\u00ae\u00af\7@\2\2\u00af\u00b0\7?\2\2\u00b0:\3")
        buf.write("\2\2\2\u00b1\u00b2\7?\2\2\u00b2\u00b3\7?\2\2\u00b3<\3")
        buf.write("\2\2\2\u00b4\u00b5\5C\"\2\u00b5\u00b6\7\60\2\2\u00b6\u00b7")
        buf.write("\5C\"\2\u00b7>\3\2\2\2\u00b8\u00ba\5\21\t\2\u00b9\u00bb")
        buf.write("\5O(\2\u00ba\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00bf\5\21\t\2\u00bf@\3\2\2\2\u00c0\u00c6\5\21\t\2\u00c1")
        buf.write("\u00c5\5O(\2\u00c2\u00c5\5M\'\2\u00c3\u00c5\5Q)\2\u00c4")
        buf.write("\u00c1\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3\3\2\2\2")
        buf.write("\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3")
        buf.write("\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca")
        buf.write("\5\21\t\2\u00caB\3\2\2\2\u00cb\u00cf\5M\'\2\u00cc\u00ce")
        buf.write("\5M\'\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf")
        buf.write("\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0D\3\2\2\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d2\u00d8\5O(\2\u00d3\u00d7\5O(\2\u00d4")
        buf.write("\u00d7\5M\'\2\u00d5\u00d7\7a\2\2\u00d6\u00d3\3\2\2\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00da\3\2\2\2")
        buf.write("\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9F\3\2\2")
        buf.write("\2\u00da\u00d8\3\2\2\2\u00db\u00dd\7\17\2\2\u00dc\u00db")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("\u00e2\7\f\2\2\u00df\u00e1\t\2\2\2\u00e0\u00df\3\2\2\2")
        buf.write("\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3")
        buf.write("\2\2\2\u00e3H\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e6")
        buf.write("\t\3\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\b%\2\2\u00e8")
        buf.write("J\3\2\2\2\u00e9\u00ec\5S*\2\u00ea\u00ec\5U+\2\u00eb\u00e9")
        buf.write("\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed")
        buf.write("\u00ee\b&\2\2\u00eeL\3\2\2\2\u00ef\u00f0\t\4\2\2\u00f0")
        buf.write("N\3\2\2\2\u00f1\u00f2\t\5\2\2\u00f2P\3\2\2\2\u00f3\u00f4")
        buf.write("\t\6\2\2\u00f4R\3\2\2\2\u00f5\u00f6\7$\2\2\u00f6\u00f7")
        buf.write("\7$\2\2\u00f7\u00f8\7$\2\2\u00f8\u00fc\3\2\2\2\u00f9\u00fb")
        buf.write("\13\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write("\u00fd\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00ff\3\2\2\2")
        buf.write("\u00fe\u00fc\3\2\2\2\u00ff\u0100\7$\2\2\u0100\u0101\7")
        buf.write("$\2\2\u0101\u0102\7$\2\2\u0102T\3\2\2\2\u0103\u0107\7")
        buf.write("%\2\2\u0104\u0106\n\7\2\2\u0105\u0104\3\2\2\2\u0106\u0109")
        buf.write("\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108")
        buf.write("V\3\2\2\2\u0109\u0107\3\2\2\2\16\2\u00bc\u00c4\u00c6\u00cf")
        buf.write("\u00d6\u00d8\u00dc\u00e2\u00eb\u00fc\u0107\3\b\2\2")
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
    DQUOTES = 8
    IF = 9
    ELSE = 10
    ELIF = 11
    WHILE = 12
    CONST = 13
    FOR = 14
    RETURN = 15
    PRINT = 16
    LEN = 17
    IN = 18
    DEF = 19
    ADD = 20
    SUB = 21
    MUL = 22
    DIV = 23
    INTDIV = 24
    GT = 25
    LT = 26
    LET = 27
    GET = 28
    EQUAL = 29
    FLOAT = 30
    CHAR = 31
    STRING = 32
    NUM = 33
    ID = 34
    NEWLINE = 35
    WS = 36
    SKIPP = 37

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "':'", "'['", "']'", "'('", "')'", "'='", "'\"'", "'if'", 
            "'else'", "'elif'", "'while'", "'const'", "'for'", "'return'", 
            "'print'", "'len'", "'in'", "'def'", "'+'", "'-'", "'*'", "'/'", 
            "'//'", "'>'", "'<'", "'<='", "'>='", "'=='" ]

    symbolicNames = [ "<INVALID>",
            "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", "LEFTP", "RIGHTP", 
            "ASSIGN", "DQUOTES", "IF", "ELSE", "ELIF", "WHILE", "CONST", 
            "FOR", "RETURN", "PRINT", "LEN", "IN", "DEF", "ADD", "SUB", 
            "MUL", "DIV", "INTDIV", "GT", "LT", "LET", "GET", "EQUAL", "FLOAT", 
            "CHAR", "STRING", "NUM", "ID", "NEWLINE", "WS", "SKIPP" ]

    ruleNames = [ "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", "LEFTP", 
                  "RIGHTP", "ASSIGN", "DQUOTES", "IF", "ELSE", "ELIF", "WHILE", 
                  "CONST", "FOR", "RETURN", "PRINT", "LEN", "IN", "DEF", 
                  "ADD", "SUB", "MUL", "DIV", "INTDIV", "GT", "LT", "LET", 
                  "GET", "EQUAL", "FLOAT", "CHAR", "STRING", "NUM", "ID", 
                  "NEWLINE", "WS", "SKIPP", "DIGIT", "LETTER", "SYMBOLS", 
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


