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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3.")
        buf.write("\u00e3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\7\2$\n\2\f\2\16")
        buf.write("\2\'\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write("\63\n\3\3\3\3\3\5\3\67\n\3\3\3\3\3\3\3\3\3\3\3\5\3>\n")
        buf.write("\3\3\3\3\3\5\3B\n\3\3\3\3\3\5\3F\n\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3R\n\3\3\3\3\3\5\3V\n\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3]\n\3\3\3\3\3\5\3a\n\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3v\n\3\3\4\5\4y\n\4\3\4\3\4\3\4\7\4~\n\4\f")
        buf.write("\4\16\4\u0081\13\4\5\4\u0083\n\4\3\5\3\5\6\5\u0087\n\5")
        buf.write("\r\5\16\5\u0088\3\5\3\5\3\6\3\6\3\6\3\7\3\7\7\7\u0092")
        buf.write("\n\7\f\7\16\7\u0095\13\7\3\b\3\b\3\b\3\t\3\t\7\t\u009c")
        buf.write("\n\t\f\t\16\t\u009f\13\t\3\n\3\n\3\n\3\13\3\13\7\13\u00a6")
        buf.write("\n\13\f\13\16\13\u00a9\13\13\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\7\r\u00b2\n\r\f\r\16\r\u00b5\13\r\3\16\3\16\3\16\7")
        buf.write("\16\u00ba\n\16\f\16\16\16\u00bd\13\16\3\17\5\17\u00c0")
        buf.write("\n\17\3\17\3\17\5\17\u00c4\n\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\5\17\u00cc\n\17\3\17\5\17\u00cf\n\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00db\n")
        buf.write("\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\2\2\22\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \2\5\3\2\35!\3\2\30\31")
        buf.write("\3\2\32\33\2\u00f8\2%\3\2\2\2\4u\3\2\2\2\6\u0082\3\2\2")
        buf.write("\2\b\u0084\3\2\2\2\n\u008c\3\2\2\2\f\u0093\3\2\2\2\16")
        buf.write("\u0096\3\2\2\2\20\u009d\3\2\2\2\22\u00a0\3\2\2\2\24\u00a7")
        buf.write("\3\2\2\2\26\u00aa\3\2\2\2\30\u00b3\3\2\2\2\32\u00b6\3")
        buf.write("\2\2\2\34\u00da\3\2\2\2\36\u00dc\3\2\2\2 \u00e0\3\2\2")
        buf.write("\2\"$\5\4\3\2#\"\3\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2")
        buf.write("\2&\3\3\2\2\2\'%\3\2\2\2()\7\27\2\2)*\5 \21\2*+\7\7\2")
        buf.write("\2+,\5\6\4\2,-\7\b\2\2-.\7\4\2\2./\5\b\5\2/v\3\2\2\2\60")
        buf.write("\62\7\r\2\2\61\63\7\7\2\2\62\61\3\2\2\2\62\63\3\2\2\2")
        buf.write("\63\64\3\2\2\2\64\66\5\n\6\2\65\67\7\b\2\2\66\65\3\2\2")
        buf.write("\2\66\67\3\2\2\2\678\3\2\2\289\7\4\2\29=\5\b\5\2:;\7\16")
        buf.write("\2\2;<\7\4\2\2<>\5\b\5\2=:\3\2\2\2=>\3\2\2\2>v\3\2\2\2")
        buf.write("?A\7\23\2\2@B\7\7\2\2A@\3\2\2\2AB\3\2\2\2BC\3\2\2\2CE")
        buf.write("\5\n\6\2DF\7\b\2\2ED\3\2\2\2EF\3\2\2\2FG\3\2\2\2GH\7*")
        buf.write("\2\2Hv\3\2\2\2IJ\7\24\2\2JK\7\7\2\2KL\5\n\6\2LM\7\b\2")
        buf.write("\2MN\7*\2\2Nv\3\2\2\2OQ\7\20\2\2PR\7\7\2\2QP\3\2\2\2Q")
        buf.write("R\3\2\2\2RS\3\2\2\2SU\5\n\6\2TV\7\b\2\2UT\3\2\2\2UV\3")
        buf.write("\2\2\2VW\3\2\2\2WX\7\4\2\2XY\5\b\5\2Yv\3\2\2\2Z\\\7\22")
        buf.write("\2\2[]\7\7\2\2\\[\3\2\2\2\\]\3\2\2\2]^\3\2\2\2^`\5\n\6")
        buf.write("\2_a\7\b\2\2`_\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\7\26\2\2")
        buf.write("cd\5\32\16\2de\7\4\2\2ef\5\b\5\2fv\3\2\2\2gh\5 \21\2h")
        buf.write("i\7\t\2\2ij\5\n\6\2jk\7*\2\2kv\3\2\2\2lm\5\34\17\2mn\7")
        buf.write("\7\2\2no\5\32\16\2op\7\b\2\2pq\7*\2\2qv\3\2\2\2rs\5\32")
        buf.write("\16\2st\7*\2\2tv\3\2\2\2u(\3\2\2\2u\60\3\2\2\2u?\3\2\2")
        buf.write("\2uI\3\2\2\2uO\3\2\2\2uZ\3\2\2\2ug\3\2\2\2ul\3\2\2\2u")
        buf.write("r\3\2\2\2v\5\3\2\2\2wy\5 \21\2xw\3\2\2\2xy\3\2\2\2y\u0083")
        buf.write("\3\2\2\2z\177\5 \21\2{|\7\3\2\2|~\5 \21\2}{\3\2\2\2~\u0081")
        buf.write("\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0083\3")
        buf.write("\2\2\2\u0081\177\3\2\2\2\u0082x\3\2\2\2\u0082z\3\2\2\2")
        buf.write("\u0083\7\3\2\2\2\u0084\u0086\7-\2\2\u0085\u0087\5\4\3")
        buf.write("\2\u0086\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0086")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\u008b\7.\2\2\u008b\t\3\2\2\2\u008c\u008d\5\16\b\2\u008d")
        buf.write("\u008e\5\f\7\2\u008e\13\3\2\2\2\u008f\u0090\t\2\2\2\u0090")
        buf.write("\u0092\5\16\b\2\u0091\u008f\3\2\2\2\u0092\u0095\3\2\2")
        buf.write("\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\r\3\2")
        buf.write("\2\2\u0095\u0093\3\2\2\2\u0096\u0097\5\22\n\2\u0097\u0098")
        buf.write("\5\20\t\2\u0098\17\3\2\2\2\u0099\u009a\t\3\2\2\u009a\u009c")
        buf.write("\5\26\f\2\u009b\u0099\3\2\2\2\u009c\u009f\3\2\2\2\u009d")
        buf.write("\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e\21\3\2\2\2\u009f")
        buf.write("\u009d\3\2\2\2\u00a0\u00a1\5\26\f\2\u00a1\u00a2\5\24\13")
        buf.write("\2\u00a2\23\3\2\2\2\u00a3\u00a4\t\4\2\2\u00a4\u00a6\5")
        buf.write("\26\f\2\u00a5\u00a3\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7")
        buf.write("\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\25\3\2\2\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00aa\u00ab\5\34\17\2\u00ab\u00ac\5\30")
        buf.write("\r\2\u00ac\27\3\2\2\2\u00ad\u00ae\7\5\2\2\u00ae\u00af")
        buf.write("\5\n\6\2\u00af\u00b0\7\6\2\2\u00b0\u00b2\3\2\2\2\u00b1")
        buf.write("\u00ad\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2")
        buf.write("\u00b3\u00b4\3\2\2\2\u00b4\31\3\2\2\2\u00b5\u00b3\3\2")
        buf.write("\2\2\u00b6\u00bb\5\n\6\2\u00b7\u00b8\7\3\2\2\u00b8\u00ba")
        buf.write("\5\n\6\2\u00b9\u00b7\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\33\3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00be\u00c0\7\31\2\2\u00bf\u00be\3\2\2")
        buf.write("\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00db")
        buf.write("\7(\2\2\u00c2\u00c4\7\31\2\2\u00c3\u00c2\3\2\2\2\u00c3")
        buf.write("\u00c4\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00db\7%\2\2")
        buf.write("\u00c6\u00db\7&\2\2\u00c7\u00db\7\'\2\2\u00c8\u00ce\5")
        buf.write(" \21\2\u00c9\u00cb\7\7\2\2\u00ca\u00cc\5\32\16\2\u00cb")
        buf.write("\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\u00cf\7\b\2\2\u00ce\u00c9\3\2\2\2\u00ce\u00cf\3")
        buf.write("\2\2\2\u00cf\u00db\3\2\2\2\u00d0\u00d1\7\7\2\2\u00d1\u00d2")
        buf.write("\5\n\6\2\u00d2\u00d3\7\b\2\2\u00d3\u00db\3\2\2\2\u00d4")
        buf.write("\u00db\5\36\20\2\u00d5\u00d6\7\25\2\2\u00d6\u00d7\7\7")
        buf.write("\2\2\u00d7\u00d8\5\n\6\2\u00d8\u00d9\7\b\2\2\u00d9\u00db")
        buf.write("\3\2\2\2\u00da\u00bf\3\2\2\2\u00da\u00c3\3\2\2\2\u00da")
        buf.write("\u00c6\3\2\2\2\u00da\u00c7\3\2\2\2\u00da\u00c8\3\2\2\2")
        buf.write("\u00da\u00d0\3\2\2\2\u00da\u00d4\3\2\2\2\u00da\u00d5\3")
        buf.write("\2\2\2\u00db\35\3\2\2\2\u00dc\u00dd\7\5\2\2\u00dd\u00de")
        buf.write("\5\32\16\2\u00de\u00df\7\6\2\2\u00df\37\3\2\2\2\u00e0")
        buf.write("\u00e1\7)\2\2\u00e1!\3\2\2\2\33%\62\66=AEQU\\`ux\177\u0082")
        buf.write("\u0088\u0093\u009d\u00a7\u00b3\u00bb\u00bf\u00c3\u00cb")
        buf.write("\u00ce\u00da")
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
                     "'=='", "'\\n'", "'\\t'" ]

    symbolicNames = [ "<INVALID>", "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", 
                      "LEFTP", "RIGHTP", "ASSIGN", "SQUOTES", "DQUOTES", 
                      "QUOTES", "IF", "ELSE", "ELIF", "WHILE", "CONST", 
                      "FOR", "RETURN", "PRINT", "LEN", "IN", "DEF", "ADD", 
                      "SUB", "MUL", "DIV", "INTDIV", "GT", "LT", "LET", 
                      "GET", "EQUAL", "BSN", "BST", "ES", "FLOAT", "CHAR", 
                      "STRING", "NUM", "ID", "NEWLINE", "WS", "SKIPP", "INDENT", 
                      "DEDENT" ]

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
    BSN=32
    BST=33
    ES=34
    FLOAT=35
    CHAR=36
    STRING=37
    NUM=38
    ID=39
    NEWLINE=40
    WS=41
    SKIPP=42
    INDENT=43
    DEDENT=44

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
        def ident(self):
            return self.getTypedRuleContext(miParserParser.IdentContext,0)

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

        def ident(self):
            return self.getTypedRuleContext(miParserParser.IdentContext,0)

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
        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)

        def RIGHTP(self):
            return self.getToken(miParserParser.RIGHTP, 0)
        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)

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
        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)
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
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = miParserParser.DefStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(miParserParser.DEF)
                self.state = 39
                self.ident()
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


                self.state = 69
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = miParserParser.PrintStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.match(miParserParser.PRINT)
                self.state = 72
                self.match(miParserParser.LEFTP)
                self.state = 73
                self.expression()
                self.state = 74
                self.match(miParserParser.RIGHTP)
                self.state = 75
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 5:
                localctx = miParserParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.match(miParserParser.WHILE)
                self.state = 79
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 78
                    self.match(miParserParser.LEFTP)


                self.state = 81
                self.expression()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.RIGHTP:
                    self.state = 82
                    self.match(miParserParser.RIGHTP)


                self.state = 85
                self.match(miParserParser.COLON)
                self.state = 86
                self.sequence()
                pass

            elif la_ == 6:
                localctx = miParserParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.match(miParserParser.FOR)
                self.state = 90
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 89
                    self.match(miParserParser.LEFTP)


                self.state = 92
                self.expression()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.RIGHTP:
                    self.state = 93
                    self.match(miParserParser.RIGHTP)


                self.state = 96
                self.match(miParserParser.IN)
                self.state = 97
                self.expressionList()
                self.state = 98
                self.match(miParserParser.COLON)
                self.state = 99
                self.sequence()
                pass

            elif la_ == 7:
                localctx = miParserParser.AssignStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 101
                self.ident()
                self.state = 102
                self.match(miParserParser.ASSIGN)
                self.state = 103
                self.expression()
                self.state = 104
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 8:
                localctx = miParserParser.FunctionCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 106
                self.primitiveExpression()
                self.state = 107
                self.match(miParserParser.LEFTP)
                self.state = 108
                self.expressionList()
                self.state = 109
                self.match(miParserParser.RIGHTP)
                self.state = 110
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 9:
                localctx = miParserParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 112
                self.expressionList()
                self.state = 113
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

        def ident(self):
            return self.getTypedRuleContext(miParserParser.IdentContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)


    class ArgumentsListContext(ArgListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ArgListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ident(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.IdentContext)
            else:
                return self.getTypedRuleContext(miParserParser.IdentContext,i)

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
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = miParserParser.ArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.ID:
                    self.state = 117
                    self.ident()


                pass

            elif la_ == 2:
                localctx = miParserParser.ArgumentsListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.ident()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==miParserParser.COMMA:
                    self.state = 121
                    self.match(miParserParser.COMMA)
                    self.state = 122
                    self.ident()
                    self.state = 127
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
            self.state = 130
            self.match(miParserParser.INDENT)
            self.state = 132 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 131
                self.statement()
                self.state = 134 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.IF) | (1 << miParserParser.WHILE) | (1 << miParserParser.FOR) | (1 << miParserParser.RETURN) | (1 << miParserParser.PRINT) | (1 << miParserParser.LEN) | (1 << miParserParser.DEF) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0)):
                    break

            self.state = 136
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
            self.state = 138
            self.additionExpression()
            self.state = 139
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
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.GT) | (1 << miParserParser.LT) | (1 << miParserParser.LET) | (1 << miParserParser.GET) | (1 << miParserParser.EQUAL))) != 0):
                self.state = 141
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.GT) | (1 << miParserParser.LT) | (1 << miParserParser.LET) | (1 << miParserParser.GET) | (1 << miParserParser.EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 142
                self.additionExpression()
                self.state = 147
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
            self.state = 148
            self.multiplicationExpression()
            self.state = 149
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
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.ADD or _la==miParserParser.SUB:
                self.state = 151
                _la = self._input.LA(1)
                if not(_la==miParserParser.ADD or _la==miParserParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 152
                self.elementExpression()
                self.state = 157
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
            self.state = 158
            self.elementExpression()
            self.state = 159
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
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.MUL or _la==miParserParser.DIV:
                self.state = 161
                _la = self._input.LA(1)
                if not(_la==miParserParser.MUL or _la==miParserParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 162
                self.elementExpression()
                self.state = 167
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
            self.state = 168
            self.primitiveExpression()
            self.state = 169
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
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.LEFTSQUARE:
                self.state = 171
                self.match(miParserParser.LEFTSQUARE)
                self.state = 172
                self.expression()
                self.state = 173
                self.match(miParserParser.RIGHTSQUARE)
                self.state = 179
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
            self.state = 180
            self.expression()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.COMMA:
                self.state = 181
                self.match(miParserParser.COMMA)
                self.state = 182
                self.expression()
                self.state = 187
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
        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

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

        def LEFTP(self):
            return self.getToken(miParserParser.LEFTP, 0)
        def RIGHTP(self):
            return self.getToken(miParserParser.RIGHTP, 0)
        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)


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
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                localctx = miParserParser.IntegerPEContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.SUB:
                    self.state = 188
                    self.match(miParserParser.SUB)


                self.state = 191
                self.match(miParserParser.NUM)
                pass

            elif la_ == 2:
                localctx = miParserParser.FloatPEContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.SUB:
                    self.state = 192
                    self.match(miParserParser.SUB)


                self.state = 195
                self.match(miParserParser.FLOAT)
                pass

            elif la_ == 3:
                localctx = miParserParser.CharPEContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.match(miParserParser.CHAR)
                pass

            elif la_ == 4:
                localctx = miParserParser.StringPEContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 197
                self.match(miParserParser.STRING)
                pass

            elif la_ == 5:
                localctx = miParserParser.IdentifierPEContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 198
                self.ident()
                self.state = 204
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 199
                    self.match(miParserParser.LEFTP)
                    self.state = 201
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.LEN) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0):
                        self.state = 200
                        self.expressionList()


                    self.state = 203
                    self.match(miParserParser.RIGHTP)


                pass

            elif la_ == 6:
                localctx = miParserParser.ExpressPEContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 206
                self.match(miParserParser.LEFTP)
                self.state = 207
                self.expression()
                self.state = 208
                self.match(miParserParser.RIGHTP)
                pass

            elif la_ == 7:
                localctx = miParserParser.ListExPEContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 210
                self.listExpression()
                pass

            elif la_ == 8:
                localctx = miParserParser.LenPEContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 211
                self.match(miParserParser.LEN)
                self.state = 212
                self.match(miParserParser.LEFTP)
                self.state = 213
                self.expression()
                self.state = 214
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
        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)

        def RIGHTSQUARE(self):
            return self.getToken(miParserParser.RIGHTSQUARE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpressionAST" ):
                return visitor.visitListExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def listExpression(self):

        localctx = miParserParser.ListExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listExpression)
        try:
            localctx = miParserParser.ListExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(miParserParser.LEFTSQUARE)
            self.state = 219
            self.expressionList()
            self.state = 220
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
            self.state = 222
            self.match(miParserParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





