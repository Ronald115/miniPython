// Generated from d:\Sebas\TEC\2022\1 Semestre\Compiladores e Interpretes\MiniPy\miniPython\miParser.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class miParserParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COMMA=1, COLON=2, LEFTSQUARE=3, RIGHTSQUARE=4, LEFTP=5, RIGHTP=6, ASSIGN=7, 
		DQUOTES=8, IF=9, ELSE=10, ELIF=11, WHILE=12, CONST=13, FOR=14, RETURN=15, 
		PRINT=16, LEN=17, IN=18, DEF=19, ADD=20, SUB=21, MUL=22, DIV=23, INTDIV=24, 
		GT=25, LT=26, LET=27, GET=28, EQUAL=29, FLOAT=30, CHAR=31, STRING=32, 
		NUM=33, ID=34, NEWLINE=35, WS=36, SKIPP=37, INDENT=38, DEDENT=39;
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
			null, "','", "':'", "'['", "']'", "'('", "')'", "'='", "'\"'", "'if'", 
			"'else'", "'elif'", "'while'", "'const'", "'for'", "'return'", "'print'", 
			"'len'", "'in'", "'def'", "'+'", "'-'", "'*'", "'/'", "'//'", "'>'", 
			"'<'", "'<='", "'>='", "'=='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", "LEFTP", "RIGHTP", 
			"ASSIGN", "DQUOTES", "IF", "ELSE", "ELIF", "WHILE", "CONST", "FOR", "RETURN", 
			"PRINT", "LEN", "IN", "DEF", "ADD", "SUB", "MUL", "DIV", "INTDIV", "GT", 
			"LT", "LET", "GET", "EQUAL", "FLOAT", "CHAR", "STRING", "NUM", "ID", 
			"NEWLINE", "WS", "SKIPP", "INDENT", "DEDENT"
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
	public String getGrammarFileName() { return "miParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public miParserParser(TokenStream input) {
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
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LEFTSQUARE) | (1L << LEFTP) | (1L << IF) | (1L << WHILE) | (1L << FOR) | (1L << RETURN) | (1L << PRINT) | (1L << LEN) | (1L << DEF) | (1L << FLOAT) | (1L << CHAR) | (1L << STRING) | (1L << NUM) | (1L << ID))) != 0)) {
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
		public TerminalNode WHILE() { return getToken(miParserParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode COLON() { return getToken(miParserParser.COLON, 0); }
		public SequenceContext sequence() {
			return getRuleContext(SequenceContext.class,0);
		}
		public TerminalNode LEFTP() { return getToken(miParserParser.LEFTP, 0); }
		public TerminalNode RIGHTP() { return getToken(miParserParser.RIGHTP, 0); }
		public WhileStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class DefStatementContext extends StatementContext {
		public TerminalNode DEF() { return getToken(miParserParser.DEF, 0); }
		public TerminalNode ID() { return getToken(miParserParser.ID, 0); }
		public TerminalNode LEFTP() { return getToken(miParserParser.LEFTP, 0); }
		public ArgListContext argList() {
			return getRuleContext(ArgListContext.class,0);
		}
		public TerminalNode RIGHTP() { return getToken(miParserParser.RIGHTP, 0); }
		public TerminalNode COLON() { return getToken(miParserParser.COLON, 0); }
		public SequenceContext sequence() {
			return getRuleContext(SequenceContext.class,0);
		}
		public DefStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class PrintStatementContext extends StatementContext {
		public TerminalNode PRINT() { return getToken(miParserParser.PRINT, 0); }
		public TerminalNode LEFTP() { return getToken(miParserParser.LEFTP, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHTP() { return getToken(miParserParser.RIGHTP, 0); }
		public TerminalNode NEWLINE() { return getToken(miParserParser.NEWLINE, 0); }
		public PrintStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class ForStatementContext extends StatementContext {
		public TerminalNode FOR() { return getToken(miParserParser.FOR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode IN() { return getToken(miParserParser.IN, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode COLON() { return getToken(miParserParser.COLON, 0); }
		public SequenceContext sequence() {
			return getRuleContext(SequenceContext.class,0);
		}
		public TerminalNode LEFTP() { return getToken(miParserParser.LEFTP, 0); }
		public TerminalNode RIGHTP() { return getToken(miParserParser.RIGHTP, 0); }
		public ForStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class AssignStatementContext extends StatementContext {
		public TerminalNode ID() { return getToken(miParserParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(miParserParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(miParserParser.NEWLINE, 0); }
		public AssignStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class FunctionCallStatementContext extends StatementContext {
		public PrimitiveExpressionContext primitiveExpression() {
			return getRuleContext(PrimitiveExpressionContext.class,0);
		}
		public TerminalNode LEFTP() { return getToken(miParserParser.LEFTP, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode RIGHTP() { return getToken(miParserParser.RIGHTP, 0); }
		public TerminalNode NEWLINE() { return getToken(miParserParser.NEWLINE, 0); }
		public FunctionCallStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class ExpressionStatementContext extends StatementContext {
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(miParserParser.NEWLINE, 0); }
		public ExpressionStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class IfStatementContext extends StatementContext {
		public TerminalNode IF() { return getToken(miParserParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> COLON() { return getTokens(miParserParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(miParserParser.COLON, i);
		}
		public List<SequenceContext> sequence() {
			return getRuleContexts(SequenceContext.class);
		}
		public SequenceContext sequence(int i) {
			return getRuleContext(SequenceContext.class,i);
		}
		public TerminalNode LEFTP() { return getToken(miParserParser.LEFTP, 0); }
		public TerminalNode RIGHTP() { return getToken(miParserParser.RIGHTP, 0); }
		public TerminalNode ELSE() { return getToken(miParserParser.ELSE, 0); }
		public IfStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class ReturnStatementContext extends StatementContext {
		public TerminalNode RETURN() { return getToken(miParserParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(miParserParser.NEWLINE, 0); }
		public TerminalNode LEFTP() { return getToken(miParserParser.LEFTP, 0); }
		public TerminalNode RIGHTP() { return getToken(miParserParser.RIGHTP, 0); }
		public ReturnStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		int _la;
		try {
			setState(113);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
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
				setState(46);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
				case 1:
					{
					setState(45);
					match(LEFTP);
					}
					break;
				}
				setState(48);
				expression();
				setState(50);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==RIGHTP) {
					{
					setState(49);
					match(RIGHTP);
					}
				}

				setState(52);
				match(COLON);
				setState(53);
				sequence();
				setState(57);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ELSE) {
					{
					setState(54);
					match(ELSE);
					setState(55);
					match(COLON);
					setState(56);
					sequence();
					}
				}

				}
				break;
			case 3:
				_localctx = new ReturnStatementContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(59);
				match(RETURN);
				setState(61);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
				case 1:
					{
					setState(60);
					match(LEFTP);
					}
					break;
				}
				setState(63);
				expression();
				setState(65);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==RIGHTP) {
					{
					setState(64);
					match(RIGHTP);
					}
				}

				setState(67);
				match(NEWLINE);
				}
				break;
			case 4:
				_localctx = new PrintStatementContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(69);
				match(PRINT);
				setState(70);
				match(LEFTP);
				setState(71);
				expression();
				setState(72);
				match(RIGHTP);
				setState(73);
				match(NEWLINE);
				}
				break;
			case 5:
				_localctx = new WhileStatementContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(75);
				match(WHILE);
				setState(77);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
				case 1:
					{
					setState(76);
					match(LEFTP);
					}
					break;
				}
				setState(79);
				expression();
				setState(81);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==RIGHTP) {
					{
					setState(80);
					match(RIGHTP);
					}
				}

				setState(83);
				match(COLON);
				setState(84);
				sequence();
				}
				break;
			case 6:
				_localctx = new ForStatementContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(86);
				match(FOR);
				setState(88);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
				case 1:
					{
					setState(87);
					match(LEFTP);
					}
					break;
				}
				setState(90);
				expression();
				setState(92);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==RIGHTP) {
					{
					setState(91);
					match(RIGHTP);
					}
				}

				setState(94);
				match(IN);
				setState(95);
				expressionList();
				setState(96);
				match(COLON);
				setState(97);
				sequence();
				}
				break;
			case 7:
				_localctx = new AssignStatementContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(99);
				match(ID);
				setState(100);
				match(ASSIGN);
				setState(101);
				expression();
				setState(102);
				match(NEWLINE);
				}
				break;
			case 8:
				_localctx = new FunctionCallStatementContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(104);
				primitiveExpression();
				setState(105);
				match(LEFTP);
				setState(106);
				expressionList();
				setState(107);
				match(RIGHTP);
				setState(108);
				match(NEWLINE);
				}
				break;
			case 9:
				_localctx = new ExpressionStatementContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(110);
				expressionList();
				setState(111);
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
		public TerminalNode ID() { return getToken(miParserParser.ID, 0); }
		public ArgumentContext(ArgListContext ctx) { copyFrom(ctx); }
	}
	public static class ArgumentsListContext extends ArgListContext {
		public List<TerminalNode> ID() { return getTokens(miParserParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(miParserParser.ID, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(miParserParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(miParserParser.COMMA, i);
		}
		public ArgumentsListContext(ArgListContext ctx) { copyFrom(ctx); }
	}

	public final ArgListContext argList() throws RecognitionException {
		ArgListContext _localctx = new ArgListContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_argList);
		int _la;
		try {
			setState(126);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				_localctx = new ArgumentContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(116);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(115);
					match(ID);
					}
				}

				}
				break;
			case 2:
				_localctx = new ArgumentsListContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(118);
				match(ID);
				setState(123);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(119);
					match(COMMA);
					setState(120);
					match(ID);
					}
					}
					setState(125);
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
		public TerminalNode INDENT() { return getToken(miParserParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(miParserParser.DEDENT, 0); }
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
			setState(128);
			match(INDENT);
			setState(130); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(129);
				statement();
				}
				}
				setState(132); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LEFTSQUARE) | (1L << LEFTP) | (1L << IF) | (1L << WHILE) | (1L << FOR) | (1L << RETURN) | (1L << PRINT) | (1L << LEN) | (1L << DEF) | (1L << FLOAT) | (1L << CHAR) | (1L << STRING) | (1L << NUM) | (1L << ID))) != 0) );
			setState(134);
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
			setState(136);
			additionExpression();
			setState(137);
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
		public List<TerminalNode> LT() { return getTokens(miParserParser.LT); }
		public TerminalNode LT(int i) {
			return getToken(miParserParser.LT, i);
		}
		public List<TerminalNode> GT() { return getTokens(miParserParser.GT); }
		public TerminalNode GT(int i) {
			return getToken(miParserParser.GT, i);
		}
		public List<TerminalNode> LET() { return getTokens(miParserParser.LET); }
		public TerminalNode LET(int i) {
			return getToken(miParserParser.LET, i);
		}
		public List<TerminalNode> GET() { return getTokens(miParserParser.GET); }
		public TerminalNode GET(int i) {
			return getToken(miParserParser.GET, i);
		}
		public List<TerminalNode> EQUAL() { return getTokens(miParserParser.EQUAL); }
		public TerminalNode EQUAL(int i) {
			return getToken(miParserParser.EQUAL, i);
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
			setState(143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GT) | (1L << LT) | (1L << LET) | (1L << GET) | (1L << EQUAL))) != 0)) {
				{
				{
				setState(139);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GT) | (1L << LT) | (1L << LET) | (1L << GET) | (1L << EQUAL))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(140);
				additionExpression();
				}
				}
				setState(145);
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
			setState(146);
			multiplicationExpression();
			setState(147);
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
		public List<TerminalNode> ADD() { return getTokens(miParserParser.ADD); }
		public TerminalNode ADD(int i) {
			return getToken(miParserParser.ADD, i);
		}
		public List<TerminalNode> SUB() { return getTokens(miParserParser.SUB); }
		public TerminalNode SUB(int i) {
			return getToken(miParserParser.SUB, i);
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
			setState(153);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ADD || _la==SUB) {
				{
				{
				setState(149);
				_la = _input.LA(1);
				if ( !(_la==ADD || _la==SUB) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(150);
				elementExpression();
				}
				}
				setState(155);
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
			setState(156);
			elementExpression();
			setState(157);
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
		public List<TerminalNode> MUL() { return getTokens(miParserParser.MUL); }
		public TerminalNode MUL(int i) {
			return getToken(miParserParser.MUL, i);
		}
		public List<TerminalNode> DIV() { return getTokens(miParserParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(miParserParser.DIV, i);
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
			setState(163);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MUL || _la==DIV) {
				{
				{
				setState(159);
				_la = _input.LA(1);
				if ( !(_la==MUL || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(160);
				elementExpression();
				}
				}
				setState(165);
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
			setState(166);
			primitiveExpression();
			setState(167);
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
		public List<TerminalNode> LEFTSQUARE() { return getTokens(miParserParser.LEFTSQUARE); }
		public TerminalNode LEFTSQUARE(int i) {
			return getToken(miParserParser.LEFTSQUARE, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> RIGHTSQUARE() { return getTokens(miParserParser.RIGHTSQUARE); }
		public TerminalNode RIGHTSQUARE(int i) {
			return getToken(miParserParser.RIGHTSQUARE, i);
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
			setState(175);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LEFTSQUARE) {
				{
				{
				setState(169);
				match(LEFTSQUARE);
				setState(170);
				expression();
				setState(171);
				match(RIGHTSQUARE);
				}
				}
				setState(177);
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
		public List<TerminalNode> COMMA() { return getTokens(miParserParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(miParserParser.COMMA, i);
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
			setState(178);
			expression();
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(179);
				match(COMMA);
				setState(180);
				expression();
				}
				}
				setState(185);
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
	public static class FloatPEContext extends PrimitiveExpressionContext {
		public TerminalNode FLOAT() { return getToken(miParserParser.FLOAT, 0); }
		public FloatPEContext(PrimitiveExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ExpressPEContext extends PrimitiveExpressionContext {
		public TerminalNode LEFTP() { return getToken(miParserParser.LEFTP, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHTP() { return getToken(miParserParser.RIGHTP, 0); }
		public ExpressPEContext(PrimitiveExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ListExPEContext extends PrimitiveExpressionContext {
		public ListExpressionContext listExpression() {
			return getRuleContext(ListExpressionContext.class,0);
		}
		public ListExPEContext(PrimitiveExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class IntegerPEContext extends PrimitiveExpressionContext {
		public TerminalNode NUM() { return getToken(miParserParser.NUM, 0); }
		public IntegerPEContext(PrimitiveExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class StringPEContext extends PrimitiveExpressionContext {
		public TerminalNode STRING() { return getToken(miParserParser.STRING, 0); }
		public StringPEContext(PrimitiveExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class LenPEContext extends PrimitiveExpressionContext {
		public TerminalNode LEN() { return getToken(miParserParser.LEN, 0); }
		public TerminalNode LEFTP() { return getToken(miParserParser.LEFTP, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHTP() { return getToken(miParserParser.RIGHTP, 0); }
		public LenPEContext(PrimitiveExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class CharPEContext extends PrimitiveExpressionContext {
		public TerminalNode CHAR() { return getToken(miParserParser.CHAR, 0); }
		public CharPEContext(PrimitiveExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class IdentifierPEContext extends PrimitiveExpressionContext {
		public TerminalNode ID() { return getToken(miParserParser.ID, 0); }
		public TerminalNode LEFTP() { return getToken(miParserParser.LEFTP, 0); }
		public TerminalNode RIGHTP() { return getToken(miParserParser.RIGHTP, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public IdentifierPEContext(PrimitiveExpressionContext ctx) { copyFrom(ctx); }
	}

	public final PrimitiveExpressionContext primitiveExpression() throws RecognitionException {
		PrimitiveExpressionContext _localctx = new PrimitiveExpressionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_primitiveExpression);
		int _la;
		try {
			setState(208);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM:
				_localctx = new IntegerPEContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(186);
				match(NUM);
				}
				break;
			case FLOAT:
				_localctx = new FloatPEContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(187);
				match(FLOAT);
				}
				break;
			case CHAR:
				_localctx = new CharPEContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(188);
				match(CHAR);
				}
				break;
			case STRING:
				_localctx = new StringPEContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(189);
				match(STRING);
				}
				break;
			case ID:
				_localctx = new IdentifierPEContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(190);
				match(ID);
				setState(196);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
				case 1:
					{
					setState(191);
					match(LEFTP);
					setState(193);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LEFTSQUARE) | (1L << LEFTP) | (1L << LEN) | (1L << FLOAT) | (1L << CHAR) | (1L << STRING) | (1L << NUM) | (1L << ID))) != 0)) {
						{
						setState(192);
						expressionList();
						}
					}

					setState(195);
					match(RIGHTP);
					}
					break;
				}
				}
				break;
			case LEFTP:
				_localctx = new ExpressPEContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(198);
				match(LEFTP);
				setState(199);
				expression();
				setState(200);
				match(RIGHTP);
				}
				break;
			case LEFTSQUARE:
				_localctx = new ListExPEContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(202);
				listExpression();
				}
				break;
			case LEN:
				_localctx = new LenPEContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(203);
				match(LEN);
				setState(204);
				match(LEFTP);
				setState(205);
				expression();
				setState(206);
				match(RIGHTP);
				}
				break;
			default:
				throw new NoViableAltException(this);
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
		public TerminalNode LEFTSQUARE() { return getToken(miParserParser.LEFTSQUARE, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode RIGHTSQUARE() { return getToken(miParserParser.RIGHTSQUARE, 0); }
		public ListExpressionASTContext(ListExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ListExpressionContext listExpression() throws RecognitionException {
		ListExpressionContext _localctx = new ListExpressionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_listExpression);
		try {
			_localctx = new ListExpressionASTContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(210);
			match(LEFTSQUARE);
			setState(211);
			expressionList();
			setState(212);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3)\u00d9\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\7\2\"\n\2\f\2\16"+
		"\2%\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\61\n\3\3\3\3\3\5"+
		"\3\65\n\3\3\3\3\3\3\3\3\3\3\3\5\3<\n\3\3\3\3\3\5\3@\n\3\3\3\3\3\5\3D\n"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3P\n\3\3\3\3\3\5\3T\n\3\3"+
		"\3\3\3\3\3\3\3\3\3\5\3[\n\3\3\3\3\3\5\3_\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3t\n\3\3\4\5\4w\n"+
		"\4\3\4\3\4\3\4\7\4|\n\4\f\4\16\4\177\13\4\5\4\u0081\n\4\3\5\3\5\6\5\u0085"+
		"\n\5\r\5\16\5\u0086\3\5\3\5\3\6\3\6\3\6\3\7\3\7\7\7\u0090\n\7\f\7\16\7"+
		"\u0093\13\7\3\b\3\b\3\b\3\t\3\t\7\t\u009a\n\t\f\t\16\t\u009d\13\t\3\n"+
		"\3\n\3\n\3\13\3\13\7\13\u00a4\n\13\f\13\16\13\u00a7\13\13\3\f\3\f\3\f"+
		"\3\r\3\r\3\r\3\r\7\r\u00b0\n\r\f\r\16\r\u00b3\13\r\3\16\3\16\3\16\7\16"+
		"\u00b8\n\16\f\16\16\16\u00bb\13\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\5\17\u00c4\n\17\3\17\5\17\u00c7\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\5\17\u00d3\n\17\3\20\3\20\3\20\3\20\3\20\2\2\21\2\4"+
		"\6\b\n\f\16\20\22\24\26\30\32\34\36\2\5\3\2\33\37\3\2\26\27\3\2\30\31"+
		"\2\u00ed\2#\3\2\2\2\4s\3\2\2\2\6\u0080\3\2\2\2\b\u0082\3\2\2\2\n\u008a"+
		"\3\2\2\2\f\u0091\3\2\2\2\16\u0094\3\2\2\2\20\u009b\3\2\2\2\22\u009e\3"+
		"\2\2\2\24\u00a5\3\2\2\2\26\u00a8\3\2\2\2\30\u00b1\3\2\2\2\32\u00b4\3\2"+
		"\2\2\34\u00d2\3\2\2\2\36\u00d4\3\2\2\2 \"\5\4\3\2! \3\2\2\2\"%\3\2\2\2"+
		"#!\3\2\2\2#$\3\2\2\2$\3\3\2\2\2%#\3\2\2\2&\'\7\25\2\2\'(\7$\2\2()\7\7"+
		"\2\2)*\5\6\4\2*+\7\b\2\2+,\7\4\2\2,-\5\b\5\2-t\3\2\2\2.\60\7\13\2\2/\61"+
		"\7\7\2\2\60/\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2\62\64\5\n\6\2\63\65\7"+
		"\b\2\2\64\63\3\2\2\2\64\65\3\2\2\2\65\66\3\2\2\2\66\67\7\4\2\2\67;\5\b"+
		"\5\289\7\f\2\29:\7\4\2\2:<\5\b\5\2;8\3\2\2\2;<\3\2\2\2<t\3\2\2\2=?\7\21"+
		"\2\2>@\7\7\2\2?>\3\2\2\2?@\3\2\2\2@A\3\2\2\2AC\5\n\6\2BD\7\b\2\2CB\3\2"+
		"\2\2CD\3\2\2\2DE\3\2\2\2EF\7%\2\2Ft\3\2\2\2GH\7\22\2\2HI\7\7\2\2IJ\5\n"+
		"\6\2JK\7\b\2\2KL\7%\2\2Lt\3\2\2\2MO\7\16\2\2NP\7\7\2\2ON\3\2\2\2OP\3\2"+
		"\2\2PQ\3\2\2\2QS\5\n\6\2RT\7\b\2\2SR\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\7\4"+
		"\2\2VW\5\b\5\2Wt\3\2\2\2XZ\7\20\2\2Y[\7\7\2\2ZY\3\2\2\2Z[\3\2\2\2[\\\3"+
		"\2\2\2\\^\5\n\6\2]_\7\b\2\2^]\3\2\2\2^_\3\2\2\2_`\3\2\2\2`a\7\24\2\2a"+
		"b\5\32\16\2bc\7\4\2\2cd\5\b\5\2dt\3\2\2\2ef\7$\2\2fg\7\t\2\2gh\5\n\6\2"+
		"hi\7%\2\2it\3\2\2\2jk\5\34\17\2kl\7\7\2\2lm\5\32\16\2mn\7\b\2\2no\7%\2"+
		"\2ot\3\2\2\2pq\5\32\16\2qr\7%\2\2rt\3\2\2\2s&\3\2\2\2s.\3\2\2\2s=\3\2"+
		"\2\2sG\3\2\2\2sM\3\2\2\2sX\3\2\2\2se\3\2\2\2sj\3\2\2\2sp\3\2\2\2t\5\3"+
		"\2\2\2uw\7$\2\2vu\3\2\2\2vw\3\2\2\2w\u0081\3\2\2\2x}\7$\2\2yz\7\3\2\2"+
		"z|\7$\2\2{y\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0081\3\2\2\2\177"+
		"}\3\2\2\2\u0080v\3\2\2\2\u0080x\3\2\2\2\u0081\7\3\2\2\2\u0082\u0084\7"+
		"(\2\2\u0083\u0085\5\4\3\2\u0084\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086"+
		"\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\7)"+
		"\2\2\u0089\t\3\2\2\2\u008a\u008b\5\16\b\2\u008b\u008c\5\f\7\2\u008c\13"+
		"\3\2\2\2\u008d\u008e\t\2\2\2\u008e\u0090\5\16\b\2\u008f\u008d\3\2\2\2"+
		"\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\r\3"+
		"\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095\5\22\n\2\u0095\u0096\5\20\t\2\u0096"+
		"\17\3\2\2\2\u0097\u0098\t\3\2\2\u0098\u009a\5\26\f\2\u0099\u0097\3\2\2"+
		"\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\21"+
		"\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f\5\26\f\2\u009f\u00a0\5\24\13"+
		"\2\u00a0\23\3\2\2\2\u00a1\u00a2\t\4\2\2\u00a2\u00a4\5\26\f\2\u00a3\u00a1"+
		"\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6"+
		"\25\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\5\34\17\2\u00a9\u00aa\5\30"+
		"\r\2\u00aa\27\3\2\2\2\u00ab\u00ac\7\5\2\2\u00ac\u00ad\5\n\6\2\u00ad\u00ae"+
		"\7\6\2\2\u00ae\u00b0\3\2\2\2\u00af\u00ab\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1"+
		"\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\31\3\2\2\2\u00b3\u00b1\3\2\2"+
		"\2\u00b4\u00b9\5\n\6\2\u00b5\u00b6\7\3\2\2\u00b6\u00b8\5\n\6\2\u00b7\u00b5"+
		"\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba"+
		"\33\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00d3\7#\2\2\u00bd\u00d3\7 \2\2"+
		"\u00be\u00d3\7!\2\2\u00bf\u00d3\7\"\2\2\u00c0\u00c6\7$\2\2\u00c1\u00c3"+
		"\7\7\2\2\u00c2\u00c4\5\32\16\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4\3\2\2\2"+
		"\u00c4\u00c5\3\2\2\2\u00c5\u00c7\7\b\2\2\u00c6\u00c1\3\2\2\2\u00c6\u00c7"+
		"\3\2\2\2\u00c7\u00d3\3\2\2\2\u00c8\u00c9\7\7\2\2\u00c9\u00ca\5\n\6\2\u00ca"+
		"\u00cb\7\b\2\2\u00cb\u00d3\3\2\2\2\u00cc\u00d3\5\36\20\2\u00cd\u00ce\7"+
		"\23\2\2\u00ce\u00cf\7\7\2\2\u00cf\u00d0\5\n\6\2\u00d0\u00d1\7\b\2\2\u00d1"+
		"\u00d3\3\2\2\2\u00d2\u00bc\3\2\2\2\u00d2\u00bd\3\2\2\2\u00d2\u00be\3\2"+
		"\2\2\u00d2\u00bf\3\2\2\2\u00d2\u00c0\3\2\2\2\u00d2\u00c8\3\2\2\2\u00d2"+
		"\u00cc\3\2\2\2\u00d2\u00cd\3\2\2\2\u00d3\35\3\2\2\2\u00d4\u00d5\7\5\2"+
		"\2\u00d5\u00d6\5\32\16\2\u00d6\u00d7\7\6\2\2\u00d7\37\3\2\2\2\31#\60\64"+
		";?COSZ^sv}\u0080\u0086\u0091\u009b\u00a5\u00b1\u00b9\u00c3\u00c6\u00d2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}