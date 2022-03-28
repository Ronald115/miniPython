# Generated from D:/Sebas/TEC/2022/1 Semestre/Compiladores e Interpretes/MiniPy/miniPython\miParser.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3)")
        buf.write("\u00d9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\7\2\"\n\2\f\2\16\2%\13\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\61\n\3\3")
        buf.write("\3\3\3\5\3\65\n\3\3\3\3\3\3\3\3\3\3\3\5\3<\n\3\3\3\3\3")
        buf.write("\5\3@\n\3\3\3\3\3\5\3D\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3P\n\3\3\3\3\3\5\3T\n\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3[\n\3\3\3\3\3\5\3_\n\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3t\n\3\3\4\5\4w\n\4\3\4\3\4\3\4\7\4|\n\4\f\4\16\4\177")
        buf.write("\13\4\5\4\u0081\n\4\3\5\3\5\6\5\u0085\n\5\r\5\16\5\u0086")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\7\3\7\7\7\u0090\n\7\f\7\16\7\u0093")
        buf.write("\13\7\3\b\3\b\3\b\3\t\3\t\7\t\u009a\n\t\f\t\16\t\u009d")
        buf.write("\13\t\3\n\3\n\3\n\3\13\3\13\7\13\u00a4\n\13\f\13\16\13")
        buf.write("\u00a7\13\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\7\r\u00b0\n\r")
        buf.write("\f\r\16\r\u00b3\13\r\3\16\3\16\3\16\7\16\u00b8\n\16\f")
        buf.write("\16\16\16\u00bb\13\16\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\5\17\u00c4\n\17\3\17\5\17\u00c7\n\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00d3\n\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\2\2\21\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36\2\5\3\2\33\37\3\2\26\27\3\2\30\31\2\u00ed")
        buf.write("\2#\3\2\2\2\4s\3\2\2\2\6\u0080\3\2\2\2\b\u0082\3\2\2\2")
        buf.write("\n\u008a\3\2\2\2\f\u0091\3\2\2\2\16\u0094\3\2\2\2\20\u009b")
        buf.write("\3\2\2\2\22\u009e\3\2\2\2\24\u00a5\3\2\2\2\26\u00a8\3")
        buf.write("\2\2\2\30\u00b1\3\2\2\2\32\u00b4\3\2\2\2\34\u00d2\3\2")
        buf.write("\2\2\36\u00d4\3\2\2\2 \"\5\4\3\2! \3\2\2\2\"%\3\2\2\2")
        buf.write("#!\3\2\2\2#$\3\2\2\2$\3\3\2\2\2%#\3\2\2\2&\'\7\25\2\2")
        buf.write("\'(\7$\2\2()\7\7\2\2)*\5\6\4\2*+\7\b\2\2+,\7\4\2\2,-\5")
        buf.write("\b\5\2-t\3\2\2\2.\60\7\13\2\2/\61\7\7\2\2\60/\3\2\2\2")
        buf.write("\60\61\3\2\2\2\61\62\3\2\2\2\62\64\5\n\6\2\63\65\7\b\2")
        buf.write("\2\64\63\3\2\2\2\64\65\3\2\2\2\65\66\3\2\2\2\66\67\7\4")
        buf.write("\2\2\67;\5\b\5\289\7\f\2\29:\7\4\2\2:<\5\b\5\2;8\3\2\2")
        buf.write("\2;<\3\2\2\2<t\3\2\2\2=?\7\21\2\2>@\7\7\2\2?>\3\2\2\2")
        buf.write("?@\3\2\2\2@A\3\2\2\2AC\5\n\6\2BD\7\b\2\2CB\3\2\2\2CD\3")
        buf.write("\2\2\2DE\3\2\2\2EF\7%\2\2Ft\3\2\2\2GH\7\22\2\2HI\7\7\2")
        buf.write("\2IJ\5\n\6\2JK\7\b\2\2KL\7%\2\2Lt\3\2\2\2MO\7\16\2\2N")
        buf.write("P\7\7\2\2ON\3\2\2\2OP\3\2\2\2PQ\3\2\2\2QS\5\n\6\2RT\7")
        buf.write("\b\2\2SR\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\7\4\2\2VW\5\b\5")
        buf.write("\2Wt\3\2\2\2XZ\7\20\2\2Y[\7\7\2\2ZY\3\2\2\2Z[\3\2\2\2")
        buf.write("[\\\3\2\2\2\\^\5\n\6\2]_\7\b\2\2^]\3\2\2\2^_\3\2\2\2_")
        buf.write("`\3\2\2\2`a\7\24\2\2ab\5\32\16\2bc\7\4\2\2cd\5\b\5\2d")
        buf.write("t\3\2\2\2ef\7$\2\2fg\7\t\2\2gh\5\n\6\2hi\7%\2\2it\3\2")
        buf.write("\2\2jk\5\34\17\2kl\7\7\2\2lm\5\32\16\2mn\7\b\2\2no\7%")
        buf.write("\2\2ot\3\2\2\2pq\5\32\16\2qr\7%\2\2rt\3\2\2\2s&\3\2\2")
        buf.write("\2s.\3\2\2\2s=\3\2\2\2sG\3\2\2\2sM\3\2\2\2sX\3\2\2\2s")
        buf.write("e\3\2\2\2sj\3\2\2\2sp\3\2\2\2t\5\3\2\2\2uw\7$\2\2vu\3")
        buf.write("\2\2\2vw\3\2\2\2w\u0081\3\2\2\2x}\7$\2\2yz\7\3\2\2z|\7")
        buf.write("$\2\2{y\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0081")
        buf.write("\3\2\2\2\177}\3\2\2\2\u0080v\3\2\2\2\u0080x\3\2\2\2\u0081")
        buf.write("\7\3\2\2\2\u0082\u0084\7(\2\2\u0083\u0085\5\4\3\2\u0084")
        buf.write("\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0084\3\2\2\2")
        buf.write("\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\7")
        buf.write(")\2\2\u0089\t\3\2\2\2\u008a\u008b\5\16\b\2\u008b\u008c")
        buf.write("\5\f\7\2\u008c\13\3\2\2\2\u008d\u008e\t\2\2\2\u008e\u0090")
        buf.write("\5\16\b\2\u008f\u008d\3\2\2\2\u0090\u0093\3\2\2\2\u0091")
        buf.write("\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\r\3\2\2\2\u0093")
        buf.write("\u0091\3\2\2\2\u0094\u0095\5\22\n\2\u0095\u0096\5\20\t")
        buf.write("\2\u0096\17\3\2\2\2\u0097\u0098\t\3\2\2\u0098\u009a\5")
        buf.write("\26\f\2\u0099\u0097\3\2\2\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\21\3\2\2\2\u009d")
        buf.write("\u009b\3\2\2\2\u009e\u009f\5\26\f\2\u009f\u00a0\5\24\13")
        buf.write("\2\u00a0\23\3\2\2\2\u00a1\u00a2\t\4\2\2\u00a2\u00a4\5")
        buf.write("\26\f\2\u00a3\u00a1\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5")
        buf.write("\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\25\3\2\2\2\u00a7")
        buf.write("\u00a5\3\2\2\2\u00a8\u00a9\5\34\17\2\u00a9\u00aa\5\30")
        buf.write("\r\2\u00aa\27\3\2\2\2\u00ab\u00ac\7\5\2\2\u00ac\u00ad")
        buf.write("\5\n\6\2\u00ad\u00ae\7\6\2\2\u00ae\u00b0\3\2\2\2\u00af")
        buf.write("\u00ab\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\31\3\2\2\2\u00b3\u00b1\3\2")
        buf.write("\2\2\u00b4\u00b9\5\n\6\2\u00b5\u00b6\7\3\2\2\u00b6\u00b8")
        buf.write("\5\n\6\2\u00b7\u00b5\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\33\3\2\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bc\u00d3\7#\2\2\u00bd\u00d3\7 \2\2\u00be")
        buf.write("\u00d3\7!\2\2\u00bf\u00d3\7\"\2\2\u00c0\u00c6\7$\2\2\u00c1")
        buf.write("\u00c3\7\7\2\2\u00c2\u00c4\5\32\16\2\u00c3\u00c2\3\2\2")
        buf.write("\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c7")
        buf.write("\7\b\2\2\u00c6\u00c1\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7")
        buf.write("\u00d3\3\2\2\2\u00c8\u00c9\7\7\2\2\u00c9\u00ca\5\n\6\2")
        buf.write("\u00ca\u00cb\7\b\2\2\u00cb\u00d3\3\2\2\2\u00cc\u00d3\5")
        buf.write("\36\20\2\u00cd\u00ce\7\23\2\2\u00ce\u00cf\7\7\2\2\u00cf")
        buf.write("\u00d0\5\n\6\2\u00d0\u00d1\7\b\2\2\u00d1\u00d3\3\2\2\2")
        buf.write("\u00d2\u00bc\3\2\2\2\u00d2\u00bd\3\2\2\2\u00d2\u00be\3")
        buf.write("\2\2\2\u00d2\u00bf\3\2\2\2\u00d2\u00c0\3\2\2\2\u00d2\u00c8")
        buf.write("\3\2\2\2\u00d2\u00cc\3\2\2\2\u00d2\u00cd\3\2\2\2\u00d3")
        buf.write("\35\3\2\2\2\u00d4\u00d5\7\5\2\2\u00d5\u00d6\5\32\16\2")
        buf.write("\u00d6\u00d7\7\6\2\2\u00d7\37\3\2\2\2\31#\60\64;?COSZ")
        buf.write("^sv}\u0080\u0086\u0091\u009b\u00a5\u00b1\u00b9\u00c3\u00c6")
        buf.write("\u00d2")
        return buf.getvalue()


class miParserParser ( Parser ):

    grammarFileName = "miParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "':'", "'['", "']'", "'('", "')'", 
                     "'='", "'\"'", "'if'", "'else'", "'elif'", "'while'", 
                     "'const'", "'for'", "'return'", "'print'", "'len'", 
                     "'in'", "'def'", "'+'", "'-'", "'*'", "'/'", "'//'", 
                     "'>'", "'<'", "'<='", "'>='", "'=='" ]

    symbolicNames = [ "<INVALID>", "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", 
                      "LEFTP", "RIGHTP", "ASSIGN", "DQUOTES", "IF", "ELSE", 
                      "ELIF", "WHILE", "CONST", "FOR", "RETURN", "PRINT", 
                      "LEN", "IN", "DEF", "ADD", "SUB", "MUL", "DIV", "INTDIV", 
                      "GT", "LT", "LET", "GET", "EQUAL", "FLOAT", "CHAR", 
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

    ruleNames =  [ "program", "statement", "argList", "sequence", "expression", 
                   "comparison", "additionExpression", "additionFactor", 
                   "multiplicationExpression", "multiplicationFactor", "elementExpression", 
                   "elementAccess", "expressionList", "primitiveExpression", 
                   "listExpression" ]

    EOF = Token.EOF
    COMMA=1
    COLON=2
    LEFTSQUARE=3
    RIGHTSQUARE=4
    LEFTP=5
    RIGHTP=6
    ASSIGN=7
    DQUOTES=8
    IF=9
    ELSE=10
    ELIF=11
    WHILE=12
    CONST=13
    FOR=14
    RETURN=15
    PRINT=16
    LEN=17
    IN=18
    DEF=19
    ADD=20
    SUB=21
    MUL=22
    DIV=23
    INTDIV=24
    GT=25
    LT=26
    LET=27
    GET=28
    EQUAL=29
    FLOAT=30
    CHAR=31
    STRING=32
    NUM=33
    ID=34
    NEWLINE=35
    WS=36
    SKIPP=37
    INDENT=38
    DEDENT=39

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




    def program(self):

        localctx = miParserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ProgramASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.IF) | (1 << miParserParser.WHILE) | (1 << miParserParser.FOR) | (1 << miParserParser.RETURN) | (1 << miParserParser.PRINT) | (1 << miParserParser.LEN) | (1 << miParserParser.DEF) | (1 << miParserParser.FLOAT) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0):
                self.state = 30
                self.statement()
                self.state = 35
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


    class ExpressionStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)

        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)


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



    def statement(self):

        localctx = miParserParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = miParserParser.DefStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(miParserParser.DEF)
                self.state = 37
                self.match(miParserParser.ID)
                self.state = 38
                self.match(miParserParser.LEFTP)
                self.state = 39
                self.argList()
                self.state = 40
                self.match(miParserParser.RIGHTP)
                self.state = 41
                self.match(miParserParser.COLON)
                self.state = 42
                self.sequence()
                pass

            elif la_ == 2:
                localctx = miParserParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(miParserParser.IF)
                self.state = 46
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 45
                    self.match(miParserParser.LEFTP)


                self.state = 48
                self.expression()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.RIGHTP:
                    self.state = 49
                    self.match(miParserParser.RIGHTP)


                self.state = 52
                self.match(miParserParser.COLON)
                self.state = 53
                self.sequence()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.ELSE:
                    self.state = 54
                    self.match(miParserParser.ELSE)
                    self.state = 55
                    self.match(miParserParser.COLON)
                    self.state = 56
                    self.sequence()


                pass

            elif la_ == 3:
                localctx = miParserParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.match(miParserParser.RETURN)
                self.state = 61
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 60
                    self.match(miParserParser.LEFTP)


                self.state = 63
                self.expression()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.RIGHTP:
                    self.state = 64
                    self.match(miParserParser.RIGHTP)


                self.state = 67
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = miParserParser.PrintStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.match(miParserParser.PRINT)
                self.state = 70
                self.match(miParserParser.LEFTP)
                self.state = 71
                self.expression()
                self.state = 72
                self.match(miParserParser.RIGHTP)
                self.state = 73
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 5:
                localctx = miParserParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.match(miParserParser.WHILE)
                self.state = 77
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 76
                    self.match(miParserParser.LEFTP)


                self.state = 79
                self.expression()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.RIGHTP:
                    self.state = 80
                    self.match(miParserParser.RIGHTP)


                self.state = 83
                self.match(miParserParser.COLON)
                self.state = 84
                self.sequence()
                pass

            elif la_ == 6:
                localctx = miParserParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 86
                self.match(miParserParser.FOR)
                self.state = 88
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 87
                    self.match(miParserParser.LEFTP)


                self.state = 90
                self.expression()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.RIGHTP:
                    self.state = 91
                    self.match(miParserParser.RIGHTP)


                self.state = 94
                self.match(miParserParser.IN)
                self.state = 95
                self.expressionList()
                self.state = 96
                self.match(miParserParser.COLON)
                self.state = 97
                self.sequence()
                pass

            elif la_ == 7:
                localctx = miParserParser.AssignStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 99
                self.match(miParserParser.ID)
                self.state = 100
                self.match(miParserParser.ASSIGN)
                self.state = 101
                self.expression()
                self.state = 102
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 8:
                localctx = miParserParser.FunctionCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 104
                self.primitiveExpression()
                self.state = 105
                self.match(miParserParser.LEFTP)
                self.state = 106
                self.expressionList()
                self.state = 107
                self.match(miParserParser.RIGHTP)
                self.state = 108
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 9:
                localctx = miParserParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 110
                self.expressionList()
                self.state = 111
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



    def argList(self):

        localctx = miParserParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = miParserParser.ArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.ID:
                    self.state = 115
                    self.match(miParserParser.ID)


                pass

            elif la_ == 2:
                localctx = miParserParser.ArgumentsListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(miParserParser.ID)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==miParserParser.COMMA:
                    self.state = 119
                    self.match(miParserParser.COMMA)
                    self.state = 120
                    self.match(miParserParser.ID)
                    self.state = 125
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




    def sequence(self):

        localctx = miParserParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sequence)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.SequenceASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(miParserParser.INDENT)
            self.state = 130 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 129
                self.statement()
                self.state = 132 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.IF) | (1 << miParserParser.WHILE) | (1 << miParserParser.FOR) | (1 << miParserParser.RETURN) | (1 << miParserParser.PRINT) | (1 << miParserParser.LEN) | (1 << miParserParser.DEF) | (1 << miParserParser.FLOAT) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0)):
                    break

            self.state = 134
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




    def expression(self):

        localctx = miParserParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            localctx = miParserParser.ExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.additionExpression()
            self.state = 137
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



    def comparison(self):

        localctx = miParserParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ComparisonASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.GT) | (1 << miParserParser.LT) | (1 << miParserParser.LET) | (1 << miParserParser.GET) | (1 << miParserParser.EQUAL))) != 0):
                self.state = 139
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.GT) | (1 << miParserParser.LT) | (1 << miParserParser.LET) | (1 << miParserParser.GET) | (1 << miParserParser.EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 140
                self.additionExpression()
                self.state = 145
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




    def additionExpression(self):

        localctx = miParserParser.AdditionExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_additionExpression)
        try:
            localctx = miParserParser.AditionalExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.multiplicationExpression()
            self.state = 147
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



    def additionFactor(self):

        localctx = miParserParser.AdditionFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_additionFactor)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.AddFactorContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.ADD or _la==miParserParser.SUB:
                self.state = 149
                _la = self._input.LA(1)
                if not(_la==miParserParser.ADD or _la==miParserParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 150
                self.elementExpression()
                self.state = 155
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




    def multiplicationExpression(self):

        localctx = miParserParser.MultiplicationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_multiplicationExpression)
        try:
            localctx = miParserParser.MultiplicationExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.elementExpression()
            self.state = 157
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



    def multiplicationFactor(self):

        localctx = miParserParser.MultiplicationFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_multiplicationFactor)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.MulFactorContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.MUL or _la==miParserParser.DIV:
                self.state = 159
                _la = self._input.LA(1)
                if not(_la==miParserParser.MUL or _la==miParserParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 160
                self.elementExpression()
                self.state = 165
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




    def elementExpression(self):

        localctx = miParserParser.ElementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elementExpression)
        try:
            localctx = miParserParser.ElementExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.primitiveExpression()
            self.state = 167
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



    def elementAccess(self):

        localctx = miParserParser.ElementAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_elementAccess)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ElementAccessASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.LEFTSQUARE:
                self.state = 169
                self.match(miParserParser.LEFTSQUARE)
                self.state = 170
                self.expression()
                self.state = 171
                self.match(miParserParser.RIGHTSQUARE)
                self.state = 177
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



    def expressionList(self):

        localctx = miParserParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ExpressionListASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.expression()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.COMMA:
                self.state = 179
                self.match(miParserParser.COMMA)
                self.state = 180
                self.expression()
                self.state = 185
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


    class ListExPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def listExpression(self):
            return self.getTypedRuleContext(miParserParser.ListExpressionContext,0)



    class IntegerPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(miParserParser.NUM, 0)


    class StringPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(miParserParser.STRING, 0)


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


    class CharPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(miParserParser.CHAR, 0)


    class IdentifierPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(miParserParser.ID, 0)
        def LEFTP(self):
            return self.getToken(miParserParser.LEFTP, 0)
        def RIGHTP(self):
            return self.getToken(miParserParser.RIGHTP, 0)
        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)




    def primitiveExpression(self):

        localctx = miParserParser.PrimitiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_primitiveExpression)
        self._la = 0 # Token type
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miParserParser.NUM]:
                localctx = miParserParser.IntegerPEContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(miParserParser.NUM)
                pass
            elif token in [miParserParser.FLOAT]:
                localctx = miParserParser.FloatPEContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(miParserParser.FLOAT)
                pass
            elif token in [miParserParser.CHAR]:
                localctx = miParserParser.CharPEContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.match(miParserParser.CHAR)
                pass
            elif token in [miParserParser.STRING]:
                localctx = miParserParser.StringPEContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.match(miParserParser.STRING)
                pass
            elif token in [miParserParser.ID]:
                localctx = miParserParser.IdentifierPEContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 190
                self.match(miParserParser.ID)
                self.state = 196
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 191
                    self.match(miParserParser.LEFTP)
                    self.state = 193
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.LEN) | (1 << miParserParser.FLOAT) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0):
                        self.state = 192
                        self.expressionList()


                    self.state = 195
                    self.match(miParserParser.RIGHTP)


                pass
            elif token in [miParserParser.LEFTP]:
                localctx = miParserParser.ExpressPEContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 198
                self.match(miParserParser.LEFTP)
                self.state = 199
                self.expression()
                self.state = 200
                self.match(miParserParser.RIGHTP)
                pass
            elif token in [miParserParser.LEFTSQUARE]:
                localctx = miParserParser.ListExPEContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 202
                self.listExpression()
                pass
            elif token in [miParserParser.LEN]:
                localctx = miParserParser.LenPEContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 203
                self.match(miParserParser.LEN)
                self.state = 204
                self.match(miParserParser.LEFTP)
                self.state = 205
                self.expression()
                self.state = 206
                self.match(miParserParser.RIGHTP)
                pass
            else:
                raise NoViableAltException(self)

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



    def listExpression(self):

        localctx = miParserParser.ListExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listExpression)
        try:
            localctx = miParserParser.ListExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(miParserParser.LEFTSQUARE)
            self.state = 211
            self.expressionList()
            self.state = 212
            self.match(miParserParser.RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





