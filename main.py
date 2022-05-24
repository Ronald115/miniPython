from distutils.log import error
import json
import sys
import os

sys.path.append("./generated")

from generated.miParserLexer import miParserLexer
from generated.miParserParser import miParserParser

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from Contextual import Contextual

errors = {"parser": [], "lexer": [], "contextual": [], "typeErrors": []}
errorDetected = False


class ParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        errors["parser"].append({'line': line, 'column': column, 'msg': msg})
        # print("Parser ERROR: when parsing line %d column %d: %s\n" %(line, column, msg))


class LexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        errors["lexer"].append({'line': line, 'column': column, 'msg': msg})
        # print("Scanner ERROR: line %d:%d %s\n" %(line, column, msg))

def genBytecode(codigo):

    f = open('bytecode.txt', 'w')
    cont = 1
    for instr in codigo:
        if (instr['arg'] == None):
            f.write("{} {}\n".format(str(cont), instr['instr']))
        else:
            f.write("{} {} {}\n".format(str(cont), instr['instr'], instr['arg']))
        cont += 1
    f.close()


if __name__ == "__main__":
    file = FileStream(sys.argv[1], encoding='utf-8')
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

    codigo = None
    if len(errors['lexer']) == 0 and len(errors['parser']) == 0:
        ac = Contextual()
        codigo = ac.visit(tree)

        errors["contextual"] = ac.errores
        errors["typeErrors"] = ac.typeErrors
        if len(errors["contextual"]) != 0 or len(errors["typeErrors"]) != 0:
            errorDetected = True
    else:
        errorDetected = True

    if not errorDetected:
        genBytecode(codigo)
        output = os.popen('MiniPY.exe bytecode.txt').read()
    print(json.dumps({"errors": errors, "output": output[0:-1]}))
