import sys
sys.path.append('./generated')

from generated.miParserLexer import miParserLexer
from generated.miParserParser import miParserParser
from antlr4 import *
from antlr4.error import ErrorListener
from antlr4.error.Errors import ParseCancellationException


class LexerErrors(ErrorListener):
    pass


if __name__ == "__main__":
    file = FileStream(sys.argv[1])

    lexerError = LexerErrors()
    lexer = miParserLexer(file)

    lexer.removeErrorListeners()
    lexer.addErrorListener(lexerError)
    stream = CommonTokenStream(lexer)
    parser = miParserParser(stream)
    # parser.removeErrorListeners()
    tree = parser.program()
