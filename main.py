import sys
from miParserLexer import miParserLexer
from miParserParser import miParserParser
from antlr4 import *

if __name__ == "__main__":
    input = FileStream(sys.argv[1])
    lexer = miParserLexer(input)
    stream = CommonTokenStream(lexer)
    parser = miParserParser(stream)
    tree = parser.program()
