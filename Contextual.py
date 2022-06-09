from generated.miParserVisitor import miParserVisitor
from generated.miParserParser import miParserParser

from TablaSimbolos import TablaSimbolos
from TablaMetodos import TablaMetodos


class Contextual(miParserVisitor):

    def __init__(self):
        self.errores = []
        self.typeErrors = []

        self.ts = TablaSimbolos()
        self.ts.openScope()

        self.tm = TablaMetodos()
        self.tm.openScope()

        self.codigo = []
        self.instActual = 0

        self.methods = []

        self.setFor = False
        self.iterArg = ''

    def modifyArg(self, arg, instCount):
        self.codigo[instCount]['arg'] = arg

    def generate(self, instr, arg):
        self.codigo.append({'instr': instr, 'arg': arg})
        self.instActual += 1

    def checkMethods(self):
        for m in self.methods:
            _, _, found, _ = self.tm.buscar(m["ident"], m['givenParams'])
            if not found:
                self.errores.append(m)

    # Visit a parse tree #programAST.
    def visitProgramAST(self, ctx: miParserParser.ProgramASTContext):
        for i in range(0, len(ctx.statement())):
            self.visit(ctx.statement(i))
        self.generate("END", None)
        self.checkMethods()

        return self.codigo

    # Visit a parse tree #defStatement.
    def visitDefStatement(self, ctx: miParserParser.DefStatementContext):
        self.generate("DEF",ctx.ID().getText())
        args, argsCtx = self.visit(ctx.argList())
        self.tm.insertar(ctx.ID().getSymbol(), ctx, args)
        self.ts.openScope()
        self.tm.openScope()
        self.insertarArgs(args,argsCtx)
        self.visit(ctx.sequence())

        self.ts.closeScope()
        self.tm.closeScope()

    # Visit a parse tree #ifStatement.
    def visitIfStatement(self, ctx: miParserParser.IfStatementContext):
        self.visit(ctx.expression())
        ifInicial = self.instActual
        self.generate("JUMP_IF_FALSE", "")
        self.visit(ctx.sequence())

        self.modifyArg(self.instActual, ifInicial)

        if ctx.ELSE():
            self.modifyArg(self.instActual+1, ifInicial)
            absolute = self.instActual
            self.generate("JUMP_ABSOLUTE", "")
            self.visit(ctx.elseSequence())
            self.modifyArg(self.instActual, absolute)

    # Visit a parse tree #returnStatement.
    def visitReturnStatement(self, ctx: miParserParser.ReturnStatementContext):
        if ctx.expression():
            self.visit(ctx.expression())
            self.generate("RETURN_VALUE", None)
        else:
            self.generate("RETURN", None)

    # Visit a parse tree #printStatement.
    def visitPrintStatement(self, ctx: miParserParser.PrintStatementContext):
        self.visit(ctx.expression())
        self.generate("LOAD_GLOBAL", "print")
        self.generate("CALL_FUNCTION", "1")

    # Visit a parse tree #whileStatement.
    def visitWhileStatement(self, ctx: miParserParser.WhileStatementContext):
        absolute = self.instActual
        self.generate("JUMP_ABSOLUTE", "")

        self.visit(ctx.sequence())

        self.modifyArg(self.instActual, absolute)
        self.visit(ctx.expression())
        self.generate("JUMP_IF_TRUE", absolute+1)

    # Visit a parse tree #forStatement.
    def visitForStatement(self, ctx: miParserParser.ForStatementContext):
        self.ts.openScope()
        self.tm.openScope()

        self.setFor = True
        self.visit(ctx.expression())

        list = "__list__"+self.iterArg
        iterator = "__iter__"+self.iterArg


        self.generate("PUSH_LOCAL", iterator)
        self.generate("PUSH_LOCAL", list)

        self.generate("LOAD_CONST", "0")
        self.generate("STORE_FAST", iterator)

        self.setFor = False

        self.visit(ctx.expressionList())
        self.generate("STORE_FAST", list)

        instruccion = self.instActual
        self.generate("LOAD_FAST", iterator)
        self.generate("LOAD_FAST", list)
        self.generate("LOAD_GLOBAL", 'len')
        self.generate("CALL_FUNCTION", '1')
        self.generate("COMPARE_OP", '<')

        jpmfalse = self.instActual
        self.generate("JUMP_IF_FALSE", '')

        self.generate("LOAD_FAST", list)
        self.generate("LOAD_FAST", iterator)
        self.generate("BINARY_SUBSCR", None)
        self.generate("STORE_FAST", self.iterArg)

        self.visit(ctx.sequence())


        self.generate("LOAD_CONST", 1)
        self.generate("LOAD_FAST", iterator)
        self.generate("BINARY_ADD", None)
        self.generate("STORE_FAST", iterator)

        self.generate("JUMP_ABSOLUTE", instruccion)
        self.modifyArg(self.instActual, jpmfalse)

        self.ts.openScope()
        self.tm.openScope()


    # Visit a parse tree #assignStatement.
    def visitAssignStatement(self, ctx: miParserParser.AssignStatementContext):
        found = self.ts.buscarEnNivelActual(ctx.ID().getText())
        element_access, expr = self.visitElementAccess(ctx.elementAccess(), "assign")
        if not element_access:
            if not found:
                self.ts.insertar(ctx.ID().getSymbol(), ctx)
                self.generate("PUSH_LOCAL", ctx.ID().getText())
            self.visit(ctx.expression())
            self.generate("STORE_FAST", ctx.ID().getText())
        else:
            if not found:
                self.errores.append({"ident": ctx.ID().getText(), "requiredParams": None, "givenParams": None,
                                     "found": None, "args": None})
            else:
                self.visit(ctx.expression())
                self.generate("LOAD_FAST", ctx.ID().getText())
                for e in expr:
                    self.visit(e)
                self.generate("STORE_SUBSCR", None)

    # Visit a parse tree #functionCallStatement.
    def visitFunctionCallStatement(self, ctx: miParserParser.FunctionCallStatementContext):
        params = 0
        if ctx.expressionList():
            params = self.visit(ctx.expressionList())
        pe = self.visit(ctx.primitiveExpression())
        if pe == "ident":
            self.visitIdentMet(ctx.primitiveExpression().ident(), params)
            self.generate("CALL_FUNCTION", params)
        else:
            self.typeErrors.append({"type": pe, "call": True})

    # Visit a parse tree #expressionStatement.
    def visitExpressionStatement(self, ctx: miParserParser.ExpressionStatementContext):
        self.visit(ctx.expressionList())

    # Visit a parse tree #argument.
    def insertarArgs(self, args, ctx):
        for a in args:
            self.ts.insertar(a.getSymbol(), ctx)

    def visitArgument(self, ctx: miParserParser.ArgumentContext):
        arg = []
        if ctx.ID():
            arg.append(ctx.ID())
            self.generate("PUSH_LOCAL", ctx.ID())
        return arg, ctx

    # Visit a parse tree #argumentsList.
    def visitArgumentsList(self, ctx: miParserParser.ArgumentsListContext):
        args = []
        for i in range(len(ctx.ID())-1, 0, -1):
            args.append(ctx.ID(i))
            self.generate("PUSH_LOCAL", ctx.ID(i))
        args.append(ctx.ID(0))
        self.generate("PUSH_LOCAL", ctx.ID(0))
        return args, ctx

    # Visit a parse tree #sequenceAST.
    def visitSequenceAST(self, ctx: miParserParser.SequenceASTContext):
        for i in range(0, len(ctx.statement())):
            self.visit(ctx.statement(i))

    # Visit a parse tree #elseSequenceAST.
    def visitElseSequenceAST(self, ctx:miParserParser.ElseSequenceASTContext):
        for i in range(0, len(ctx.statement())):
            self.visit(ctx.statement(i))

    # Visit a parse tree #expressionAST.
    def visitExpressionAST(self, ctx: miParserParser.ExpressionASTContext):
        self.visit(ctx.additionExpression())
        self.visit(ctx.comparison())

    # Visit a parse tree #comparisonAST.
    def visitComparisonAST(self, ctx: miParserParser.ComparisonASTContext):
        for i in range(0, len(ctx.additionExpression())):
            self.visit(ctx.additionExpression(i))
            self.generate("COMPARE_OP", ctx.getChild(0))

    # Visit a parse tree #aditionalExpressionAST.
    def visitAditionalExpressionAST(self, ctx: miParserParser.AditionalExpressionASTContext):
        self.visit(ctx.multiplicationExpression())
        self.visit(ctx.additionFactor())

    # Visit a parse tree #addFactor.
    def visitAddFactor(self, ctx: miParserParser.AddFactorContext):
        for i in range(0, len(ctx.elementExpression())):
            self.visit(ctx.elementExpression(i))
            if ctx.ADD(i):
                self.generate("BINARY_ADD", None)
            else:
                self.generate("BINARY_SUBSTRACT", None)

    # Visit a parse tree #multiplicationExpressionAST.
    def visitMultiplicationExpressionAST(self, ctx: miParserParser.MultiplicationExpressionASTContext):
        self.visit(ctx.elementExpression())
        self.visit(ctx.multiplicationFactor())

    # Visit a parse tree #mulFactor.
    def visitMulFactor(self, ctx: miParserParser.MulFactorContext):
        for i in range(0, len(ctx.elementExpression())):
            self.visit(ctx.elementExpression(i))

            if ctx.MUL(i):
                self.generate("BINARY_MULTIPLY", None)
            elif ctx.DIV(i):
                self.generate("BINARY_DIVIDE", None)
            elif ctx.MOD(i):
                self.generate("BINARY_MODULO", None)
            elif ctx.POW(i):
                self.generate("BINARY_POWER", None)

    # Visit a parse tree #elementExpressionAST.
    def visitElementExpressionAST(self, ctx: miParserParser.ElementExpressionASTContext):
        pe = self.visit(ctx.primitiveExpression())
        if pe == "ident":
            self.visit(ctx.primitiveExpression().ident())
        self.visitElementAccess(ctx.elementAccess(), pe)

    # Visit a parse tree #elementAccessAST.
    def visitElementAccess(self, ctx: miParserParser.ElementAccessASTContext, ident):
        if len(ctx.expression()) != 0:
            if ident == 'assign':
                lista = ctx.expression()
                return True, lista

            if ident == 'ident':
                for i in range(0, len(ctx.expression())):
                    self.visit(ctx.expression(i))
                self.generate("BINARY_SUBSCR", None)
            else:
                self.typeErrors.append({"type": ident, "call": False})
        return False, None

    # Visit a parse tree #expressionListAST.
    def visitExpressionListAST(self, ctx: miParserParser.ExpressionListASTContext):
        x = len(ctx.expression()) -1
        for i in range(x, 0,-1):
            self.visit(ctx.expression(i))
        self.visit(ctx.expression(0))

        return len(ctx.expression())

    # Visit a parse tree #integerPE.
    def visitIntegerPE(self, ctx: miParserParser.IntegerPEContext):
        self.generate("LOAD_CONST", ctx.NUM().getText())
        return "int"

    # Visit a parse tree #floatPE.
    def visitFloatPE(self, ctx: miParserParser.FloatPEContext):
        self.generate("LOAD_CONST", ctx.FLOAT().getText())
        return 'float'

    # Visit a parse tree #charPE.
    def visitCharPE(self, ctx: miParserParser.CharPEContext):
        self.generate("LOAD_CONST", ctx.CHAR().getText())
        return 'char'

    # Visit a parse tree #stringPE.
    def visitStringPE(self, ctx: miParserParser.StringPEContext):
        self.generate("LOAD_CONST", ctx.STRING().getText())
        return 'str'

    # Visit a parse tree produced by miParserParser#boolPE.
    def visitBoolPE(self, ctx:miParserParser.BoolPEContext):
        self.generate("LOAD_CONST", ctx.BOOL().getText())
        return 'bool'

    # Visit a parse tree #identifierPE.
    def visitIdentifierPE(self, ctx: miParserParser.IdentifierPEContext):
        if self.setFor:
            self.generate("PUSH_LOCAL", ctx.ident().ID().getText())
            self.ts.insertar(ctx.ident().ID().getSymbol(), ctx.ident())
            self.iterArg = ctx.ident().ID().getText()
            return None
        return "ident"

    # Visit a parse tree produced by miParserParser#callPE.
    def visitCallPE(self, ctx:miParserParser.CallPEContext):
        params = 0
        if ctx.expressionList():
            params = self.visit(ctx.expressionList())
        self.visitIdentMet(ctx.ident(), params)
        self.generate("CALL_FUNCTION", params)
        return "call"

    # Visit a parse tree #expressPE.
    def visitExpressPE(self, ctx: miParserParser.ExpressPEContext):
        self.visit(ctx.expressionList())
        return 'expression'

    # Visit a parse tree #listExPE.
    def visitListExPE(self, ctx: miParserParser.ListExPEContext):
        self.visit(ctx.listExpression())

        return 'listExpressions'

    # Visit a parse tree #lenPE.
    def visitLenPE(self, ctx: miParserParser.LenPEContext):
        self.visit(ctx.expression())
        self.generate("LOAD_GLOBAL", "len")
        self.generate("CALL_FUNCTION", "1")
        return "int"

    # Visit a parse tree #listExpressionAST.
    def visitListExpressionAST(self, ctx: miParserParser.ListExpressionASTContext):
        if ctx.expressionList():
            len_expr = self.visit(ctx.expressionList())
            self.generate("BUILD_LIST", len_expr)

    # Visit a parse tree produced by miParserParser#ident.
    def visitIdentAST(self, ctx: miParserParser.IdentContext):
        ident = self.ts.buscar(ctx.ID().getText())
        if not ident:
            self.errores.append({"ident": ctx.ID().getText(), "requiredParams": None, "givenParams": None,
                                 "found": None, "args": None})
        self.generate("LOAD_FAST", ctx.ID().getText())

    def visitIdentMet(self, ctx: miParserParser.IdentContext, params):
        ident, requiredParams, found, args = self.tm.buscar(ctx.ID().getText(), params)
        if not ident:
            self.methods.append({"ident": ctx.ID().getText(), "requiredParams": requiredParams, "givenParams": params, "found": found, "args": args})
        self.generate("LOAD_GLOBAL", ctx.ID().getText())
        return ident

    def imprimir(self):
        self.ts.imprimir()
        self.tm.imprimir()
