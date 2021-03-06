// Generated from d:\Sebas\TEC\2022\1 Semestre\Compiladores e Interpretes\MiniPy\miniPython\miParser.g4 by ANTLR 4.8

from antlr_denter.DenterHelper import DenterHelper
from miParserParser import miParserParser

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class miParserLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COMMA=1, COLON=2, LEFTSQUARE=3, RIGHTSQUARE=4, LEFTP=5, RIGHTP=6, ASSIGN=7, 
		DQUOTES=8, IF=9, ELSE=10, ELIF=11, WHILE=12, CONST=13, FOR=14, RETURN=15, 
		PRINT=16, LEN=17, IN=18, DEF=19, ADD=20, SUB=21, MUL=22, DIV=23, INTDIV=24, 
		GT=25, LT=26, LET=27, GET=28, EQUAL=29, FLOAT=30, CHAR=31, STRING=32, 
		NUM=33, ID=34, NEWLINE=35, WS=36, SKIPP=37;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"COMMA", "COLON", "LEFTSQUARE", "RIGHTSQUARE", "LEFTP", "RIGHTP", "ASSIGN", 
			"DQUOTES", "IF", "ELSE", "ELIF", "WHILE", "CONST", "FOR", "RETURN", "PRINT", 
			"LEN", "IN", "DEF", "ADD", "SUB", "MUL", "DIV", "INTDIV", "GT", "LT", 
			"LET", "GET", "EQUAL", "FLOAT", "CHAR", "STRING", "NUM", "ID", "NEWLINE", 
			"WS", "SKIPP", "DIGIT", "LETTER", "SYMBOLS", "COMMENT", "LINECOMMENT"
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
			"NEWLINE", "WS", "SKIPP"
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


	public miParserLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "miParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\'\u010a\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3"+
		"\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n"+
		"\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22"+
		"\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30"+
		"\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35"+
		"\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \6 \u00bb\n \r \16 \u00bc\3 "+
		"\3 \3!\3!\3!\3!\7!\u00c5\n!\f!\16!\u00c8\13!\3!\3!\3\"\3\"\7\"\u00ce\n"+
		"\"\f\"\16\"\u00d1\13\"\3#\3#\3#\3#\7#\u00d7\n#\f#\16#\u00da\13#\3$\5$"+
		"\u00dd\n$\3$\3$\7$\u00e1\n$\f$\16$\u00e4\13$\3%\3%\3%\3%\3&\3&\5&\u00ec"+
		"\n&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3*\3*\7*\u00fb\n*\f*\16*\u00fe"+
		"\13*\3*\3*\3*\3*\3+\3+\7+\u0106\n+\f+\16+\u0109\13+\3\u00fc\2,\3\3\5\4"+
		"\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22"+
		"#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C"+
		"#E$G%I&K\'M\2O\2Q\2S\2U\2\3\2\b\4\2\13\13\"\"\6\2\13\f\17\17\"\"--\3\2"+
		"\62;\4\2C\\c|\6\2\"\"./<=aa\4\2\f\f\17\17\2\u0111\2\3\3\2\2\2\2\5\3\2"+
		"\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21"+
		"\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2"+
		"\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3"+
		"\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3"+
		"\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3"+
		"\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2"+
		"\2\3W\3\2\2\2\5Y\3\2\2\2\7[\3\2\2\2\t]\3\2\2\2\13_\3\2\2\2\ra\3\2\2\2"+
		"\17c\3\2\2\2\21e\3\2\2\2\23g\3\2\2\2\25j\3\2\2\2\27o\3\2\2\2\31t\3\2\2"+
		"\2\33z\3\2\2\2\35\u0080\3\2\2\2\37\u0084\3\2\2\2!\u008b\3\2\2\2#\u0091"+
		"\3\2\2\2%\u0095\3\2\2\2\'\u0098\3\2\2\2)\u009c\3\2\2\2+\u009e\3\2\2\2"+
		"-\u00a0\3\2\2\2/\u00a2\3\2\2\2\61\u00a4\3\2\2\2\63\u00a7\3\2\2\2\65\u00a9"+
		"\3\2\2\2\67\u00ab\3\2\2\29\u00ae\3\2\2\2;\u00b1\3\2\2\2=\u00b4\3\2\2\2"+
		"?\u00b8\3\2\2\2A\u00c0\3\2\2\2C\u00cb\3\2\2\2E\u00d2\3\2\2\2G\u00dc\3"+
		"\2\2\2I\u00e5\3\2\2\2K\u00eb\3\2\2\2M\u00ef\3\2\2\2O\u00f1\3\2\2\2Q\u00f3"+
		"\3\2\2\2S\u00f5\3\2\2\2U\u0103\3\2\2\2WX\7.\2\2X\4\3\2\2\2YZ\7<\2\2Z\6"+
		"\3\2\2\2[\\\7]\2\2\\\b\3\2\2\2]^\7_\2\2^\n\3\2\2\2_`\7*\2\2`\f\3\2\2\2"+
		"ab\7+\2\2b\16\3\2\2\2cd\7?\2\2d\20\3\2\2\2ef\7$\2\2f\22\3\2\2\2gh\7k\2"+
		"\2hi\7h\2\2i\24\3\2\2\2jk\7g\2\2kl\7n\2\2lm\7u\2\2mn\7g\2\2n\26\3\2\2"+
		"\2op\7g\2\2pq\7n\2\2qr\7k\2\2rs\7h\2\2s\30\3\2\2\2tu\7y\2\2uv\7j\2\2v"+
		"w\7k\2\2wx\7n\2\2xy\7g\2\2y\32\3\2\2\2z{\7e\2\2{|\7q\2\2|}\7p\2\2}~\7"+
		"u\2\2~\177\7v\2\2\177\34\3\2\2\2\u0080\u0081\7h\2\2\u0081\u0082\7q\2\2"+
		"\u0082\u0083\7t\2\2\u0083\36\3\2\2\2\u0084\u0085\7t\2\2\u0085\u0086\7"+
		"g\2\2\u0086\u0087\7v\2\2\u0087\u0088\7w\2\2\u0088\u0089\7t\2\2\u0089\u008a"+
		"\7p\2\2\u008a \3\2\2\2\u008b\u008c\7r\2\2\u008c\u008d\7t\2\2\u008d\u008e"+
		"\7k\2\2\u008e\u008f\7p\2\2\u008f\u0090\7v\2\2\u0090\"\3\2\2\2\u0091\u0092"+
		"\7n\2\2\u0092\u0093\7g\2\2\u0093\u0094\7p\2\2\u0094$\3\2\2\2\u0095\u0096"+
		"\7k\2\2\u0096\u0097\7p\2\2\u0097&\3\2\2\2\u0098\u0099\7f\2\2\u0099\u009a"+
		"\7g\2\2\u009a\u009b\7h\2\2\u009b(\3\2\2\2\u009c\u009d\7-\2\2\u009d*\3"+
		"\2\2\2\u009e\u009f\7/\2\2\u009f,\3\2\2\2\u00a0\u00a1\7,\2\2\u00a1.\3\2"+
		"\2\2\u00a2\u00a3\7\61\2\2\u00a3\60\3\2\2\2\u00a4\u00a5\7\61\2\2\u00a5"+
		"\u00a6\7\61\2\2\u00a6\62\3\2\2\2\u00a7\u00a8\7@\2\2\u00a8\64\3\2\2\2\u00a9"+
		"\u00aa\7>\2\2\u00aa\66\3\2\2\2\u00ab\u00ac\7>\2\2\u00ac\u00ad\7?\2\2\u00ad"+
		"8\3\2\2\2\u00ae\u00af\7@\2\2\u00af\u00b0\7?\2\2\u00b0:\3\2\2\2\u00b1\u00b2"+
		"\7?\2\2\u00b2\u00b3\7?\2\2\u00b3<\3\2\2\2\u00b4\u00b5\5C\"\2\u00b5\u00b6"+
		"\7\60\2\2\u00b6\u00b7\5C\"\2\u00b7>\3\2\2\2\u00b8\u00ba\5\21\t\2\u00b9"+
		"\u00bb\5O(\2\u00ba\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00ba\3\2\2"+
		"\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\5\21\t\2\u00bf"+
		"@\3\2\2\2\u00c0\u00c6\5\21\t\2\u00c1\u00c5\5O(\2\u00c2\u00c5\5M\'\2\u00c3"+
		"\u00c5\5Q)\2\u00c4\u00c1\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3\3\2\2"+
		"\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9"+
		"\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\5\21\t\2\u00caB\3\2\2\2\u00cb"+
		"\u00cf\5M\'\2\u00cc\u00ce\5M\'\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1\3\2\2"+
		"\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0D\3\2\2\2\u00d1\u00cf"+
		"\3\2\2\2\u00d2\u00d8\5O(\2\u00d3\u00d7\5O(\2\u00d4\u00d7\5M\'\2\u00d5"+
		"\u00d7\7a\2\2\u00d6\u00d3\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3\2"+
		"\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9"+
		"F\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dd\7\17\2\2\u00dc\u00db\3\2\2\2"+
		"\u00dc\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e2\7\f\2\2\u00df\u00e1"+
		"\t\2\2\2\u00e0\u00df\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2"+
		"\u00e3\3\2\2\2\u00e3H\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e6\t\3\2\2"+
		"\u00e6\u00e7\3\2\2\2\u00e7\u00e8\b%\2\2\u00e8J\3\2\2\2\u00e9\u00ec\5S"+
		"*\2\u00ea\u00ec\5U+\2\u00eb\u00e9\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ed"+
		"\3\2\2\2\u00ed\u00ee\b&\2\2\u00eeL\3\2\2\2\u00ef\u00f0\t\4\2\2\u00f0N"+
		"\3\2\2\2\u00f1\u00f2\t\5\2\2\u00f2P\3\2\2\2\u00f3\u00f4\t\6\2\2\u00f4"+
		"R\3\2\2\2\u00f5\u00f6\7$\2\2\u00f6\u00f7\7$\2\2\u00f7\u00f8\7$\2\2\u00f8"+
		"\u00fc\3\2\2\2\u00f9\u00fb\13\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fe\3"+
		"\2\2\2\u00fc\u00fd\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe"+
		"\u00fc\3\2\2\2\u00ff\u0100\7$\2\2\u0100\u0101\7$\2\2\u0101\u0102\7$\2"+
		"\2\u0102T\3\2\2\2\u0103\u0107\7%\2\2\u0104\u0106\n\7\2\2\u0105\u0104\3"+
		"\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108"+
		"V\3\2\2\2\u0109\u0107\3\2\2\2\16\2\u00bc\u00c4\u00c6\u00cf\u00d6\u00d8"+
		"\u00dc\u00e2\u00eb\u00fc\u0107\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}