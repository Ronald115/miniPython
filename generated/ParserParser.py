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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3*")
        buf.write("\u00b6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\7\2\"\n\2\f\2\16\2%\13\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3Y\n\3\3\4\3")
        buf.write("\4\3\4\3\4\7\4_\n\4\f\4\16\4b\13\4\5\4d\n\4\3\5\3\5\7")
        buf.write("\5h\n\5\f\5\16\5k\13\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\7\7")
        buf.write("t\n\7\f\7\16\7w\13\7\3\b\3\b\3\b\3\t\3\t\7\t~\n\t\f\t")
        buf.write("\16\t\u0081\13\t\3\n\3\n\3\n\3\13\3\13\7\13\u0088\n\13")
        buf.write("\f\13\16\13\u008b\13\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\7")
        buf.write("\r\u0094\n\r\f\r\16\r\u0097\13\r\3\16\3\16\3\16\7\16\u009c")
        buf.write("\n\16\f\16\16\16\u009f\13\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17")
        buf.write("\u00b0\n\17\3\20\3\20\3\20\3\20\3\20\2\2\21\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36\2\6\3\2\36\"\3\2\31\32\3")
        buf.write("\2\33\34\4\2\3\6$$\2\u00ba\2#\3\2\2\2\4X\3\2\2\2\6c\3")
        buf.write("\2\2\2\be\3\2\2\2\nn\3\2\2\2\fu\3\2\2\2\16x\3\2\2\2\20")
        buf.write("\177\3\2\2\2\22\u0082\3\2\2\2\24\u0089\3\2\2\2\26\u008c")
        buf.write("\3\2\2\2\30\u0095\3\2\2\2\32\u0098\3\2\2\2\34\u00a0\3")
        buf.write("\2\2\2\36\u00b1\3\2\2\2 \"\5\4\3\2! \3\2\2\2\"%\3\2\2")
        buf.write("\2#!\3\2\2\2#$\3\2\2\2$\3\3\2\2\2%#\3\2\2\2&\'\7\30\2")
        buf.write("\2\'(\7$\2\2()\7\13\2\2)*\5\6\4\2*+\7\f\2\2+,\7\b\2\2")
        buf.write(",-\5\b\5\2-Y\3\2\2\2./\7\16\2\2/\60\5\n\6\2\60\61\7\b")
        buf.write("\2\2\61\62\5\b\5\2\62\63\7\17\2\2\63\64\7\b\2\2\64\65")
        buf.write("\5\b\5\2\65Y\3\2\2\2\66\67\7\24\2\2\678\5\n\6\289\7%\2")
        buf.write("\29Y\3\2\2\2:;\7\25\2\2;<\5\n\6\2<=\7%\2\2=Y\3\2\2\2>")
        buf.write("?\7\21\2\2?@\5\n\6\2@A\7\b\2\2AB\5\b\5\2BY\3\2\2\2CD\7")
        buf.write("\23\2\2DE\5\n\6\2EF\7\27\2\2FG\5\32\16\2GH\7\b\2\2HI\5")
        buf.write("\b\5\2IY\3\2\2\2JK\7$\2\2KL\7\r\2\2LM\5\n\6\2MN\7%\2\2")
        buf.write("NY\3\2\2\2OP\5\34\17\2PQ\7\13\2\2QR\5\32\16\2RS\7\f\2")
        buf.write("\2ST\7%\2\2TY\3\2\2\2UV\5\32\16\2VW\7%\2\2WY\3\2\2\2X")
        buf.write("&\3\2\2\2X.\3\2\2\2X\66\3\2\2\2X:\3\2\2\2X>\3\2\2\2XC")
        buf.write("\3\2\2\2XJ\3\2\2\2XO\3\2\2\2XU\3\2\2\2Y\5\3\2\2\2Zd\7")
        buf.write("$\2\2[`\7$\2\2\\]\7\7\2\2]_\7$\2\2^\\\3\2\2\2_b\3\2\2")
        buf.write("\2`^\3\2\2\2`a\3\2\2\2ad\3\2\2\2b`\3\2\2\2cZ\3\2\2\2c")
        buf.write("[\3\2\2\2d\7\3\2\2\2ei\7)\2\2fh\5\4\3\2gf\3\2\2\2hk\3")
        buf.write("\2\2\2ig\3\2\2\2ij\3\2\2\2jl\3\2\2\2ki\3\2\2\2lm\7*\2")
        buf.write("\2m\t\3\2\2\2no\5\16\b\2op\5\f\7\2p\13\3\2\2\2qr\t\2\2")
        buf.write("\2rt\5\16\b\2sq\3\2\2\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2")
        buf.write("v\r\3\2\2\2wu\3\2\2\2xy\5\22\n\2yz\5\20\t\2z\17\3\2\2")
        buf.write("\2{|\t\3\2\2|~\5\26\f\2}{\3\2\2\2~\u0081\3\2\2\2\177}")
        buf.write("\3\2\2\2\177\u0080\3\2\2\2\u0080\21\3\2\2\2\u0081\177")
        buf.write("\3\2\2\2\u0082\u0083\5\26\f\2\u0083\u0084\5\24\13\2\u0084")
        buf.write("\23\3\2\2\2\u0085\u0086\t\4\2\2\u0086\u0088\5\26\f\2\u0087")
        buf.write("\u0085\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u0087\3\2\2\2")
        buf.write("\u0089\u008a\3\2\2\2\u008a\25\3\2\2\2\u008b\u0089\3\2")
        buf.write("\2\2\u008c\u008d\5\34\17\2\u008d\u008e\5\30\r\2\u008e")
        buf.write("\27\3\2\2\2\u008f\u0090\7\t\2\2\u0090\u0091\5\n\6\2\u0091")
        buf.write("\u0092\7\n\2\2\u0092\u0094\3\2\2\2\u0093\u008f\3\2\2\2")
        buf.write("\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3")
        buf.write("\2\2\2\u0096\31\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u009d")
        buf.write("\5\n\6\2\u0099\u009a\7\7\2\2\u009a\u009c\5\n\6\2\u009b")
        buf.write("\u0099\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009d\u009e\3\2\2\2\u009e\33\3\2\2\2\u009f\u009d\3\2")
        buf.write("\2\2\u00a0\u00af\t\5\2\2\u00a1\u00a2\7\13\2\2\u00a2\u00a3")
        buf.write("\5\32\16\2\u00a3\u00a4\7\f\2\2\u00a4\u00b0\3\2\2\2\u00a5")
        buf.write("\u00a6\7\13\2\2\u00a6\u00a7\5\n\6\2\u00a7\u00a8\7\f\2")
        buf.write("\2\u00a8\u00b0\3\2\2\2\u00a9\u00b0\5\36\20\2\u00aa\u00ab")
        buf.write("\7\26\2\2\u00ab\u00ac\7\13\2\2\u00ac\u00ad\5\n\6\2\u00ad")
        buf.write("\u00ae\7\f\2\2\u00ae\u00b0\3\2\2\2\u00af\u00a1\3\2\2\2")
        buf.write("\u00af\u00a5\3\2\2\2\u00af\u00a9\3\2\2\2\u00af\u00aa\3")
        buf.write("\2\2\2\u00b0\35\3\2\2\2\u00b1\u00b2\7\t\2\2\u00b2\u00b3")
        buf.write("\5\32\16\2\u00b3\u00b4\7\n\2\2\u00b4\37\3\2\2\2\r#X`c")
        buf.write("iu\177\u0089\u0095\u009d\u00af")
        return buf.getvalue()


class ParserParser ( Parser ):

    grammarFileName = "Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'char'", "'String'", 
                     "','", "':'", "'['", "']'", "'('", "')'", "'='", "'if'", 
                     "'else'", "'elif'", "'while'", "'const'", "'for'", 
                     "'return'", "'print'", "'len'", "'in'", "'def'", "'+'", 
                     "'-'", "'*'", "'/'", "'//'", "'>'", "'<'", "'<='", 
                     "'>='", "'=='" ]

    symbolicNames = [ "<INVALID>", "INTEGER", "FLOAT", "CHARCONST", "STRING", 
                      "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", "LEFTP", 
                      "RIGHTP", "ASSIGN", "IF", "ELSE", "ELIF", "WHILE", 
                      "CONST", "FOR", "RETURN", "PRINT", "LEN", "IN", "DEF", 
                      "ADD", "SUB", "MUL", "DIV", "INTDIV", "GT", "LT", 
                      "LET", "GET", "EQUAL", "NUM", "ID", "NEWLINE", "WS", 
                      "COMMENT", "LINECOMMENT", "INDENT", "DEDENT" ]

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
    INTEGER=1
    FLOAT=2
    CHARCONST=3
    STRING=4
    COMMA=5
    COLON=6
    LEFTSQUARE=7
    RIGHTSQUARE=8
    LEFTP=9
    RIGHTP=10
    ASSIGN=11
    IF=12
    ELSE=13
    ELIF=14
    WHILE=15
    CONST=16
    FOR=17
    RETURN=18
    PRINT=19
    LEN=20
    IN=21
    DEF=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    INTDIV=27
    GT=28
    LT=29
    LET=30
    GET=31
    EQUAL=32
    NUM=33
    ID=34
    NEWLINE=35
    WS=36
    COMMENT=37
    LINECOMMENT=38
    INDENT=39
    DEDENT=40

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
            return ParserParser.RULE_program

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramASTContext(ProgramContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ProgramContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(ParserParser.StatementContext,i)




    def program(self):

        localctx = ParserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            localctx = ParserParser.ProgramASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParserParser.INTEGER) | (1 << ParserParser.FLOAT) | (1 << ParserParser.CHARCONST) | (1 << ParserParser.STRING) | (1 << ParserParser.IF) | (1 << ParserParser.WHILE) | (1 << ParserParser.FOR) | (1 << ParserParser.RETURN) | (1 << ParserParser.PRINT) | (1 << ParserParser.DEF) | (1 << ParserParser.ID))) != 0):
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
            return ParserParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(ParserParser.WHILE, 0)
        def expression(self):
            return self.getTypedRuleContext(ParserParser.ExpressionContext,0)

        def COLON(self):
            return self.getToken(ParserParser.COLON, 0)
        def sequence(self):
            return self.getTypedRuleContext(ParserParser.SequenceContext,0)



    class DefStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEF(self):
            return self.getToken(ParserParser.DEF, 0)
        def ID(self):
            return self.getToken(ParserParser.ID, 0)
        def LEFTP(self):
            return self.getToken(ParserParser.LEFTP, 0)
        def argList(self):
            return self.getTypedRuleContext(ParserParser.ArgListContext,0)

        def RIGHTP(self):
            return self.getToken(ParserParser.RIGHTP, 0)
        def COLON(self):
            return self.getToken(ParserParser.COLON, 0)
        def sequence(self):
            return self.getTypedRuleContext(ParserParser.SequenceContext,0)



    class PrintStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(ParserParser.PRINT, 0)
        def expression(self):
            return self.getTypedRuleContext(ParserParser.ExpressionContext,0)

        def NEWLINE(self):
            return self.getToken(ParserParser.NEWLINE, 0)


    class ForStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(ParserParser.FOR, 0)
        def expression(self):
            return self.getTypedRuleContext(ParserParser.ExpressionContext,0)

        def IN(self):
            return self.getToken(ParserParser.IN, 0)
        def expressionList(self):
            return self.getTypedRuleContext(ParserParser.ExpressionListContext,0)

        def COLON(self):
            return self.getToken(ParserParser.COLON, 0)
        def sequence(self):
            return self.getTypedRuleContext(ParserParser.SequenceContext,0)



    class AssignStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ParserParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(ParserParser.ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(ParserParser.ExpressionContext,0)

        def NEWLINE(self):
            return self.getToken(ParserParser.NEWLINE, 0)


    class FunctionCallStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primitiveExpression(self):
            return self.getTypedRuleContext(ParserParser.PrimitiveExpressionContext,0)

        def LEFTP(self):
            return self.getToken(ParserParser.LEFTP, 0)
        def expressionList(self):
            return self.getTypedRuleContext(ParserParser.ExpressionListContext,0)

        def RIGHTP(self):
            return self.getToken(ParserParser.RIGHTP, 0)
        def NEWLINE(self):
            return self.getToken(ParserParser.NEWLINE, 0)


    class ExpressionStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressionList(self):
            return self.getTypedRuleContext(ParserParser.ExpressionListContext,0)

        def NEWLINE(self):
            return self.getToken(ParserParser.NEWLINE, 0)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ParserParser.IF, 0)
        def expression(self):
            return self.getTypedRuleContext(ParserParser.ExpressionContext,0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.COLON)
            else:
                return self.getToken(ParserParser.COLON, i)
        def sequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.SequenceContext)
            else:
                return self.getTypedRuleContext(ParserParser.SequenceContext,i)

        def ELSE(self):
            return self.getToken(ParserParser.ELSE, 0)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(ParserParser.RETURN, 0)
        def expression(self):
            return self.getTypedRuleContext(ParserParser.ExpressionContext,0)

        def NEWLINE(self):
            return self.getToken(ParserParser.NEWLINE, 0)



    def statement(self):

        localctx = ParserParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = ParserParser.DefStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(ParserParser.DEF)
                self.state = 37
                self.match(ParserParser.ID)
                self.state = 38
                self.match(ParserParser.LEFTP)
                self.state = 39
                self.argList()
                self.state = 40
                self.match(ParserParser.RIGHTP)
                self.state = 41
                self.match(ParserParser.COLON)
                self.state = 42
                self.sequence()
                pass

            elif la_ == 2:
                localctx = ParserParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(ParserParser.IF)
                self.state = 45
                self.expression()
                self.state = 46
                self.match(ParserParser.COLON)
                self.state = 47
                self.sequence()
                self.state = 48
                self.match(ParserParser.ELSE)
                self.state = 49
                self.match(ParserParser.COLON)
                self.state = 50
                self.sequence()
                pass

            elif la_ == 3:
                localctx = ParserParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.match(ParserParser.RETURN)
                self.state = 53
                self.expression()
                self.state = 54
                self.match(ParserParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = ParserParser.PrintStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.match(ParserParser.PRINT)
                self.state = 57
                self.expression()
                self.state = 58
                self.match(ParserParser.NEWLINE)
                pass

            elif la_ == 5:
                localctx = ParserParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.match(ParserParser.WHILE)
                self.state = 61
                self.expression()
                self.state = 62
                self.match(ParserParser.COLON)
                self.state = 63
                self.sequence()
                pass

            elif la_ == 6:
                localctx = ParserParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.match(ParserParser.FOR)
                self.state = 66
                self.expression()
                self.state = 67
                self.match(ParserParser.IN)
                self.state = 68
                self.expressionList()
                self.state = 69
                self.match(ParserParser.COLON)
                self.state = 70
                self.sequence()
                pass

            elif la_ == 7:
                localctx = ParserParser.AssignStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 72
                self.match(ParserParser.ID)
                self.state = 73
                self.match(ParserParser.ASSIGN)
                self.state = 74
                self.expression()
                self.state = 75
                self.match(ParserParser.NEWLINE)
                pass

            elif la_ == 8:
                localctx = ParserParser.FunctionCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 77
                self.primitiveExpression()
                self.state = 78
                self.match(ParserParser.LEFTP)
                self.state = 79
                self.expressionList()
                self.state = 80
                self.match(ParserParser.RIGHTP)
                self.state = 81
                self.match(ParserParser.NEWLINE)
                pass

            elif la_ == 9:
                localctx = ParserParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 83
                self.expressionList()
                self.state = 84
                self.match(ParserParser.NEWLINE)
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
            return ParserParser.RULE_argList

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArgumentContext(ArgListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ArgListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ParserParser.ID, 0)


    class ArgumentsListContext(ArgListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ArgListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.ID)
            else:
                return self.getToken(ParserParser.ID, i)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.COMMA)
            else:
                return self.getToken(ParserParser.COMMA, i)



    def argList(self):

        localctx = ParserParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = ParserParser.ArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(ParserParser.ID)
                pass

            elif la_ == 2:
                localctx = ParserParser.ArgumentsListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.match(ParserParser.ID)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ParserParser.COMMA:
                    self.state = 90
                    self.match(ParserParser.COMMA)
                    self.state = 91
                    self.match(ParserParser.ID)
                    self.state = 96
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
            return ParserParser.RULE_sequence

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SequenceASTContext(SequenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.SequenceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INDENT(self):
            return self.getToken(ParserParser.INDENT, 0)
        def DEDENT(self):
            return self.getToken(ParserParser.DEDENT, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(ParserParser.StatementContext,i)




    def sequence(self):

        localctx = ParserParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sequence)
        self._la = 0 # Token type
        try:
            localctx = ParserParser.SequenceASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(ParserParser.INDENT)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParserParser.INTEGER) | (1 << ParserParser.FLOAT) | (1 << ParserParser.CHARCONST) | (1 << ParserParser.STRING) | (1 << ParserParser.IF) | (1 << ParserParser.WHILE) | (1 << ParserParser.FOR) | (1 << ParserParser.RETURN) | (1 << ParserParser.PRINT) | (1 << ParserParser.DEF) | (1 << ParserParser.ID))) != 0):
                self.state = 100
                self.statement()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(ParserParser.DEDENT)
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
            return ParserParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionASTContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def additionExpression(self):
            return self.getTypedRuleContext(ParserParser.AdditionExpressionContext,0)

        def comparison(self):
            return self.getTypedRuleContext(ParserParser.ComparisonContext,0)




    def expression(self):

        localctx = ParserParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            localctx = ParserParser.ExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.additionExpression()
            self.state = 109
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
            return ParserParser.RULE_comparison

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComparisonASTContext(ComparisonContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ComparisonContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def additionExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.AdditionExpressionContext)
            else:
                return self.getTypedRuleContext(ParserParser.AdditionExpressionContext,i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.LT)
            else:
                return self.getToken(ParserParser.LT, i)
        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.GT)
            else:
                return self.getToken(ParserParser.GT, i)
        def LET(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.LET)
            else:
                return self.getToken(ParserParser.LET, i)
        def GET(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.GET)
            else:
                return self.getToken(ParserParser.GET, i)
        def EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.EQUAL)
            else:
                return self.getToken(ParserParser.EQUAL, i)



    def comparison(self):

        localctx = ParserParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            localctx = ParserParser.ComparisonASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParserParser.GT) | (1 << ParserParser.LT) | (1 << ParserParser.LET) | (1 << ParserParser.GET) | (1 << ParserParser.EQUAL))) != 0):
                self.state = 111
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParserParser.GT) | (1 << ParserParser.LT) | (1 << ParserParser.LET) | (1 << ParserParser.GET) | (1 << ParserParser.EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 112
                self.additionExpression()
                self.state = 117
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
            return ParserParser.RULE_additionExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AditionalExpressionASTContext(AdditionExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.AdditionExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multiplicationExpression(self):
            return self.getTypedRuleContext(ParserParser.MultiplicationExpressionContext,0)

        def additionFactor(self):
            return self.getTypedRuleContext(ParserParser.AdditionFactorContext,0)




    def additionExpression(self):

        localctx = ParserParser.AdditionExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_additionExpression)
        try:
            localctx = ParserParser.AditionalExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.multiplicationExpression()
            self.state = 119
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
            return ParserParser.RULE_additionFactor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddFactorContext(AdditionFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.AdditionFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def elementExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ElementExpressionContext)
            else:
                return self.getTypedRuleContext(ParserParser.ElementExpressionContext,i)

        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.ADD)
            else:
                return self.getToken(ParserParser.ADD, i)
        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.SUB)
            else:
                return self.getToken(ParserParser.SUB, i)



    def additionFactor(self):

        localctx = ParserParser.AdditionFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_additionFactor)
        self._la = 0 # Token type
        try:
            localctx = ParserParser.AddFactorContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ParserParser.ADD or _la==ParserParser.SUB:
                self.state = 121
                _la = self._input.LA(1)
                if not(_la==ParserParser.ADD or _la==ParserParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 122
                self.elementExpression()
                self.state = 127
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
            return ParserParser.RULE_multiplicationExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MultiplicationExpressionASTContext(MultiplicationExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.MultiplicationExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def elementExpression(self):
            return self.getTypedRuleContext(ParserParser.ElementExpressionContext,0)

        def multiplicationFactor(self):
            return self.getTypedRuleContext(ParserParser.MultiplicationFactorContext,0)




    def multiplicationExpression(self):

        localctx = ParserParser.MultiplicationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_multiplicationExpression)
        try:
            localctx = ParserParser.MultiplicationExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.elementExpression()
            self.state = 129
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
            return ParserParser.RULE_multiplicationFactor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MulFactorContext(MultiplicationFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.MultiplicationFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def elementExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ElementExpressionContext)
            else:
                return self.getTypedRuleContext(ParserParser.ElementExpressionContext,i)

        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.MUL)
            else:
                return self.getToken(ParserParser.MUL, i)
        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.DIV)
            else:
                return self.getToken(ParserParser.DIV, i)



    def multiplicationFactor(self):

        localctx = ParserParser.MultiplicationFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_multiplicationFactor)
        self._la = 0 # Token type
        try:
            localctx = ParserParser.MulFactorContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ParserParser.MUL or _la==ParserParser.DIV:
                self.state = 131
                _la = self._input.LA(1)
                if not(_la==ParserParser.MUL or _la==ParserParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 132
                self.elementExpression()
                self.state = 137
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
            return ParserParser.RULE_elementExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ElementExpressionASTContext(ElementExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ElementExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primitiveExpression(self):
            return self.getTypedRuleContext(ParserParser.PrimitiveExpressionContext,0)

        def elementAccess(self):
            return self.getTypedRuleContext(ParserParser.ElementAccessContext,0)




    def elementExpression(self):

        localctx = ParserParser.ElementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elementExpression)
        try:
            localctx = ParserParser.ElementExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.primitiveExpression()
            self.state = 139
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
            return ParserParser.RULE_elementAccess

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ElementAccessASTContext(ElementAccessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ElementAccessContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFTSQUARE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.LEFTSQUARE)
            else:
                return self.getToken(ParserParser.LEFTSQUARE, i)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExpressionContext,i)

        def RIGHTSQUARE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.RIGHTSQUARE)
            else:
                return self.getToken(ParserParser.RIGHTSQUARE, i)



    def elementAccess(self):

        localctx = ParserParser.ElementAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_elementAccess)
        self._la = 0 # Token type
        try:
            localctx = ParserParser.ElementAccessASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ParserParser.LEFTSQUARE:
                self.state = 141
                self.match(ParserParser.LEFTSQUARE)
                self.state = 142
                self.expression()
                self.state = 143
                self.match(ParserParser.RIGHTSQUARE)
                self.state = 149
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
            return ParserParser.RULE_expressionList

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionListASTContext(ExpressionListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ExpressionListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ParserParser.ExpressionContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserParser.COMMA)
            else:
                return self.getToken(ParserParser.COMMA, i)



    def expressionList(self):

        localctx = ParserParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            localctx = ParserParser.ExpressionListASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.expression()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ParserParser.COMMA:
                self.state = 151
                self.match(ParserParser.COMMA)
                self.state = 152
                self.expression()
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


    class PrimitiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ParserParser.RULE_primitiveExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrimitiveExpressionASTContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(ParserParser.INTEGER, 0)
        def FLOAT(self):
            return self.getToken(ParserParser.FLOAT, 0)
        def CHARCONST(self):
            return self.getToken(ParserParser.CHARCONST, 0)
        def STRING(self):
            return self.getToken(ParserParser.STRING, 0)
        def ID(self):
            return self.getToken(ParserParser.ID, 0)
        def LEFTP(self):
            return self.getToken(ParserParser.LEFTP, 0)
        def expressionList(self):
            return self.getTypedRuleContext(ParserParser.ExpressionListContext,0)

        def RIGHTP(self):
            return self.getToken(ParserParser.RIGHTP, 0)
        def expression(self):
            return self.getTypedRuleContext(ParserParser.ExpressionContext,0)

        def listExpression(self):
            return self.getTypedRuleContext(ParserParser.ListExpressionContext,0)

        def LEN(self):
            return self.getToken(ParserParser.LEN, 0)



    def primitiveExpression(self):

        localctx = ParserParser.PrimitiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_primitiveExpression)
        self._la = 0 # Token type
        try:
            localctx = ParserParser.PrimitiveExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParserParser.INTEGER) | (1 << ParserParser.FLOAT) | (1 << ParserParser.CHARCONST) | (1 << ParserParser.STRING) | (1 << ParserParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 159
                self.match(ParserParser.LEFTP)
                self.state = 160
                self.expressionList()
                self.state = 161
                self.match(ParserParser.RIGHTP)
                pass

            elif la_ == 2:
                self.state = 163
                self.match(ParserParser.LEFTP)
                self.state = 164
                self.expression()
                self.state = 165
                self.match(ParserParser.RIGHTP)
                pass

            elif la_ == 3:
                self.state = 167
                self.listExpression()
                pass

            elif la_ == 4:
                self.state = 168
                self.match(ParserParser.LEN)
                self.state = 169
                self.match(ParserParser.LEFTP)
                self.state = 170
                self.expression()
                self.state = 171
                self.match(ParserParser.RIGHTP)
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
            return ParserParser.RULE_listExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ListExpressionASTContext(ListExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserParser.ListExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFTSQUARE(self):
            return self.getToken(ParserParser.LEFTSQUARE, 0)
        def expressionList(self):
            return self.getTypedRuleContext(ParserParser.ExpressionListContext,0)

        def RIGHTSQUARE(self):
            return self.getToken(ParserParser.RIGHTSQUARE, 0)



    def listExpression(self):

        localctx = ParserParser.ListExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listExpression)
        try:
            localctx = ParserParser.ListExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(ParserParser.LEFTSQUARE)
            self.state = 176
            self.expressionList()
            self.state = 177
            self.match(ParserParser.RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





