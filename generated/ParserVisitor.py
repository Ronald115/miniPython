# Generated from D:/Sebas/TEC/2022/1 Semestre/Compiladores e Interpretes/MiniPy/miniPython\Parser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ParserParser import ParserParser
else:
    from ParserParser import ParserParser

# This class defines a complete generic visitor for a parse tree produced by ParserParser.

class ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ParserParser#program.
    def visitProgram(self, ctx:ParserParser.ProgramContext):
        return self.visitChildren(ctx)



del ParserParser