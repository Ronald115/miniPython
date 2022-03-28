import sys
from generated.ParserLexer import ParserLexer
from generated.ParserParser import ParserParser
from antlr4 import *

if __name__ == "__main__":
    input = FileStream(sys.argv[1])
    lexer = ParserLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ParserParser(stream)
    tree = parser.program()
