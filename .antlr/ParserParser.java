// Generated from d:\Sebas\TEC\2022\1 Semestre\Compiladores e Interpretes\MiniPy\miniPython\Parser.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ParserParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INTEGER=1, FLOAT=2, CHARCONST=3, STRING=4, COMMA=5, COLON=6, LEFTSQUARE=7, 
		RIGHTSQUARE=8, LEFTP=9, RIGHTP=10, ASSIGN=11, IF=12, ELSE=13, ELIF=14, 
		WHILE=15, CONST=16, FOR=17, RETURN=18, PRINT=19, LEN=20, IN=21, DEF=22, 
		ADD=23, SUB=24, MUL=25, DIV=26, INTDIV=27, GT=28, LT=29, LET=30, GET=31, 
		EQUAL=32, NUM=33, ID=34, NEWLINE=35, WS=36, COMMENT=37, LINECOMMENT=38, 
		INDENT=39, DEDENT=40;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_argList = 2, RULE_sequence = 3, 
		RULE_expression = 4, RULE_comparison = 5, RULE_additionExpression = 6, 
		RULE_additionFactor = 7, RULE_multiplicationExpression = 8, RULE_multiplicationFactor = 9, 
		RULE_elementExpression = 10, RULE_elementAccess = 11, RULE_expressionList = 12, 
		RULE_primitiveExpression = 13, RULE_listExpression = 14;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "argList", "sequence", "expression", "comparison", 
			"additionExpression", "additionFactor", "multiplicationExpression", "multiplicationFactor", 
			"elementExpression", "elementAccess", "expressionList", "primitiveExpression", 
			"listExpression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'int'", "'float'", "'char'", "'String'", "','", "':'", "'['", 
			"']'", "'('", "')'", "'='", "'if'", "'else'", "'elif'", "'while'", "'const'", 
			"'for'", "'return'", "'print'", "'len'", "'in'", "'def'", "'+'", "'-'", 
			"'*'", "'/'", "'//'", "'>'", "'<'", "'<='", "'>='", "'=='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INTEGER", "FLOAT", "CHARCONST", "STRING", "COMMA", "COLON", "LEFTSQUARE", 
			"RIGHTSQUARE", "LEFTP", "RIGHTP", "ASSIGN", "IF", "ELSE", "ELIF", "WHILE", 
			"CONST", "FOR", "RETURN", "PRINT", "LEN", "IN", "DEF", "ADD", "SUB", 
			"MUL", "DIV", "INTDIV", "GT", "LT", "LET", "GET", "EQUAL", "NUM", "ID", 
			"NEWLINE", "WS", "COMMENT", "LINECOMMENT", "INDENT", "DEDENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Parser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ParserParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	 
		public ProgramContext() { }
		public void copyFrom(ProgramContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ProgramASTContext extends ProgramContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramASTContext(ProgramContext ctx) { copyFrom(ctx); }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			_localctx = new ProgramASTContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTEGER) | (1L << FLOAT) | (1L << CHARCONST) | (1L << STRING) | (1L << IF) | (1L << WHILE) | (1L << FOR) | (1L << RETURN) | (1L << PRINT) | (1L << DEF) | (1L << ID))) != 0)) {
				{
				{
				setState(30);
				statement();
				}
				}
				setState(35);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class WhileStatementContext extends StatementContext {
		public TerminalNode WHILE() { return getToken(ParserParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode COLON() { return getToken(ParserParser.COLON, 0); }
		public SequenceContext sequence() {
			return getRuleContext(SequenceContext.class,0);
		}
		public WhileStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class DefStatementContext extends StatementContext {
		public TerminalNode DEF() { return getToken(ParserParser.DEF, 0); }
		public TerminalNode ID() { return getToken(ParserParser.ID, 0); }
		public TerminalNode LEFTP() { return getToken(ParserParser.LEFTP, 0); }
		public ArgListContext argList() {
			return getRuleContext(ArgListContext.class,0);
		}
		public TerminalNode RIGHTP() { return getToken(ParserParser.RIGHTP, 0); }
		public TerminalNode COLON() { return getToken(ParserParser.COLON, 0); }
		public SequenceContext sequence() {
			return getRuleContext(SequenceContext.class,0);
		}
		public DefStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class PrintStatementContext extends StatementContext {
		public TerminalNode PRINT() { return getToken(ParserParser.PRINT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(ParserParser.NEWLINE, 0); }
		public PrintStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class ForStatementContext extends StatementContext {
		public TerminalNode FOR() { return getToken(ParserParser.FOR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode IN() { return getToken(ParserParser.IN, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode COLON() { return getToken(ParserParser.COLON, 0); }
		public SequenceContext sequence() {
			return getRuleContext(SequenceContext.class,0);
		}
		public ForStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class AssignStatementContext extends StatementContext {
		public TerminalNode ID() { return getToken(ParserParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(ParserParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(ParserParser.NEWLINE, 0); }
		public AssignStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class FunctionCallStatementContext extends StatementContext {
		public PrimitiveExpressionContext primitiveExpression() {
			return getRuleContext(PrimitiveExpressionContext.class,0);
		}
		public TerminalNode LEFTP() { return getToken(ParserParser.LEFTP, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode RIGHTP() { return getToken(ParserParser.RIGHTP, 0); }
		public TerminalNode NEWLINE() { return getToken(ParserParser.NEWLINE, 0); }
		public FunctionCallStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class ExpressionStatementContext extends StatementContext {
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(ParserParser.NEWLINE, 0); }
		public ExpressionStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class IfStatementContext extends StatementContext {
		public TerminalNode IF() { return getToken(ParserParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> COLON() { return getTokens(ParserParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(ParserParser.COLON, i);
		}
		public List<SequenceContext> sequence() {
			return getRuleContexts(SequenceContext.class);
		}
		public SequenceContext sequence(int i) {
			return getRuleContext(SequenceContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(ParserParser.ELSE, 0); }
		public IfStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class ReturnStatementContext extends StatementContext {
		public TerminalNode RETURN() { return getToken(ParserParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(ParserParser.NEWLINE, 0); }
		public ReturnStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(86);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				_localctx = new DefStatementContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(36);
				match(DEF);
				setState(37);
				match(ID);
				setState(38);
				match(LEFTP);
				setState(39);
				argList();
				setState(40);
				match(RIGHTP);
				setState(41);
				match(COLON);
				setState(42);
				sequence();
				}
				break;
			case 2:
				_localctx = new IfStatementContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(44);
				match(IF);
				setState(45);
				expression();
				setState(46);
				match(COLON);
				setState(47);
				sequence();
				setState(48);
				match(ELSE);
				setState(49);
				match(COLON);
				setState(50);
				sequence();
				}
				break;
			case 3:
				_localctx = new ReturnStatementContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(52);
				match(RETURN);
				setState(53);
				expression();
				setState(54);
				match(NEWLINE);
				}
				break;
			case 4:
				_localctx = new PrintStatementContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(56);
				match(PRINT);
				setState(57);
				expression();
				setState(58);
				match(NEWLINE);
				}
				break;
			case 5:
				_localctx = new WhileStatementContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(60);
				match(WHILE);
				setState(61);
				expression();
				setState(62);
				match(COLON);
				setState(63);
				sequence();
				}
				break;
			case 6:
				_localctx = new ForStatementContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(65);
				match(FOR);
				setState(66);
				expression();
				setState(67);
				match(IN);
				setState(68);
				expressionList();
				setState(69);
				match(COLON);
				setState(70);
				sequence();
				}
				break;
			case 7:
				_localctx = new AssignStatementContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(72);
				match(ID);
				setState(73);
				match(ASSIGN);
				setState(74);
				expression();
				setState(75);
				match(NEWLINE);
				}
				break;
			case 8:
				_localctx = new FunctionCallStatementContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(77);
				primitiveExpression();
				setState(78);
				match(LEFTP);
				setState(79);
				expressionList();
				setState(80);
				match(RIGHTP);
				setState(81);
				match(NEWLINE);
				}
				break;
			case 9:
				_localctx = new ExpressionStatementContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(83);
				expressionList();
				setState(84);
				match(NEWLINE);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgListContext extends ParserRuleContext {
		public ArgListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argList; }
	 
		public ArgListContext() { }
		public void copyFrom(ArgListContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ArgumentContext extends ArgListContext {
		public TerminalNode ID() { return getToken(ParserParser.ID, 0); }
		public ArgumentContext(ArgListContext ctx) { copyFrom(ctx); }
	}
	public static class ArgumentsListContext extends ArgListContext {
		public List<TerminalNode> ID() { return getTokens(ParserParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserParser.ID, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(ParserParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ParserParser.COMMA, i);
		}
		public ArgumentsListContext(ArgListContext ctx) { copyFrom(ctx); }
	}

	public final ArgListContext argList() throws RecognitionException {
		ArgListContext _localctx = new ArgListContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_argList);
		int _la;
		try {
			setState(97);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				_localctx = new ArgumentContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(88);
				match(ID);
				}
				break;
			case 2:
				_localctx = new ArgumentsListContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(89);
				match(ID);
				setState(94);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(90);
					match(COMMA);
					setState(91);
					match(ID);
					}
					}
					setState(96);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SequenceContext extends ParserRuleContext {
		public SequenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sequence; }
	 
		public SequenceContext() { }
		public void copyFrom(SequenceContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class SequenceASTContext extends SequenceContext {
		public TerminalNode INDENT() { return getToken(ParserParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(ParserParser.DEDENT, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public SequenceASTContext(SequenceContext ctx) { copyFrom(ctx); }
	}

	public final SequenceContext sequence() throws RecognitionException {
		SequenceContext _localctx = new SequenceContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_sequence);
		int _la;
		try {
			_localctx = new SequenceASTContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(INDENT);
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTEGER) | (1L << FLOAT) | (1L << CHARCONST) | (1L << STRING) | (1L << IF) | (1L << WHILE) | (1L << FOR) | (1L << RETURN) | (1L << PRINT) | (1L << DEF) | (1L << ID))) != 0)) {
				{
				{
				setState(100);
				statement();
				}
				}
				setState(105);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(106);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ExpressionASTContext extends ExpressionContext {
		public AdditionExpressionContext additionExpression() {
			return getRuleContext(AdditionExpressionContext.class,0);
		}
		public ComparisonContext comparison() {
			return getRuleContext(ComparisonContext.class,0);
		}
		public ExpressionASTContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_expression);
		try {
			_localctx = new ExpressionASTContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			additionExpression();
			setState(109);
			comparison();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ComparisonContext extends ParserRuleContext {
		public ComparisonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison; }
	 
		public ComparisonContext() { }
		public void copyFrom(ComparisonContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ComparisonASTContext extends ComparisonContext {
		public List<AdditionExpressionContext> additionExpression() {
			return getRuleContexts(AdditionExpressionContext.class);
		}
		public AdditionExpressionContext additionExpression(int i) {
			return getRuleContext(AdditionExpressionContext.class,i);
		}
		public List<TerminalNode> LT() { return getTokens(ParserParser.LT); }
		public TerminalNode LT(int i) {
			return getToken(ParserParser.LT, i);
		}
		public List<TerminalNode> GT() { return getTokens(ParserParser.GT); }
		public TerminalNode GT(int i) {
			return getToken(ParserParser.GT, i);
		}
		public List<TerminalNode> LET() { return getTokens(ParserParser.LET); }
		public TerminalNode LET(int i) {
			return getToken(ParserParser.LET, i);
		}
		public List<TerminalNode> GET() { return getTokens(ParserParser.GET); }
		public TerminalNode GET(int i) {
			return getToken(ParserParser.GET, i);
		}
		public List<TerminalNode> EQUAL() { return getTokens(ParserParser.EQUAL); }
		public TerminalNode EQUAL(int i) {
			return getToken(ParserParser.EQUAL, i);
		}
		public ComparisonASTContext(ComparisonContext ctx) { copyFrom(ctx); }
	}

	public final ComparisonContext comparison() throws RecognitionException {
		ComparisonContext _localctx = new ComparisonContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_comparison);
		int _la;
		try {
			_localctx = new ComparisonASTContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GT) | (1L << LT) | (1L << LET) | (1L << GET) | (1L << EQUAL))) != 0)) {
				{
				{
				setState(111);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GT) | (1L << LT) | (1L << LET) | (1L << GET) | (1L << EQUAL))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(112);
				additionExpression();
				}
				}
				setState(117);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AdditionExpressionContext extends ParserRuleContext {
		public AdditionExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additionExpression; }
	 
		public AdditionExpressionContext() { }
		public void copyFrom(AdditionExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AditionalExpressionASTContext extends AdditionExpressionContext {
		public MultiplicationExpressionContext multiplicationExpression() {
			return getRuleContext(MultiplicationExpressionContext.class,0);
		}
		public AdditionFactorContext additionFactor() {
			return getRuleContext(AdditionFactorContext.class,0);
		}
		public AditionalExpressionASTContext(AdditionExpressionContext ctx) { copyFrom(ctx); }
	}

	public final AdditionExpressionContext additionExpression() throws RecognitionException {
		AdditionExpressionContext _localctx = new AdditionExpressionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_additionExpression);
		try {
			_localctx = new AditionalExpressionASTContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			multiplicationExpression();
			setState(119);
			additionFactor();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AdditionFactorContext extends ParserRuleContext {
		public AdditionFactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additionFactor; }
	 
		public AdditionFactorContext() { }
		public void copyFrom(AdditionFactorContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AddFactorContext extends AdditionFactorContext {
		public List<ElementExpressionContext> elementExpression() {
			return getRuleContexts(ElementExpressionContext.class);
		}
		public ElementExpressionContext elementExpression(int i) {
			return getRuleContext(ElementExpressionContext.class,i);
		}
		public List<TerminalNode> ADD() { return getTokens(ParserParser.ADD); }
		public TerminalNode ADD(int i) {
			return getToken(ParserParser.ADD, i);
		}
		public List<TerminalNode> SUB() { return getTokens(ParserParser.SUB); }
		public TerminalNode SUB(int i) {
			return getToken(ParserParser.SUB, i);
		}
		public AddFactorContext(AdditionFactorContext ctx) { copyFrom(ctx); }
	}

	public final AdditionFactorContext additionFactor() throws RecognitionException {
		AdditionFactorContext _localctx = new AdditionFactorContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_additionFactor);
		int _la;
		try {
			_localctx = new AddFactorContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ADD || _la==SUB) {
				{
				{
				setState(121);
				_la = _input.LA(1);
				if ( !(_la==ADD || _la==SUB) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(122);
				elementExpression();
				}
				}
				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MultiplicationExpressionContext extends ParserRuleContext {
		public MultiplicationExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicationExpression; }
	 
		public MultiplicationExpressionContext() { }
		public void copyFrom(MultiplicationExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MultiplicationExpressionASTContext extends MultiplicationExpressionContext {
		public ElementExpressionContext elementExpression() {
			return getRuleContext(ElementExpressionContext.class,0);
		}
		public MultiplicationFactorContext multiplicationFactor() {
			return getRuleContext(MultiplicationFactorContext.class,0);
		}
		public MultiplicationExpressionASTContext(MultiplicationExpressionContext ctx) { copyFrom(ctx); }
	}

	public final MultiplicationExpressionContext multiplicationExpression() throws RecognitionException {
		MultiplicationExpressionContext _localctx = new MultiplicationExpressionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_multiplicationExpression);
		try {
			_localctx = new MultiplicationExpressionASTContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			elementExpression();
			setState(129);
			multiplicationFactor();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MultiplicationFactorContext extends ParserRuleContext {
		public MultiplicationFactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicationFactor; }
	 
		public MultiplicationFactorContext() { }
		public void copyFrom(MultiplicationFactorContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MulFactorContext extends MultiplicationFactorContext {
		public List<ElementExpressionContext> elementExpression() {
			return getRuleContexts(ElementExpressionContext.class);
		}
		public ElementExpressionContext elementExpression(int i) {
			return getRuleContext(ElementExpressionContext.class,i);
		}
		public List<TerminalNode> MUL() { return getTokens(ParserParser.MUL); }
		public TerminalNode MUL(int i) {
			return getToken(ParserParser.MUL, i);
		}
		public List<TerminalNode> DIV() { return getTokens(ParserParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(ParserParser.DIV, i);
		}
		public MulFactorContext(MultiplicationFactorContext ctx) { copyFrom(ctx); }
	}

	public final MultiplicationFactorContext multiplicationFactor() throws RecognitionException {
		MultiplicationFactorContext _localctx = new MultiplicationFactorContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_multiplicationFactor);
		int _la;
		try {
			_localctx = new MulFactorContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MUL || _la==DIV) {
				{
				{
				setState(131);
				_la = _input.LA(1);
				if ( !(_la==MUL || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(132);
				elementExpression();
				}
				}
				setState(137);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElementExpressionContext extends ParserRuleContext {
		public ElementExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elementExpression; }
	 
		public ElementExpressionContext() { }
		public void copyFrom(ElementExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ElementExpressionASTContext extends ElementExpressionContext {
		public PrimitiveExpressionContext primitiveExpression() {
			return getRuleContext(PrimitiveExpressionContext.class,0);
		}
		public ElementAccessContext elementAccess() {
			return getRuleContext(ElementAccessContext.class,0);
		}
		public ElementExpressionASTContext(ElementExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ElementExpressionContext elementExpression() throws RecognitionException {
		ElementExpressionContext _localctx = new ElementExpressionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_elementExpression);
		try {
			_localctx = new ElementExpressionASTContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			primitiveExpression();
			setState(139);
			elementAccess();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElementAccessContext extends ParserRuleContext {
		public ElementAccessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elementAccess; }
	 
		public ElementAccessContext() { }
		public void copyFrom(ElementAccessContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ElementAccessASTContext extends ElementAccessContext {
		public List<TerminalNode> LEFTSQUARE() { return getTokens(ParserParser.LEFTSQUARE); }
		public TerminalNode LEFTSQUARE(int i) {
			return getToken(ParserParser.LEFTSQUARE, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> RIGHTSQUARE() { return getTokens(ParserParser.RIGHTSQUARE); }
		public TerminalNode RIGHTSQUARE(int i) {
			return getToken(ParserParser.RIGHTSQUARE, i);
		}
		public ElementAccessASTContext(ElementAccessContext ctx) { copyFrom(ctx); }
	}

	public final ElementAccessContext elementAccess() throws RecognitionException {
		ElementAccessContext _localctx = new ElementAccessContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_elementAccess);
		int _la;
		try {
			_localctx = new ElementAccessASTContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LEFTSQUARE) {
				{
				{
				setState(141);
				match(LEFTSQUARE);
				setState(142);
				expression();
				setState(143);
				match(RIGHTSQUARE);
				}
				}
				setState(149);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionListContext extends ParserRuleContext {
		public ExpressionListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionList; }
	 
		public ExpressionListContext() { }
		public void copyFrom(ExpressionListContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ExpressionListASTContext extends ExpressionListContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(ParserParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ParserParser.COMMA, i);
		}
		public ExpressionListASTContext(ExpressionListContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionListContext expressionList() throws RecognitionException {
		ExpressionListContext _localctx = new ExpressionListContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_expressionList);
		int _la;
		try {
			_localctx = new ExpressionListASTContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			expression();
			setState(155);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(151);
				match(COMMA);
				setState(152);
				expression();
				}
				}
				setState(157);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrimitiveExpressionContext extends ParserRuleContext {
		public PrimitiveExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitiveExpression; }
	 
		public PrimitiveExpressionContext() { }
		public void copyFrom(PrimitiveExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PrimitiveExpressionASTContext extends PrimitiveExpressionContext {
		public TerminalNode INTEGER() { return getToken(ParserParser.INTEGER, 0); }
		public TerminalNode FLOAT() { return getToken(ParserParser.FLOAT, 0); }
		public TerminalNode CHARCONST() { return getToken(ParserParser.CHARCONST, 0); }
		public TerminalNode STRING() { return getToken(ParserParser.STRING, 0); }
		public TerminalNode ID() { return getToken(ParserParser.ID, 0); }
		public TerminalNode LEFTP() { return getToken(ParserParser.LEFTP, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode RIGHTP() { return getToken(ParserParser.RIGHTP, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ListExpressionContext listExpression() {
			return getRuleContext(ListExpressionContext.class,0);
		}
		public TerminalNode LEN() { return getToken(ParserParser.LEN, 0); }
		public PrimitiveExpressionASTContext(PrimitiveExpressionContext ctx) { copyFrom(ctx); }
	}

	public final PrimitiveExpressionContext primitiveExpression() throws RecognitionException {
		PrimitiveExpressionContext _localctx = new PrimitiveExpressionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_primitiveExpression);
		int _la;
		try {
			_localctx = new PrimitiveExpressionASTContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTEGER) | (1L << FLOAT) | (1L << CHARCONST) | (1L << STRING) | (1L << ID))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(173);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(159);
				match(LEFTP);
				setState(160);
				expressionList();
				setState(161);
				match(RIGHTP);
				}
				break;
			case 2:
				{
				setState(163);
				match(LEFTP);
				setState(164);
				expression();
				setState(165);
				match(RIGHTP);
				}
				break;
			case 3:
				{
				setState(167);
				listExpression();
				}
				break;
			case 4:
				{
				setState(168);
				match(LEN);
				setState(169);
				match(LEFTP);
				setState(170);
				expression();
				setState(171);
				match(RIGHTP);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ListExpressionContext extends ParserRuleContext {
		public ListExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listExpression; }
	 
		public ListExpressionContext() { }
		public void copyFrom(ListExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ListExpressionASTContext extends ListExpressionContext {
		public TerminalNode LEFTSQUARE() { return getToken(ParserParser.LEFTSQUARE, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode RIGHTSQUARE() { return getToken(ParserParser.RIGHTSQUARE, 0); }
		public ListExpressionASTContext(ListExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ListExpressionContext listExpression() throws RecognitionException {
		ListExpressionContext _localctx = new ListExpressionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_listExpression);
		try {
			_localctx = new ListExpressionASTContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			match(LEFTSQUARE);
			setState(176);
			expressionList();
			setState(177);
			match(RIGHTSQUARE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3*\u00b6\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\7\2\"\n\2\f\2\16"+
		"\2%\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5"+
		"\3Y\n\3\3\4\3\4\3\4\3\4\7\4_\n\4\f\4\16\4b\13\4\5\4d\n\4\3\5\3\5\7\5h"+
		"\n\5\f\5\16\5k\13\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\7\7t\n\7\f\7\16\7w\13"+
		"\7\3\b\3\b\3\b\3\t\3\t\7\t~\n\t\f\t\16\t\u0081\13\t\3\n\3\n\3\n\3\13\3"+
		"\13\7\13\u0088\n\13\f\13\16\13\u008b\13\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r"+
		"\7\r\u0094\n\r\f\r\16\r\u0097\13\r\3\16\3\16\3\16\7\16\u009c\n\16\f\16"+
		"\16\16\u009f\13\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\3\17\5\17\u00b0\n\17\3\20\3\20\3\20\3\20\3\20\2\2\21"+
		"\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36\2\6\3\2\36\"\3\2\31\32\3\2\33"+
		"\34\4\2\3\6$$\2\u00ba\2#\3\2\2\2\4X\3\2\2\2\6c\3\2\2\2\be\3\2\2\2\nn\3"+
		"\2\2\2\fu\3\2\2\2\16x\3\2\2\2\20\177\3\2\2\2\22\u0082\3\2\2\2\24\u0089"+
		"\3\2\2\2\26\u008c\3\2\2\2\30\u0095\3\2\2\2\32\u0098\3\2\2\2\34\u00a0\3"+
		"\2\2\2\36\u00b1\3\2\2\2 \"\5\4\3\2! \3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3"+
		"\2\2\2$\3\3\2\2\2%#\3\2\2\2&\'\7\30\2\2\'(\7$\2\2()\7\13\2\2)*\5\6\4\2"+
		"*+\7\f\2\2+,\7\b\2\2,-\5\b\5\2-Y\3\2\2\2./\7\16\2\2/\60\5\n\6\2\60\61"+
		"\7\b\2\2\61\62\5\b\5\2\62\63\7\17\2\2\63\64\7\b\2\2\64\65\5\b\5\2\65Y"+
		"\3\2\2\2\66\67\7\24\2\2\678\5\n\6\289\7%\2\29Y\3\2\2\2:;\7\25\2\2;<\5"+
		"\n\6\2<=\7%\2\2=Y\3\2\2\2>?\7\21\2\2?@\5\n\6\2@A\7\b\2\2AB\5\b\5\2BY\3"+
		"\2\2\2CD\7\23\2\2DE\5\n\6\2EF\7\27\2\2FG\5\32\16\2GH\7\b\2\2HI\5\b\5\2"+
		"IY\3\2\2\2JK\7$\2\2KL\7\r\2\2LM\5\n\6\2MN\7%\2\2NY\3\2\2\2OP\5\34\17\2"+
		"PQ\7\13\2\2QR\5\32\16\2RS\7\f\2\2ST\7%\2\2TY\3\2\2\2UV\5\32\16\2VW\7%"+
		"\2\2WY\3\2\2\2X&\3\2\2\2X.\3\2\2\2X\66\3\2\2\2X:\3\2\2\2X>\3\2\2\2XC\3"+
		"\2\2\2XJ\3\2\2\2XO\3\2\2\2XU\3\2\2\2Y\5\3\2\2\2Zd\7$\2\2[`\7$\2\2\\]\7"+
		"\7\2\2]_\7$\2\2^\\\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2ad\3\2\2\2b`\3"+
		"\2\2\2cZ\3\2\2\2c[\3\2\2\2d\7\3\2\2\2ei\7)\2\2fh\5\4\3\2gf\3\2\2\2hk\3"+
		"\2\2\2ig\3\2\2\2ij\3\2\2\2jl\3\2\2\2ki\3\2\2\2lm\7*\2\2m\t\3\2\2\2no\5"+
		"\16\b\2op\5\f\7\2p\13\3\2\2\2qr\t\2\2\2rt\5\16\b\2sq\3\2\2\2tw\3\2\2\2"+
		"us\3\2\2\2uv\3\2\2\2v\r\3\2\2\2wu\3\2\2\2xy\5\22\n\2yz\5\20\t\2z\17\3"+
		"\2\2\2{|\t\3\2\2|~\5\26\f\2}{\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177"+
		"\u0080\3\2\2\2\u0080\21\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083\5\26\f\2"+
		"\u0083\u0084\5\24\13\2\u0084\23\3\2\2\2\u0085\u0086\t\4\2\2\u0086\u0088"+
		"\5\26\f\2\u0087\u0085\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u0087\3\2\2\2"+
		"\u0089\u008a\3\2\2\2\u008a\25\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008d"+
		"\5\34\17\2\u008d\u008e\5\30\r\2\u008e\27\3\2\2\2\u008f\u0090\7\t\2\2\u0090"+
		"\u0091\5\n\6\2\u0091\u0092\7\n\2\2\u0092\u0094\3\2\2\2\u0093\u008f\3\2"+
		"\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096"+
		"\31\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u009d\5\n\6\2\u0099\u009a\7\7\2"+
		"\2\u009a\u009c\5\n\6\2\u009b\u0099\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b"+
		"\3\2\2\2\u009d\u009e\3\2\2\2\u009e\33\3\2\2\2\u009f\u009d\3\2\2\2\u00a0"+
		"\u00af\t\5\2\2\u00a1\u00a2\7\13\2\2\u00a2\u00a3\5\32\16\2\u00a3\u00a4"+
		"\7\f\2\2\u00a4\u00b0\3\2\2\2\u00a5\u00a6\7\13\2\2\u00a6\u00a7\5\n\6\2"+
		"\u00a7\u00a8\7\f\2\2\u00a8\u00b0\3\2\2\2\u00a9\u00b0\5\36\20\2\u00aa\u00ab"+
		"\7\26\2\2\u00ab\u00ac\7\13\2\2\u00ac\u00ad\5\n\6\2\u00ad\u00ae\7\f\2\2"+
		"\u00ae\u00b0\3\2\2\2\u00af\u00a1\3\2\2\2\u00af\u00a5\3\2\2\2\u00af\u00a9"+
		"\3\2\2\2\u00af\u00aa\3\2\2\2\u00b0\35\3\2\2\2\u00b1\u00b2\7\t\2\2\u00b2"+
		"\u00b3\5\32\16\2\u00b3\u00b4\7\n\2\2\u00b4\37\3\2\2\2\r#X`ciu\177\u0089"+
		"\u0095\u009d\u00af";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}