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
        self.instActual = 1

    def generate(self, instr, arg):
        self.codigo.append({'instr': instr, 'arg':arg})
        self.instActual += 1

    # Visit a parse tree #programAST.
    def visitProgramAST(self, ctx: miParserParser.ProgramASTContext):
        for i in range(0, len(ctx.statement())):
            self.visit(ctx.statement(i))

        self.generate("END",None)
        return self.codigo

    # Visit a parse tree #defStatement.
    def visitDefStatement(self, ctx: miParserParser.DefStatementContext):
        self.generate("DEF",ctx.ID().getText())
        args, argsCtx = self.visit(ctx.argList())

        for i in args:
            self.generate("PUSH_LOCAL",i)

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
        for i in range(0, len(ctx.sequence())):
            self.visit(ctx.sequence(i))

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
        self.generate("LOAD_GLOBAL","print")
        self.generate("CALL_FUNCTION","1")

    # Visit a parse tree #whileStatement.
    def visitWhileStatement(self, ctx: miParserParser.WhileStatementContext):
        self.visit(ctx.expression())
        self.visit(ctx.sequence())

    # Visit a parse tree #forStatement.
    def visitForStatement(self, ctx: miParserParser.ForStatementContext):
        self.visit(ctx.expression())
        self.visit(ctx.expressionList())
        self.visit(ctx.sequence())

    # Visit a parse tree #assignStatement.
    def visitAssignStatement(self, ctx: miParserParser.AssignStatementContext):
        found = self.ts.buscarEnNivelActual(ctx.ID().getText())
        if not found:
            self.ts.insertar(ctx.ID().getSymbol(), ctx)
            self.generate("PUSH_LOCAL", ctx.ID().getText())
        self.visit(ctx.expression())
        self.generate("STORE_FAST", ctx.ID().getText())

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
        return arg, ctx

    # Visit a parse tree #argumentsList.
    def visitArgumentsList(self, ctx: miParserParser.ArgumentsListContext):
        args = [ctx.ID(0)]
        #self.ts.insertar(ctx.ID(0).getSymbol(), ctx)
        for i in range(1, len(ctx.ID())):
            #self.ts.insertar(ctx.ID(i).getSymbol(), ctx)
            args.append(ctx.ID(i))
        return args, ctx

    # Visit a parse tree #sequenceAST.
    def visitSequenceAST(self, ctx: miParserParser.SequenceASTContext):
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
            else:
                self.generate("BINARY_DIVIDE", None)




    # Visit a parse tree #elementExpressionAST.
    def visitElementExpressionAST(self, ctx: miParserParser.ElementExpressionASTContext):
        pe = self.visit(ctx.primitiveExpression())
        if pe == "ident":
            self.visit(ctx.primitiveExpression().ident())
        self.visitElementAccess(ctx.elementAccess(), pe)

    # Visit a parse tree #elementAccessAST.
    def visitElementAccess(self, ctx: miParserParser.ElementAccessASTContext, ident):
        if len(ctx.expression()) != 0:
            if ident == 'ident':
                for i in range(0, len(ctx.expression())):
                    self.visit(ctx.expression(i))
            else:
                self.typeErrors.append({"type": ident, "call": False})

    # Visit a parse tree #expressionListAST.
    def visitExpressionListAST(self, ctx: miParserParser.ExpressionListASTContext):
        self.visit(ctx.expression(0))
        for i in range(1, len(ctx.expression())):
            self.visit(ctx.expression(i))

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

    # Visit a parse tree #identifierPE.
    def visitIdentifierPE(self, ctx: miParserParser.IdentifierPEContext):
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
        return "int"

    # Visit a parse tree #listExpressionAST.
    def visitListExpressionAST(self, ctx: miParserParser.ListExpressionASTContext):
        if ctx.expressionList():
            self.visit(ctx.expressionList())

    # Visit a parse tree produced by miParserParser#ident.
    def visitIdentAST(self, ctx: miParserParser.IdentContext):
        ident = self.ts.buscar(ctx.ID().getText())
        if not ident:
            self.errores.append({"ident": ctx.ID().getText(), "requiredParams": None, "givenParams": None, "found": None, "args": None})
        self.generate("LOAD_FAST", ctx.ID().getText())

    def visitIdentMet(self, ctx: miParserParser.IdentContext, params):
        ident, requiredParams, found, args = self.tm.buscar(ctx.ID().getText(), params)
        if not ident:
            self.errores.append({"ident": ctx.ID().getText(), "requiredParams": requiredParams, "givenParams": params, "found": found, "args": args})
        self.generate("LOAD_GLOBAL", ctx.ID().getText())
        return ident

    def imprimir(self):
        self.ts.imprimir()
        self.tm.imprimir()
