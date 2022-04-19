
import json
import sys

from Contextual import Contextual

sys.path.append("./generated")

from generated.miParserLexer import miParserLexer
from generated.miParserParser import miParserParser
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener


errors = {"parser": [], "lexer": []}


class ParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        errors["parser"].append({'line': line, 'column': column, 'msg': msg})
        # print("Parser ERROR: when parsing line %d column %d: %s\n" %(line, column, msg))


class LexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        errors["lexer"].append({'line': line, 'column': column, 'msg': msg})
        # print("Scanner ERROR: line %d:%d %s\n" %(line, column, msg))



if __name__ == "__main__":
    file = FileStream(sys.argv[1])
    lexer = miParserLexer(file)
    lexer.removeErrorListeners()
    lexerError = LexerErrorListener()

    lexer.addErrorListener(lexerError)

    stream = CommonTokenStream(lexer)
    parser = miParserParser(stream)
    parser.removeErrorListeners()
    parserErrorListener = ParserErrorListener()
    parser.addErrorListener(parserErrorListener)
    tree = parser.program()

    ac = Contextual()
    ac.visit(tree)

    print(json.dumps(errors))


