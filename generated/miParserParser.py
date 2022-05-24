# Generated from D:/Sebas/TEC/2022/1 Semestre/Compiladores e Interpretes/ProyectoCompiladores/miniPython\miParser.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3/")
        buf.write("\u00e8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\7\2$\n\2\f\2\16")
        buf.write("\2\'\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write("\63\n\3\3\3\3\3\5\3\67\n\3\3\3\3\3\3\3\3\3\3\3\5\3>\n")
        buf.write("\3\3\3\3\3\5\3B\n\3\3\3\3\3\5\3F\n\3\5\3H\n\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3S\n\3\3\3\3\3\5\3W\n\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3^\n\3\3\3\3\3\5\3b\n\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3q\n\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3y\n\3\3\4\5\4|\n\4\3\4\3\4")
        buf.write("\3\4\7\4\u0081\n\4\f\4\16\4\u0084\13\4\5\4\u0086\n\4\3")
        buf.write("\5\3\5\6\5\u008a\n\5\r\5\16\5\u008b\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\7\3\7\7\7\u0095\n\7\f\7\16\7\u0098\13\7\3\b\3\b\3")
        buf.write("\b\3\t\3\t\7\t\u009f\n\t\f\t\16\t\u00a2\13\t\3\n\3\n\3")
        buf.write("\n\3\13\3\13\7\13\u00a9\n\13\f\13\16\13\u00ac\13\13\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\7\r\u00b5\n\r\f\r\16\r\u00b8")
        buf.write("\13\r\3\16\3\16\3\16\7\16\u00bd\n\16\f\16\16\16\u00c0")
        buf.write("\13\16\3\17\5\17\u00c3\n\17\3\17\3\17\5\17\u00c7\n\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00d0\n\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u00de\n\17\3\20\3\20\5\20\u00e2\n\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\2\2\22\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \2\5\3\2\35\"\3\2\30\31\3\2\32\33\2\u0100\2")
        buf.write("%\3\2\2\2\4x\3\2\2\2\6\u0085\3\2\2\2\b\u0087\3\2\2\2\n")
        buf.write("\u008f\3\2\2\2\f\u0096\3\2\2\2\16\u0099\3\2\2\2\20\u00a0")
        buf.write("\3\2\2\2\22\u00a3\3\2\2\2\24\u00aa\3\2\2\2\26\u00ad\3")
        buf.write("\2\2\2\30\u00b6\3\2\2\2\32\u00b9\3\2\2\2\34\u00dd\3\2")
        buf.write("\2\2\36\u00df\3\2\2\2 \u00e5\3\2\2\2\"$\5\4\3\2#\"\3\2")
        buf.write("\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\3\3\2\2\2\'%\3\2")
        buf.write("\2\2()\7\27\2\2)*\7*\2\2*+\7\7\2\2+,\5\6\4\2,-\7\b\2\2")
        buf.write("-.\7\4\2\2./\5\b\5\2/y\3\2\2\2\60\62\7\r\2\2\61\63\7\7")
        buf.write("\2\2\62\61\3\2\2\2\62\63\3\2\2\2\63\64\3\2\2\2\64\66\5")
        buf.write("\n\6\2\65\67\7\b\2\2\66\65\3\2\2\2\66\67\3\2\2\2\678\3")
        buf.write("\2\2\289\7\4\2\29=\5\b\5\2:;\7\16\2\2;<\7\4\2\2<>\5\b")
        buf.write("\5\2=:\3\2\2\2=>\3\2\2\2>y\3\2\2\2?G\7\23\2\2@B\7\7\2")
        buf.write("\2A@\3\2\2\2AB\3\2\2\2BC\3\2\2\2CE\5\n\6\2DF\7\b\2\2E")
        buf.write("D\3\2\2\2EF\3\2\2\2FH\3\2\2\2GA\3\2\2\2GH\3\2\2\2HI\3")
        buf.write("\2\2\2Iy\7+\2\2JK\7\24\2\2KL\7\7\2\2LM\5\n\6\2MN\7\b\2")
        buf.write("\2NO\7+\2\2Oy\3\2\2\2PR\7\20\2\2QS\7\7\2\2RQ\3\2\2\2R")
        buf.write("S\3\2\2\2ST\3\2\2\2TV\5\n\6\2UW\7\b\2\2VU\3\2\2\2VW\3")
        buf.write("\2\2\2WX\3\2\2\2XY\7\4\2\2YZ\5\b\5\2Zy\3\2\2\2[]\7\22")
        buf.write("\2\2\\^\7\7\2\2]\\\3\2\2\2]^\3\2\2\2^_\3\2\2\2_a\5\n\6")
        buf.write("\2`b\7\b\2\2a`\3\2\2\2ab\3\2\2\2bc\3\2\2\2cd\7\26\2\2")
        buf.write("de\5\32\16\2ef\7\4\2\2fg\5\b\5\2gy\3\2\2\2hi\7*\2\2ij")
        buf.write("\7\t\2\2jk\5\n\6\2kl\7+\2\2ly\3\2\2\2mn\5\34\17\2np\7")
        buf.write("\7\2\2oq\5\32\16\2po\3\2\2\2pq\3\2\2\2qr\3\2\2\2rs\7\b")
        buf.write("\2\2st\7+\2\2ty\3\2\2\2uv\5\32\16\2vw\7+\2\2wy\3\2\2\2")
        buf.write("x(\3\2\2\2x\60\3\2\2\2x?\3\2\2\2xJ\3\2\2\2xP\3\2\2\2x")
        buf.write("[\3\2\2\2xh\3\2\2\2xm\3\2\2\2xu\3\2\2\2y\5\3\2\2\2z|\7")
        buf.write("*\2\2{z\3\2\2\2{|\3\2\2\2|\u0086\3\2\2\2}\u0082\7*\2\2")
        buf.write("~\177\7\3\2\2\177\u0081\7*\2\2\u0080~\3\2\2\2\u0081\u0084")
        buf.write("\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0085{\3\2\2\2\u0085")
        buf.write("}\3\2\2\2\u0086\7\3\2\2\2\u0087\u0089\7.\2\2\u0088\u008a")
        buf.write("\5\4\3\2\u0089\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b")
        buf.write("\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\3\2\2\2")
        buf.write("\u008d\u008e\7/\2\2\u008e\t\3\2\2\2\u008f\u0090\5\16\b")
        buf.write("\2\u0090\u0091\5\f\7\2\u0091\13\3\2\2\2\u0092\u0093\t")
        buf.write("\2\2\2\u0093\u0095\5\16\b\2\u0094\u0092\3\2\2\2\u0095")
        buf.write("\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\r\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009a\5\22")
        buf.write("\n\2\u009a\u009b\5\20\t\2\u009b\17\3\2\2\2\u009c\u009d")
        buf.write("\t\3\2\2\u009d\u009f\5\26\f\2\u009e\u009c\3\2\2\2\u009f")
        buf.write("\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2")
        buf.write("\u00a1\21\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4\5\26")
        buf.write("\f\2\u00a4\u00a5\5\24\13\2\u00a5\23\3\2\2\2\u00a6\u00a7")
        buf.write("\t\4\2\2\u00a7\u00a9\5\26\f\2\u00a8\u00a6\3\2\2\2\u00a9")
        buf.write("\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\25\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae\5\34")
        buf.write("\17\2\u00ae\u00af\5\30\r\2\u00af\27\3\2\2\2\u00b0\u00b1")
        buf.write("\7\5\2\2\u00b1\u00b2\5\n\6\2\u00b2\u00b3\7\6\2\2\u00b3")
        buf.write("\u00b5\3\2\2\2\u00b4\u00b0\3\2\2\2\u00b5\u00b8\3\2\2\2")
        buf.write("\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\31\3\2")
        buf.write("\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00be\5\n\6\2\u00ba\u00bb")
        buf.write("\7\3\2\2\u00bb\u00bd\5\n\6\2\u00bc\u00ba\3\2\2\2\u00bd")
        buf.write("\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2")
        buf.write("\u00bf\33\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c3\7\31")
        buf.write("\2\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\u00de\7)\2\2\u00c5\u00c7\7\31\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\u00de\7&\2\2\u00c9\u00de\7\'\2\2\u00ca\u00de\7")
        buf.write("(\2\2\u00cb\u00de\5 \21\2\u00cc\u00cd\5 \21\2\u00cd\u00cf")
        buf.write("\7\7\2\2\u00ce\u00d0\5\32\16\2\u00cf\u00ce\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\7\b\2\2")
        buf.write("\u00d2\u00de\3\2\2\2\u00d3\u00d4\7\7\2\2\u00d4\u00d5\5")
        buf.write("\32\16\2\u00d5\u00d6\7\b\2\2\u00d6\u00de\3\2\2\2\u00d7")
        buf.write("\u00de\5\36\20\2\u00d8\u00d9\7\25\2\2\u00d9\u00da\7\7")
        buf.write("\2\2\u00da\u00db\5\n\6\2\u00db\u00dc\7\b\2\2\u00dc\u00de")
        buf.write("\3\2\2\2\u00dd\u00c2\3\2\2\2\u00dd\u00c6\3\2\2\2\u00dd")
        buf.write("\u00c9\3\2\2\2\u00dd\u00ca\3\2\2\2\u00dd\u00cb\3\2\2\2")
        buf.write("\u00dd\u00cc\3\2\2\2\u00dd\u00d3\3\2\2\2\u00dd\u00d7\3")
        buf.write("\2\2\2\u00dd\u00d8\3\2\2\2\u00de\35\3\2\2\2\u00df\u00e1")
        buf.write("\7\5\2\2\u00e0\u00e2\5\32\16\2\u00e1\u00e0\3\2\2\2\u00e1")
        buf.write("\u00e2\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\7\6\2\2")
        buf.write("\u00e4\37\3\2\2\2\u00e5\u00e6\7*\2\2\u00e6!\3\2\2\2\35")
        buf.write("%\62\66=AEGRV]apx{\u0082\u0085\u008b\u0096\u00a0\u00aa")
        buf.write("\u00b6\u00be\u00c2\u00c6\u00cf\u00dd\u00e1")
        return buf.getvalue()


class miParserParser ( Parser ):

    grammarFileName = "miParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "':'", "'['", "']'", "'('", "')'", 
                     "'='", "<INVALID>", "'\"'", "<INVALID>", "'if'", "'else'", 
                     "'elif'", "'while'", "'const'", "'for'", "'return'", 
                     "'print'", "'len'", "'in'", "'def'", "'+'", "'-'", 
                     "'*'", "'/'", "'//'", "'>'", "'<'", "'<='", "'>='", 
                     "'=='", "'!='", "'\\n'", "'\\t'" ]

    symbolicNames = [ "<INVALID>", "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", 
                      "LEFTP", "RIGHTP", "ASSIGN", "SQUOTES", "DQUOTES", 
                      "QUOTES", "IF", "ELSE", "ELIF", "WHILE", "CONST", 
                      "FOR", "RETURN", "PRINT", "LEN", "IN", "DEF", "ADD", 
                      "SUB", "MUL", "DIV", "INTDIV", "GT", "LT", "LET", 
                      "GET", "EQUAL", "NOTEQUAL", "BSN", "BST", "ES", "FLOAT", 
                      "CHAR", "STRING", "NUM", "ID", "NEWLINE", "WS", "SKIPP", 
                      "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_argList = 2
    RULE_sequence = 3
    RULE_expression = 4
    RULE_comparison = 5
    RULE_additionExpression = 6
    RULE_additionFactor = 7
    RULE_multiplicationExpression = 8
    RULE_multiplicationFactor = 9
    RULE_elementExpression = 10
    RULE_elementAccess = 11
    RULE_expressionList = 12
    RULE_primitiveExpression = 13
    RULE_listExpression = 14
    RULE_ident = 15

    ruleNames =  [ "program", "statement", "argList", "sequence", "expression", 
                   "comparison", "additionExpression", "additionFactor", 
                   "multiplicationExpression", "multiplicationFactor", "elementExpression", 
                   "elementAccess", "expressionList", "primitiveExpression", 
                   "listExpression", "ident" ]

    EOF = Token.EOF
    COMMA=1
    COLON=2
    LEFTSQUARE=3
    RIGHTSQUARE=4
    LEFTP=5
    RIGHTP=6
    ASSIGN=7
    SQUOTES=8
    DQUOTES=9
    QUOTES=10
    IF=11
    ELSE=12
    ELIF=13
    WHILE=14
    CONST=15
    FOR=16
    RETURN=17
    PRINT=18
    LEN=19
    IN=20
    DEF=21
    ADD=22
    SUB=23
    MUL=24
    DIV=25
    INTDIV=26
    GT=27
    LT=28
    LET=29
    GET=30
    EQUAL=31
    NOTEQUAL=32
    BSN=33
    BST=34
    ES=35
    FLOAT=36
    CHAR=37
    STRING=38
    NUM=39
    ID=40
    NEWLINE=41
    WS=42
    SKIPP=43
    INDENT=44
    DEDENT=45

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


        def getRuleIndex(self):
            return miParserParser.RULE_program

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramASTContext(ProgramContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ProgramContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(miParserParser.StatementContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramAST" ):
                return visitor.visitProgramAST(self)
            else:
                return visitor.visitChildren(self)



    def program(self):

        localctx = miParserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ProgramASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.IF) | (1 << miParserParser.WHILE) | (1 << miParserParser.FOR) | (1 << miParserParser.RETURN) | (1 << miParserParser.PRINT) | (1 << miParserParser.LEN) | (1 << miParserParser.DEF) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0):
                self.state = 32
                self.statement()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(miParserParser.WHILE, 0)
        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

        def COLON(self):
            return self.getToken(miParserParser.COLON, 0)
        def sequence(self):
            return self.getTypedRuleContext(miParserParser.SequenceContext,0)

        def LEFTP(self):
            return self.getToken(miParserParser.LEFTP, 0)
        def RIGHTP(self):
            return self.getToken(miParserParser.RIGHTP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)


    class DefStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEF(self):
            return self.getToken(miParserParser.DEF, 0)
        def ID(self):
            return self.getToken(miParserParser.ID, 0)
        def LEFTP(self):
            return self.getToken(miParserParser.LEFTP, 0)
        def argList(self):
            return self.getTypedRuleContext(miParserParser.ArgListContext,0)

        def RIGHTP(self):
            return self.getToken(miParserParser.RIGHTP, 0)
        def COLON(self):
            return self.getToken(miParserParser.COLON, 0)
        def sequence(self):
            return self.getTypedRuleContext(miParserParser.SequenceContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefStatement" ):
                return visitor.visitDefStatement(self)
            else:
                return visitor.visitChildren(self)


    class PrintStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(miParserParser.PRINT, 0)
        def LEFTP(self):
            return self.getToken(miParserParser.LEFTP, 0)
        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

        def RIGHTP(self):
            return self.getToken(miParserParser.RIGHTP, 0)
        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)


    class ForStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(miParserParser.FOR, 0)
        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

        def IN(self):
            return self.getToken(miParserParser.IN, 0)
        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)

        def COLON(self):
            return self.getToken(miParserParser.COLON, 0)
        def sequence(self):
            return self.getTypedRuleContext(miParserParser.SequenceContext,0)

        def LEFTP(self):
            return self.getToken(miParserParser.LEFTP, 0)
        def RIGHTP(self):
            return self.getToken(miParserParser.RIGHTP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)


    class AssignStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(miParserParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(miParserParser.ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primitiveExpression(self):
            return self.getTypedRuleContext(miParserParser.PrimitiveExpressionContext,0)

        def LEFTP(self):
            return self.getToken(miParserParser.LEFTP, 0)
        def RIGHTP(self):
            return self.getToken(miParserParser.RIGHTP, 0)
        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)
        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallStatement" ):
                return visitor.visitFunctionCallStatement(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)

        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(miParserParser.IF, 0)
        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.COLON)
            else:
                return self.getToken(miParserParser.COLON, i)
        def sequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.SequenceContext)
            else:
                return self.getTypedRuleContext(miParserParser.SequenceContext,i)

        def LEFTP(self):
            return self.getToken(miParserParser.LEFTP, 0)
        def RIGHTP(self):
            return self.getToken(miParserParser.RIGHTP, 0)
        def ELSE(self):
            return self.getToken(miParserParser.ELSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(miParserParser.RETURN, 0)
        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)
        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

        def LEFTP(self):
            return self.getToken(miParserParser.LEFTP, 0)
        def RIGHTP(self):
            return self.getToken(miParserParser.RIGHTP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = miParserParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = miParserParser.DefStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(miParserParser.DEF)
                self.state = 39
                self.match(miParserParser.ID)
                self.state = 40
                self.match(miParserParser.LEFTP)
                self.state = 41
                self.argList()
                self.state = 42
                self.match(miParserParser.RIGHTP)
                self.state = 43
                self.match(miParserParser.COLON)
                self.state = 44
                self.sequence()
                pass

            elif la_ == 2:
                localctx = miParserParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(miParserParser.IF)
                self.state = 48
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 47
                    self.match(miParserParser.LEFTP)


                self.state = 50
                self.expression()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.RIGHTP:
                    self.state = 51
                    self.match(miParserParser.RIGHTP)


                self.state = 54
                self.match(miParserParser.COLON)
                self.state = 55
                self.sequence()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.ELSE:
                    self.state = 56
                    self.match(miParserParser.ELSE)
                    self.state = 57
                    self.match(miParserParser.COLON)
                    self.state = 58
                    self.sequence()


                pass

            elif la_ == 3:
                localctx = miParserParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(miParserParser.RETURN)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.LEN) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0):
                    self.state = 63
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        self.state = 62
                        self.match(miParserParser.LEFTP)


                    self.state = 65
                    self.expression()
                    self.state = 67
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==miParserParser.RIGHTP:
                        self.state = 66
                        self.match(miParserParser.RIGHTP)




                self.state = 71
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = miParserParser.PrintStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.match(miParserParser.PRINT)
                self.state = 73
                self.match(miParserParser.LEFTP)
                self.state = 74
                self.expression()
                self.state = 75
                self.match(miParserParser.RIGHTP)
                self.state = 76
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 5:
                localctx = miParserParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.match(miParserParser.WHILE)
                self.state = 80
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 79
                    self.match(miParserParser.LEFTP)


                self.state = 82
                self.expression()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.RIGHTP:
                    self.state = 83
                    self.match(miParserParser.RIGHTP)


                self.state = 86
                self.match(miParserParser.COLON)
                self.state = 87
                self.sequence()
                pass

            elif la_ == 6:
                localctx = miParserParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 89
                self.match(miParserParser.FOR)
                self.state = 91
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 90
                    self.match(miParserParser.LEFTP)


                self.state = 93
                self.expression()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.RIGHTP:
                    self.state = 94
                    self.match(miParserParser.RIGHTP)


                self.state = 97
                self.match(miParserParser.IN)
                self.state = 98
                self.expressionList()
                self.state = 99
                self.match(miParserParser.COLON)
                self.state = 100
                self.sequence()
                pass

            elif la_ == 7:
                localctx = miParserParser.AssignStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 102
                self.match(miParserParser.ID)
                self.state = 103
                self.match(miParserParser.ASSIGN)
                self.state = 104
                self.expression()
                self.state = 105
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 8:
                localctx = miParserParser.FunctionCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 107
                self.primitiveExpression()
                self.state = 108
                self.match(miParserParser.LEFTP)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.LEN) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0):
                    self.state = 109
                    self.expressionList()


                self.state = 112
                self.match(miParserParser.RIGHTP)
                self.state = 113
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 9:
                localctx = miParserParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 115
                self.expressionList()
                self.state = 116
                self.match(miParserParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_argList

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArgumentContext(ArgListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ArgListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(miParserParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)


    class ArgumentsListContext(ArgListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ArgListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.ID)
            else:
                return self.getToken(miParserParser.ID, i)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.COMMA)
            else:
                return self.getToken(miParserParser.COMMA, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentsList" ):
                return visitor.visitArgumentsList(self)
            else:
                return visitor.visitChildren(self)



    def argList(self):

        localctx = miParserParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = miParserParser.ArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.ID:
                    self.state = 120
                    self.match(miParserParser.ID)


                pass

            elif la_ == 2:
                localctx = miParserParser.ArgumentsListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(miParserParser.ID)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==miParserParser.COMMA:
                    self.state = 124
                    self.match(miParserParser.COMMA)
                    self.state = 125
                    self.match(miParserParser.ID)
                    self.state = 130
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_sequence

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SequenceASTContext(SequenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.SequenceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INDENT(self):
            return self.getToken(miParserParser.INDENT, 0)
        def DEDENT(self):
            return self.getToken(miParserParser.DEDENT, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(miParserParser.StatementContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequenceAST" ):
                return visitor.visitSequenceAST(self)
            else:
                return visitor.visitChildren(self)



    def sequence(self):

        localctx = miParserParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sequence)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.SequenceASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(miParserParser.INDENT)
            self.state = 135 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 134
                self.statement()
                self.state = 137 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.IF) | (1 << miParserParser.WHILE) | (1 << miParserParser.FOR) | (1 << miParserParser.RETURN) | (1 << miParserParser.PRINT) | (1 << miParserParser.LEN) | (1 << miParserParser.DEF) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0)):
                    break

            self.state = 139
            self.match(miParserParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionASTContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def additionExpression(self):
            return self.getTypedRuleContext(miParserParser.AdditionExpressionContext,0)

        def comparison(self):
            return self.getTypedRuleContext(miParserParser.ComparisonContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionAST" ):
                return visitor.visitExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def expression(self):

        localctx = miParserParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            localctx = miParserParser.ExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.additionExpression()
            self.state = 142
            self.comparison()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_comparison

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComparisonASTContext(ComparisonContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ComparisonContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def additionExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.AdditionExpressionContext)
            else:
                return self.getTypedRuleContext(miParserParser.AdditionExpressionContext,i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.LT)
            else:
                return self.getToken(miParserParser.LT, i)
        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.GT)
            else:
                return self.getToken(miParserParser.GT, i)
        def LET(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.LET)
            else:
                return self.getToken(miParserParser.LET, i)
        def GET(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.GET)
            else:
                return self.getToken(miParserParser.GET, i)
        def EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.EQUAL)
            else:
                return self.getToken(miParserParser.EQUAL, i)
        def NOTEQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.NOTEQUAL)
            else:
                return self.getToken(miParserParser.NOTEQUAL, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonAST" ):
                return visitor.visitComparisonAST(self)
            else:
                return visitor.visitChildren(self)



    def comparison(self):

        localctx = miParserParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ComparisonASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.GT) | (1 << miParserParser.LT) | (1 << miParserParser.LET) | (1 << miParserParser.GET) | (1 << miParserParser.EQUAL) | (1 << miParserParser.NOTEQUAL))) != 0):
                self.state = 144
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.GT) | (1 << miParserParser.LT) | (1 << miParserParser.LET) | (1 << miParserParser.GET) | (1 << miParserParser.EQUAL) | (1 << miParserParser.NOTEQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 145
                self.additionExpression()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_additionExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AditionalExpressionASTContext(AdditionExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.AdditionExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multiplicationExpression(self):
            return self.getTypedRuleContext(miParserParser.MultiplicationExpressionContext,0)

        def additionFactor(self):
            return self.getTypedRuleContext(miParserParser.AdditionFactorContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAditionalExpressionAST" ):
                return visitor.visitAditionalExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def additionExpression(self):

        localctx = miParserParser.AdditionExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_additionExpression)
        try:
            localctx = miParserParser.AditionalExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.multiplicationExpression()
            self.state = 152
            self.additionFactor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_additionFactor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddFactorContext(AdditionFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.AdditionFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def elementExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.ElementExpressionContext)
            else:
                return self.getTypedRuleContext(miParserParser.ElementExpressionContext,i)

        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.ADD)
            else:
                return self.getToken(miParserParser.ADD, i)
        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.SUB)
            else:
                return self.getToken(miParserParser.SUB, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddFactor" ):
                return visitor.visitAddFactor(self)
            else:
                return visitor.visitChildren(self)



    def additionFactor(self):

        localctx = miParserParser.AdditionFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_additionFactor)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.AddFactorContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.ADD or _la==miParserParser.SUB:
                self.state = 154
                _la = self._input.LA(1)
                if not(_la==miParserParser.ADD or _la==miParserParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 155
                self.elementExpression()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_multiplicationExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MultiplicationExpressionASTContext(MultiplicationExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.MultiplicationExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def elementExpression(self):
            return self.getTypedRuleContext(miParserParser.ElementExpressionContext,0)

        def multiplicationFactor(self):
            return self.getTypedRuleContext(miParserParser.MultiplicationFactorContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicationExpressionAST" ):
                return visitor.visitMultiplicationExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def multiplicationExpression(self):

        localctx = miParserParser.MultiplicationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_multiplicationExpression)
        try:
            localctx = miParserParser.MultiplicationExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.elementExpression()
            self.state = 162
            self.multiplicationFactor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicationFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_multiplicationFactor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MulFactorContext(MultiplicationFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.MultiplicationFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def elementExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.ElementExpressionContext)
            else:
                return self.getTypedRuleContext(miParserParser.ElementExpressionContext,i)

        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.MUL)
            else:
                return self.getToken(miParserParser.MUL, i)
        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.DIV)
            else:
                return self.getToken(miParserParser.DIV, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulFactor" ):
                return visitor.visitMulFactor(self)
            else:
                return visitor.visitChildren(self)



    def multiplicationFactor(self):

        localctx = miParserParser.MultiplicationFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_multiplicationFactor)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.MulFactorContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.MUL or _la==miParserParser.DIV:
                self.state = 164
                _la = self._input.LA(1)
                if not(_la==miParserParser.MUL or _la==miParserParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 165
                self.elementExpression()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_elementExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ElementExpressionASTContext(ElementExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ElementExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primitiveExpression(self):
            return self.getTypedRuleContext(miParserParser.PrimitiveExpressionContext,0)

        def elementAccess(self):
            return self.getTypedRuleContext(miParserParser.ElementAccessContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementExpressionAST" ):
                return visitor.visitElementExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def elementExpression(self):

        localctx = miParserParser.ElementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elementExpression)
        try:
            localctx = miParserParser.ElementExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.primitiveExpression()
            self.state = 172
            self.elementAccess()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_elementAccess

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ElementAccessASTContext(ElementAccessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ElementAccessContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFTSQUARE(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.LEFTSQUARE)
            else:
                return self.getToken(miParserParser.LEFTSQUARE, i)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(miParserParser.ExpressionContext,i)

        def RIGHTSQUARE(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.RIGHTSQUARE)
            else:
                return self.getToken(miParserParser.RIGHTSQUARE, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementAccessAST" ):
                return visitor.visitElementAccessAST(self)
            else:
                return visitor.visitChildren(self)



    def elementAccess(self):

        localctx = miParserParser.ElementAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_elementAccess)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ElementAccessASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.LEFTSQUARE:
                self.state = 174
                self.match(miParserParser.LEFTSQUARE)
                self.state = 175
                self.expression()
                self.state = 176
                self.match(miParserParser.RIGHTSQUARE)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_expressionList

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionListASTContext(ExpressionListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ExpressionListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(miParserParser.ExpressionContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.COMMA)
            else:
                return self.getToken(miParserParser.COMMA, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionListAST" ):
                return visitor.visitExpressionListAST(self)
            else:
                return visitor.visitChildren(self)



    def expressionList(self):

        localctx = miParserParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ExpressionListASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.expression()
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.COMMA:
                self.state = 184
                self.match(miParserParser.COMMA)
                self.state = 185
                self.expression()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_primitiveExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FloatPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(miParserParser.FLOAT, 0)
        def SUB(self):
            return self.getToken(miParserParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatPE" ):
                return visitor.visitFloatPE(self)
            else:
                return visitor.visitChildren(self)


    class ExpressPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFTP(self):
            return self.getToken(miParserParser.LEFTP, 0)
        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)

        def RIGHTP(self):
            return self.getToken(miParserParser.RIGHTP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressPE" ):
                return visitor.visitExpressPE(self)
            else:
                return visitor.visitChildren(self)


    class ListExPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def listExpression(self):
            return self.getTypedRuleContext(miParserParser.ListExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExPE" ):
                return visitor.visitListExPE(self)
            else:
                return visitor.visitChildren(self)


    class IntegerPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(miParserParser.NUM, 0)
        def SUB(self):
            return self.getToken(miParserParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerPE" ):
                return visitor.visitIntegerPE(self)
            else:
                return visitor.visitChildren(self)


    class CallPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ident(self):
            return self.getTypedRuleContext(miParserParser.IdentContext,0)

        def LEFTP(self):
            return self.getToken(miParserParser.LEFTP, 0)
        def RIGHTP(self):
            return self.getToken(miParserParser.RIGHTP, 0)
        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallPE" ):
                return visitor.visitCallPE(self)
            else:
                return visitor.visitChildren(self)


    class StringPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(miParserParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringPE" ):
                return visitor.visitStringPE(self)
            else:
                return visitor.visitChildren(self)


    class LenPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEN(self):
            return self.getToken(miParserParser.LEN, 0)
        def LEFTP(self):
            return self.getToken(miParserParser.LEFTP, 0)
        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

        def RIGHTP(self):
            return self.getToken(miParserParser.RIGHTP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLenPE" ):
                return visitor.visitLenPE(self)
            else:
                return visitor.visitChildren(self)


    class CharPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(miParserParser.CHAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharPE" ):
                return visitor.visitCharPE(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ident(self):
            return self.getTypedRuleContext(miParserParser.IdentContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierPE" ):
                return visitor.visitIdentifierPE(self)
            else:
                return visitor.visitChildren(self)



    def primitiveExpression(self):

        localctx = miParserParser.PrimitiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_primitiveExpression)
        self._la = 0 # Token type
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = miParserParser.IntegerPEContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.SUB:
                    self.state = 191
                    self.match(miParserParser.SUB)


                self.state = 194
                self.match(miParserParser.NUM)
                pass

            elif la_ == 2:
                localctx = miParserParser.FloatPEContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.SUB:
                    self.state = 195
                    self.match(miParserParser.SUB)


                self.state = 198
                self.match(miParserParser.FLOAT)
                pass

            elif la_ == 3:
                localctx = miParserParser.CharPEContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.match(miParserParser.CHAR)
                pass

            elif la_ == 4:
                localctx = miParserParser.StringPEContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 200
                self.match(miParserParser.STRING)
                pass

            elif la_ == 5:
                localctx = miParserParser.IdentifierPEContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 201
                self.ident()
                pass

            elif la_ == 6:
                localctx = miParserParser.CallPEContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 202
                self.ident()

                self.state = 203
                self.match(miParserParser.LEFTP)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.LEN) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0):
                    self.state = 204
                    self.expressionList()


                self.state = 207
                self.match(miParserParser.RIGHTP)
                pass

            elif la_ == 7:
                localctx = miParserParser.ExpressPEContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 209
                self.match(miParserParser.LEFTP)
                self.state = 210
                self.expressionList()
                self.state = 211
                self.match(miParserParser.RIGHTP)
                pass

            elif la_ == 8:
                localctx = miParserParser.ListExPEContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 213
                self.listExpression()
                pass

            elif la_ == 9:
                localctx = miParserParser.LenPEContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 214
                self.match(miParserParser.LEN)
                self.state = 215
                self.match(miParserParser.LEFTP)
                self.state = 216
                self.expression()
                self.state = 217
                self.match(miParserParser.RIGHTP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_listExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ListExpressionASTContext(ListExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ListExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFTSQUARE(self):
            return self.getToken(miParserParser.LEFTSQUARE, 0)
        def RIGHTSQUARE(self):
            return self.getToken(miParserParser.RIGHTSQUARE, 0)
        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpressionAST" ):
                return visitor.visitListExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def listExpression(self):

        localctx = miParserParser.ListExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listExpression)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ListExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(miParserParser.LEFTSQUARE)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.LEN) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0):
                self.state = 222
                self.expressionList()


            self.state = 225
            self.match(miParserParser.RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_ident

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdentASTContext(IdentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.IdentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(miParserParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentAST" ):
                return visitor.visitIdentAST(self)
            else:
                return visitor.visitChildren(self)



    def ident(self):

        localctx = miParserParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ident)
        try:
            localctx = miParserParser.IdentASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(miParserParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





