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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\u00f4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\7\2")
        buf.write("&\n\2\f\2\16\2)\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3\65\n\3\3\3\3\3\5\39\n\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3@\n\3\3\3\3\3\5\3D\n\3\3\3\3\3\5\3H\n\3\5\3J\n\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3U\n\3\3\3\3\3\5")
        buf.write("\3Y\n\3\3\3\3\3\3\3\3\3\3\3\5\3`\n\3\3\3\3\3\5\3d\n\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3t\n\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3|\n\3\3\4\5\4\177")
        buf.write("\n\4\3\4\3\4\3\4\7\4\u0084\n\4\f\4\16\4\u0087\13\4\5\4")
        buf.write("\u0089\n\4\3\5\3\5\6\5\u008d\n\5\r\5\16\5\u008e\3\5\3")
        buf.write("\5\3\6\3\6\6\6\u0095\n\6\r\6\16\6\u0096\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\b\3\b\7\b\u00a0\n\b\f\b\16\b\u00a3\13\b\3\t\3")
        buf.write("\t\3\t\3\n\3\n\7\n\u00aa\n\n\f\n\16\n\u00ad\13\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\7\f\u00b4\n\f\f\f\16\f\u00b7\13\f\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\7\16\u00c0\n\16\f\16\16")
        buf.write("\16\u00c3\13\16\3\17\3\17\3\17\7\17\u00c8\n\17\f\17\16")
        buf.write("\17\u00cb\13\17\3\20\5\20\u00ce\n\20\3\20\3\20\5\20\u00d2")
        buf.write("\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00dc")
        buf.write("\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00ea\n\20\3\21\3\21\5\21\u00ee\n\21\3")
        buf.write("\21\3\21\3\22\3\22\3\22\2\2\23\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"\2\5\3\2\35\"\3\2\30\31\3\2\32\33\2")
        buf.write("\u010d\2\'\3\2\2\2\4{\3\2\2\2\6\u0088\3\2\2\2\b\u008a")
        buf.write("\3\2\2\2\n\u0092\3\2\2\2\f\u009a\3\2\2\2\16\u00a1\3\2")
        buf.write("\2\2\20\u00a4\3\2\2\2\22\u00ab\3\2\2\2\24\u00ae\3\2\2")
        buf.write("\2\26\u00b5\3\2\2\2\30\u00b8\3\2\2\2\32\u00c1\3\2\2\2")
        buf.write("\34\u00c4\3\2\2\2\36\u00e9\3\2\2\2 \u00eb\3\2\2\2\"\u00f1")
        buf.write("\3\2\2\2$&\5\4\3\2%$\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3")
        buf.write("\2\2\2(\3\3\2\2\2)\'\3\2\2\2*+\7\27\2\2+,\7+\2\2,-\7\7")
        buf.write("\2\2-.\5\6\4\2./\7\b\2\2/\60\7\4\2\2\60\61\5\b\5\2\61")
        buf.write("|\3\2\2\2\62\64\7\r\2\2\63\65\7\7\2\2\64\63\3\2\2\2\64")
        buf.write("\65\3\2\2\2\65\66\3\2\2\2\668\5\f\7\2\679\7\b\2\28\67")
        buf.write("\3\2\2\289\3\2\2\29:\3\2\2\2:;\7\4\2\2;?\5\b\5\2<=\7\16")
        buf.write("\2\2=>\7\4\2\2>@\5\n\6\2?<\3\2\2\2?@\3\2\2\2@|\3\2\2\2")
        buf.write("AI\7\23\2\2BD\7\7\2\2CB\3\2\2\2CD\3\2\2\2DE\3\2\2\2EG")
        buf.write("\5\f\7\2FH\7\b\2\2GF\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IC\3\2")
        buf.write("\2\2IJ\3\2\2\2JK\3\2\2\2K|\7,\2\2LM\7\24\2\2MN\7\7\2\2")
        buf.write("NO\5\f\7\2OP\7\b\2\2PQ\7,\2\2Q|\3\2\2\2RT\7\20\2\2SU\7")
        buf.write("\7\2\2TS\3\2\2\2TU\3\2\2\2UV\3\2\2\2VX\5\f\7\2WY\7\b\2")
        buf.write("\2XW\3\2\2\2XY\3\2\2\2YZ\3\2\2\2Z[\7\4\2\2[\\\5\b\5\2")
        buf.write("\\|\3\2\2\2]_\7\22\2\2^`\7\7\2\2_^\3\2\2\2_`\3\2\2\2`")
        buf.write("a\3\2\2\2ac\5\f\7\2bd\7\b\2\2cb\3\2\2\2cd\3\2\2\2de\3")
        buf.write("\2\2\2ef\7\26\2\2fg\5\34\17\2gh\7\4\2\2hi\5\b\5\2i|\3")
        buf.write("\2\2\2jk\7+\2\2kl\5\32\16\2lm\7\t\2\2mn\5\f\7\2no\7,\2")
        buf.write("\2o|\3\2\2\2pq\5\36\20\2qs\7\7\2\2rt\5\34\17\2sr\3\2\2")
        buf.write("\2st\3\2\2\2tu\3\2\2\2uv\7\b\2\2vw\7,\2\2w|\3\2\2\2xy")
        buf.write("\5\34\17\2yz\7,\2\2z|\3\2\2\2{*\3\2\2\2{\62\3\2\2\2{A")
        buf.write("\3\2\2\2{L\3\2\2\2{R\3\2\2\2{]\3\2\2\2{j\3\2\2\2{p\3\2")
        buf.write("\2\2{x\3\2\2\2|\5\3\2\2\2}\177\7+\2\2~}\3\2\2\2~\177\3")
        buf.write("\2\2\2\177\u0089\3\2\2\2\u0080\u0085\7+\2\2\u0081\u0082")
        buf.write("\7\3\2\2\u0082\u0084\7+\2\2\u0083\u0081\3\2\2\2\u0084")
        buf.write("\u0087\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2")
        buf.write("\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0088~\3\2\2")
        buf.write("\2\u0088\u0080\3\2\2\2\u0089\7\3\2\2\2\u008a\u008c\7/")
        buf.write("\2\2\u008b\u008d\5\4\3\2\u008c\u008b\3\2\2\2\u008d\u008e")
        buf.write("\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write("\u0090\3\2\2\2\u0090\u0091\7\60\2\2\u0091\t\3\2\2\2\u0092")
        buf.write("\u0094\7/\2\2\u0093\u0095\5\4\3\2\u0094\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3")
        buf.write("\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\7\60\2\2\u0099")
        buf.write("\13\3\2\2\2\u009a\u009b\5\20\t\2\u009b\u009c\5\16\b\2")
        buf.write("\u009c\r\3\2\2\2\u009d\u009e\t\2\2\2\u009e\u00a0\5\20")
        buf.write("\t\2\u009f\u009d\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\17\3\2\2\2\u00a3\u00a1")
        buf.write("\3\2\2\2\u00a4\u00a5\5\24\13\2\u00a5\u00a6\5\22\n\2\u00a6")
        buf.write("\21\3\2\2\2\u00a7\u00a8\t\3\2\2\u00a8\u00aa\5\30\r\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2")
        buf.write("\u00ab\u00ac\3\2\2\2\u00ac\23\3\2\2\2\u00ad\u00ab\3\2")
        buf.write("\2\2\u00ae\u00af\5\30\r\2\u00af\u00b0\5\26\f\2\u00b0\25")
        buf.write("\3\2\2\2\u00b1\u00b2\t\4\2\2\u00b2\u00b4\5\30\r\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2")
        buf.write("\u00b5\u00b6\3\2\2\2\u00b6\27\3\2\2\2\u00b7\u00b5\3\2")
        buf.write("\2\2\u00b8\u00b9\5\36\20\2\u00b9\u00ba\5\32\16\2\u00ba")
        buf.write("\31\3\2\2\2\u00bb\u00bc\7\5\2\2\u00bc\u00bd\5\f\7\2\u00bd")
        buf.write("\u00be\7\6\2\2\u00be\u00c0\3\2\2\2\u00bf\u00bb\3\2\2\2")
        buf.write("\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3")
        buf.write("\2\2\2\u00c2\33\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c9")
        buf.write("\5\f\7\2\u00c5\u00c6\7\3\2\2\u00c6\u00c8\5\f\7\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2")
        buf.write("\u00c9\u00ca\3\2\2\2\u00ca\35\3\2\2\2\u00cb\u00c9\3\2")
        buf.write("\2\2\u00cc\u00ce\7\31\2\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce")
        buf.write("\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00ea\7*\2\2\u00d0")
        buf.write("\u00d2\7\31\2\2\u00d1\u00d0\3\2\2\2\u00d1\u00d2\3\2\2")
        buf.write("\2\u00d2\u00d3\3\2\2\2\u00d3\u00ea\7&\2\2\u00d4\u00ea")
        buf.write("\7(\2\2\u00d5\u00ea\7)\2\2\u00d6\u00ea\7\'\2\2\u00d7\u00ea")
        buf.write("\5\"\22\2\u00d8\u00d9\5\"\22\2\u00d9\u00db\7\7\2\2\u00da")
        buf.write("\u00dc\5\34\17\2\u00db\u00da\3\2\2\2\u00db\u00dc\3\2\2")
        buf.write("\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\7\b\2\2\u00de\u00ea")
        buf.write("\3\2\2\2\u00df\u00e0\7\7\2\2\u00e0\u00e1\5\34\17\2\u00e1")
        buf.write("\u00e2\7\b\2\2\u00e2\u00ea\3\2\2\2\u00e3\u00ea\5 \21\2")
        buf.write("\u00e4\u00e5\7\25\2\2\u00e5\u00e6\7\7\2\2\u00e6\u00e7")
        buf.write("\5\f\7\2\u00e7\u00e8\7\b\2\2\u00e8\u00ea\3\2\2\2\u00e9")
        buf.write("\u00cd\3\2\2\2\u00e9\u00d1\3\2\2\2\u00e9\u00d4\3\2\2\2")
        buf.write("\u00e9\u00d5\3\2\2\2\u00e9\u00d6\3\2\2\2\u00e9\u00d7\3")
        buf.write("\2\2\2\u00e9\u00d8\3\2\2\2\u00e9\u00df\3\2\2\2\u00e9\u00e3")
        buf.write("\3\2\2\2\u00e9\u00e4\3\2\2\2\u00ea\37\3\2\2\2\u00eb\u00ed")
        buf.write("\7\5\2\2\u00ec\u00ee\5\34\17\2\u00ed\u00ec\3\2\2\2\u00ed")
        buf.write("\u00ee\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\7\6\2\2")
        buf.write("\u00f0!\3\2\2\2\u00f1\u00f2\7+\2\2\u00f2#\3\2\2\2\36\'")
        buf.write("\648?CGITX_cs{~\u0085\u0088\u008e\u0096\u00a1\u00ab\u00b5")
        buf.write("\u00c1\u00c9\u00cd\u00d1\u00db\u00e9\u00ed")
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
                      "BOOL", "CHAR", "STRING", "NUM", "ID", "NEWLINE", 
                      "WS", "SKIPP", "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_argList = 2
    RULE_sequence = 3
    RULE_elseSequence = 4
    RULE_expression = 5
    RULE_comparison = 6
    RULE_additionExpression = 7
    RULE_additionFactor = 8
    RULE_multiplicationExpression = 9
    RULE_multiplicationFactor = 10
    RULE_elementExpression = 11
    RULE_elementAccess = 12
    RULE_expressionList = 13
    RULE_primitiveExpression = 14
    RULE_listExpression = 15
    RULE_ident = 16

    ruleNames =  [ "program", "statement", "argList", "sequence", "elseSequence", 
                   "expression", "comparison", "additionExpression", "additionFactor", 
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
    BOOL=37
    CHAR=38
    STRING=39
    NUM=40
    ID=41
    NEWLINE=42
    WS=43
    SKIPP=44
    INDENT=45
    DEDENT=46

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
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.IF) | (1 << miParserParser.WHILE) | (1 << miParserParser.FOR) | (1 << miParserParser.RETURN) | (1 << miParserParser.PRINT) | (1 << miParserParser.LEN) | (1 << miParserParser.DEF) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.BOOL) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0):
                self.state = 34
                self.statement()
                self.state = 39
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
        def elementAccess(self):
            return self.getTypedRuleContext(miParserParser.ElementAccessContext,0)

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
        def sequence(self):
            return self.getTypedRuleContext(miParserParser.SequenceContext,0)

        def LEFTP(self):
            return self.getToken(miParserParser.LEFTP, 0)
        def RIGHTP(self):
            return self.getToken(miParserParser.RIGHTP, 0)
        def ELSE(self):
            return self.getToken(miParserParser.ELSE, 0)
        def elseSequence(self):
            return self.getTypedRuleContext(miParserParser.ElseSequenceContext,0)


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
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = miParserParser.DefStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(miParserParser.DEF)
                self.state = 41
                self.match(miParserParser.ID)
                self.state = 42
                self.match(miParserParser.LEFTP)
                self.state = 43
                self.argList()
                self.state = 44
                self.match(miParserParser.RIGHTP)
                self.state = 45
                self.match(miParserParser.COLON)
                self.state = 46
                self.sequence()
                pass

            elif la_ == 2:
                localctx = miParserParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(miParserParser.IF)
                self.state = 50
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 49
                    self.match(miParserParser.LEFTP)


                self.state = 52
                self.expression()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.RIGHTP:
                    self.state = 53
                    self.match(miParserParser.RIGHTP)


                self.state = 56
                self.match(miParserParser.COLON)
                self.state = 57
                self.sequence()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.ELSE:
                    self.state = 58
                    self.match(miParserParser.ELSE)
                    self.state = 59
                    self.match(miParserParser.COLON)
                    self.state = 60
                    self.elseSequence()


                pass

            elif la_ == 3:
                localctx = miParserParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.match(miParserParser.RETURN)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.LEN) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.BOOL) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0):
                    self.state = 65
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        self.state = 64
                        self.match(miParserParser.LEFTP)


                    self.state = 67
                    self.expression()
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==miParserParser.RIGHTP:
                        self.state = 68
                        self.match(miParserParser.RIGHTP)




                self.state = 73
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = miParserParser.PrintStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.match(miParserParser.PRINT)
                self.state = 75
                self.match(miParserParser.LEFTP)
                self.state = 76
                self.expression()
                self.state = 77
                self.match(miParserParser.RIGHTP)
                self.state = 78
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 5:
                localctx = miParserParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.match(miParserParser.WHILE)
                self.state = 82
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 81
                    self.match(miParserParser.LEFTP)


                self.state = 84
                self.expression()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.RIGHTP:
                    self.state = 85
                    self.match(miParserParser.RIGHTP)


                self.state = 88
                self.match(miParserParser.COLON)
                self.state = 89
                self.sequence()
                pass

            elif la_ == 6:
                localctx = miParserParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 91
                self.match(miParserParser.FOR)
                self.state = 93
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 92
                    self.match(miParserParser.LEFTP)


                self.state = 95
                self.expression()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.RIGHTP:
                    self.state = 96
                    self.match(miParserParser.RIGHTP)


                self.state = 99
                self.match(miParserParser.IN)
                self.state = 100
                self.expressionList()
                self.state = 101
                self.match(miParserParser.COLON)
                self.state = 102
                self.sequence()
                pass

            elif la_ == 7:
                localctx = miParserParser.AssignStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 104
                self.match(miParserParser.ID)
                self.state = 105
                self.elementAccess()
                self.state = 106
                self.match(miParserParser.ASSIGN)
                self.state = 107
                self.expression()
                self.state = 108
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 8:
                localctx = miParserParser.FunctionCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 110
                self.primitiveExpression()
                self.state = 111
                self.match(miParserParser.LEFTP)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.LEN) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.BOOL) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0):
                    self.state = 112
                    self.expressionList()


                self.state = 115
                self.match(miParserParser.RIGHTP)
                self.state = 116
                self.match(miParserParser.NEWLINE)
                pass

            elif la_ == 9:
                localctx = miParserParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 118
                self.expressionList()
                self.state = 119
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
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = miParserParser.ArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.ID:
                    self.state = 123
                    self.match(miParserParser.ID)


                pass

            elif la_ == 2:
                localctx = miParserParser.ArgumentsListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.match(miParserParser.ID)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==miParserParser.COMMA:
                    self.state = 127
                    self.match(miParserParser.COMMA)
                    self.state = 128
                    self.match(miParserParser.ID)
                    self.state = 133
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
            self.state = 136
            self.match(miParserParser.INDENT)
            self.state = 138 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 137
                self.statement()
                self.state = 140 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.IF) | (1 << miParserParser.WHILE) | (1 << miParserParser.FOR) | (1 << miParserParser.RETURN) | (1 << miParserParser.PRINT) | (1 << miParserParser.LEN) | (1 << miParserParser.DEF) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.BOOL) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0)):
                    break

            self.state = 142
            self.match(miParserParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseSequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miParserParser.RULE_elseSequence

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ElseSequenceASTContext(ElseSequenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ElseSequenceContext
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
            if hasattr( visitor, "visitElseSequenceAST" ):
                return visitor.visitElseSequenceAST(self)
            else:
                return visitor.visitChildren(self)



    def elseSequence(self):

        localctx = miParserParser.ElseSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_elseSequence)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ElseSequenceASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(miParserParser.INDENT)
            self.state = 146 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 145
                self.statement()
                self.state = 148 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.IF) | (1 << miParserParser.WHILE) | (1 << miParserParser.FOR) | (1 << miParserParser.RETURN) | (1 << miParserParser.PRINT) | (1 << miParserParser.LEN) | (1 << miParserParser.DEF) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.BOOL) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0)):
                    break

            self.state = 150
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
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            localctx = miParserParser.ExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.additionExpression()
            self.state = 153
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
        self.enterRule(localctx, 12, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ComparisonASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.GT) | (1 << miParserParser.LT) | (1 << miParserParser.LET) | (1 << miParserParser.GET) | (1 << miParserParser.EQUAL) | (1 << miParserParser.NOTEQUAL))) != 0):
                self.state = 155
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.GT) | (1 << miParserParser.LT) | (1 << miParserParser.LET) | (1 << miParserParser.GET) | (1 << miParserParser.EQUAL) | (1 << miParserParser.NOTEQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 156
                self.additionExpression()
                self.state = 161
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
        self.enterRule(localctx, 14, self.RULE_additionExpression)
        try:
            localctx = miParserParser.AditionalExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.multiplicationExpression()
            self.state = 163
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
        self.enterRule(localctx, 16, self.RULE_additionFactor)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.AddFactorContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.ADD or _la==miParserParser.SUB:
                self.state = 165
                _la = self._input.LA(1)
                if not(_la==miParserParser.ADD or _la==miParserParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 166
                self.elementExpression()
                self.state = 171
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
        self.enterRule(localctx, 18, self.RULE_multiplicationExpression)
        try:
            localctx = miParserParser.MultiplicationExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.elementExpression()
            self.state = 173
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
        self.enterRule(localctx, 20, self.RULE_multiplicationFactor)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.MulFactorContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.MUL or _la==miParserParser.DIV:
                self.state = 175
                _la = self._input.LA(1)
                if not(_la==miParserParser.MUL or _la==miParserParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 176
                self.elementExpression()
                self.state = 181
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
        self.enterRule(localctx, 22, self.RULE_elementExpression)
        try:
            localctx = miParserParser.ElementExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.primitiveExpression()
            self.state = 183
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
        self.enterRule(localctx, 24, self.RULE_elementAccess)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ElementAccessASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.LEFTSQUARE:
                self.state = 185
                self.match(miParserParser.LEFTSQUARE)
                self.state = 186
                self.expression()
                self.state = 187
                self.match(miParserParser.RIGHTSQUARE)
                self.state = 193
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
        self.enterRule(localctx, 26, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ExpressionListASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.expression()
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.COMMA:
                self.state = 195
                self.match(miParserParser.COMMA)
                self.state = 196
                self.expression()
                self.state = 201
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


    class BoolPEContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(miParserParser.BOOL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolPE" ):
                return visitor.visitBoolPE(self)
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
        self.enterRule(localctx, 28, self.RULE_primitiveExpression)
        self._la = 0 # Token type
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                localctx = miParserParser.IntegerPEContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.SUB:
                    self.state = 202
                    self.match(miParserParser.SUB)


                self.state = 205
                self.match(miParserParser.NUM)
                pass

            elif la_ == 2:
                localctx = miParserParser.FloatPEContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==miParserParser.SUB:
                    self.state = 206
                    self.match(miParserParser.SUB)


                self.state = 209
                self.match(miParserParser.FLOAT)
                pass

            elif la_ == 3:
                localctx = miParserParser.CharPEContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.match(miParserParser.CHAR)
                pass

            elif la_ == 4:
                localctx = miParserParser.StringPEContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 211
                self.match(miParserParser.STRING)
                pass

            elif la_ == 5:
                localctx = miParserParser.BoolPEContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 212
                self.match(miParserParser.BOOL)
                pass

            elif la_ == 6:
                localctx = miParserParser.IdentifierPEContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 213
                self.ident()
                pass

            elif la_ == 7:
                localctx = miParserParser.CallPEContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 214
                self.ident()

                self.state = 215
                self.match(miParserParser.LEFTP)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.LEN) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.BOOL) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0):
                    self.state = 216
                    self.expressionList()


                self.state = 219
                self.match(miParserParser.RIGHTP)
                pass

            elif la_ == 8:
                localctx = miParserParser.ExpressPEContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 221
                self.match(miParserParser.LEFTP)
                self.state = 222
                self.expressionList()
                self.state = 223
                self.match(miParserParser.RIGHTP)
                pass

            elif la_ == 9:
                localctx = miParserParser.ListExPEContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 225
                self.listExpression()
                pass

            elif la_ == 10:
                localctx = miParserParser.LenPEContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 226
                self.match(miParserParser.LEN)
                self.state = 227
                self.match(miParserParser.LEFTP)
                self.state = 228
                self.expression()
                self.state = 229
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
        self.enterRule(localctx, 30, self.RULE_listExpression)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ListExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(miParserParser.LEFTSQUARE)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.LEFTSQUARE) | (1 << miParserParser.LEFTP) | (1 << miParserParser.LEN) | (1 << miParserParser.SUB) | (1 << miParserParser.FLOAT) | (1 << miParserParser.BOOL) | (1 << miParserParser.CHAR) | (1 << miParserParser.STRING) | (1 << miParserParser.NUM) | (1 << miParserParser.ID))) != 0):
                self.state = 234
                self.expressionList()


            self.state = 237
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
        self.enterRule(localctx, 32, self.RULE_ident)
        try:
            localctx = miParserParser.IdentASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(miParserParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





