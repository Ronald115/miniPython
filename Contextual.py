from generated.miParserVisitor import miParserVisitor
from generated.miParserParser import miParserParser

from TablaSimbolos import TablaSimbolos


class Contextual(miParserVisitor):
    def __init__(self):
        self.ts = TablaSimbolos()
        self.ts.openScope()

    # Visit a parse tree #programAST.
    def visitProgramAST(self, ctx: miParserParser.ProgramASTContext):
        for i in range(0, len(ctx.statement())):
            self.visit(ctx.statement(i))

    # Visit a parse tree #defStatement.
    def visitDefStatement(self, ctx: miParserParser.DefStatementContext):
        self.ts.openScope()
        self.visit(ctx.ident())
        self.visit(ctx.argList())
        self.visit(ctx.sequence())
        self.ts.imprimir()
        self.ts.closeScope()

    # Visit a parse tree #ifStatement.
    def visitIfStatement(self, ctx: miParserParser.IfStatementContext):
        self.visit(ctx.expression())
        for i in range(0, len(ctx.sequence())):
            self.visit(ctx.sequence(i))

    # Visit a parse tree #returnStatement.
    def visitReturnStatement(self, ctx: miParserParser.ReturnStatementContext):
        self.visit(ctx.expression())

    # Visit a parse tree #printStatement.
    def visitPrintStatement(self, ctx: miParserParser.PrintStatementContext):
        self.visit(ctx.expression())

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
        _, ctxID = self.visit(ctx.ident())
        self.ts.insertar(ctxID.getSymbol(), ctx)
        self.visit(ctx.expression())

    # Visit a parse tree #functionCallStatement.
    def visitFunctionCallStatement(self, ctx: miParserParser.FunctionCallStatementContext):
        self.visit(ctx.primitiveExpression())
        self.visit(ctx.expressionList())

    # Visit a parse tree #expressionStatement.
    def visitExpressionStatement(self, ctx: miParserParser.ExpressionStatementContext):
        self.visit(ctx.expressionList())

    # Visit a parse tree #argument.
    def visitArgument(self, ctx: miParserParser.ArgumentContext):
        if ctx.ident():
            self.visit(ctx.ident())

    # Visit a parse tree #argumentsList.
    def visitArgumentsList(self, ctx: miParserParser.ArgumentsListContext):
        self.visit(ctx.ident(0))
        for i in range(1, len(ctx.ident())):
            self.visit(ctx.ident(i) )

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

    # Visit a parse tree #multiplicationExpressionAST.
    def visitMultiplicationExpressionAST(self, ctx: miParserParser.MultiplicationExpressionASTContext):
        self.visit(ctx.elementExpression())
        self.visit(ctx.multiplicationFactor())

    # Visit a parse tree #mulFactor.
    def visitMulFactor(self, ctx: miParserParser.MulFactorContext):
        for i in range(0, len(ctx.elementExpression())):
            self.visit(ctx.elementExpression(i))

    # Visit a parse tree #elementExpressionAST.
    def visitElementExpressionAST(self, ctx: miParserParser.ElementExpressionASTContext):
        self.visit(ctx.primitiveExpression())
        self.visit(ctx.elementAccess())

    # Visit a parse tree #elementAccessAST.
    def visitElementAccessAST(self, ctx: miParserParser.ElementAccessASTContext):
        for i in range(0, len(ctx.expression())):
            self.visit(ctx.expression(i))

    # Visit a parse tree #expressionListAST.
    def visitExpressionListAST(self, ctx: miParserParser.ExpressionListASTContext):
        self.visit(ctx.expression())
        for i in range(1, len(ctx.expression())):
            self.visit(ctx.expression(i))
        return None

    # Visit a parse tree #integerPE.
    def visitIntegerPE(self, ctx: miParserParser.IntegerPEContext):
        pass

    # Visit a parse tree #floatPE.
    def visitFloatPE(self, ctx: miParserParser.FloatPEContext):
        pass

    # Visit a parse tree #charPE.
    def visitCharPE(self, ctx: miParserParser.CharPEContext):
        pass

    # Visit a parse tree #stringPE.
    def visitStringPE(self, ctx: miParserParser.StringPEContext):
        pass

    # Visit a parse tree #identifierPE.
    def visitIdentifierPE(self, ctx: miParserParser.IdentifierPEContext):
        ident, _ = self.visit(ctx.ident())
        if ident:
            print("EXISTE")
        else:
            print("NO EXISTE")
        if ctx.expressionList():
            self.visit(ctx.expressionList())

    # Visit a parse tree #expressPE.
    def visitExpressPE(self, ctx: miParserParser.ExpressPEContext):
        self.visit(ctx.expression())

    # Visit a parse tree #listExPE.
    def visitListExPE(self, ctx: miParserParser.ListExPEContext):
        self.visit(ctx.listExpression())

    # Visit a parse tree #lenPE.
    def visitLenPE(self, ctx: miParserParser.LenPEContext):
        # LEN LEFTP
        self.visit(ctx.expression())
        # RIGHTP

    # Visit a parse tree #listExpressionAST.
    def visitListExpressionAST(self, ctx: miParserParser.ListExpressionASTContext):
        self.visit(ctx.expressionList())
        return None
    # Visit a parse tree produced by miParserParser#ident.
    def visitIdentAST(self, ctx: miParserParser.IdentContext):
        return self.ts.buscar(ctx.ID().getText()), ctx.ID()

    def imprimir(self):
        self.ts.imprimir()
