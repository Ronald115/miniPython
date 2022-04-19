from generated.miParserVisitor import miParserVisitor
from generated.miParserParser import miParserParser


class Contextual(miParserVisitor):
    # Visit a parse tree #programAST.
    def visitProgramAST(self, ctx: miParserParser.ProgramASTContext):
        for i in range(0,len(ctx.statement())):
            self.visit(ctx.statement(i))
        return None

    # Visit a parse tree #defStatement.
    def visitDefStatement(self, ctx: miParserParser.DefStatementContext):
        self.visit(ctx.ident())
        self.visit(ctx.argList())
        self.visit(ctx.sequence())

    # Visit a parse tree #ifStatement.
    def visitIfStatement(self, ctx: miParserParser.IfStatementContext):

        return self.visitChildren(ctx)

    # Visit a parse tree #returnStatement.
    def visitReturnStatement(self, ctx: miParserParser.ReturnStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #printStatement.
    def visitPrintStatement(self, ctx: miParserParser.PrintStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #whileStatement.
    def visitWhileStatement(self, ctx: miParserParser.WhileStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #forStatement.
    def visitForStatement(self, ctx: miParserParser.ForStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #assignStatement.
    def visitAssignStatement(self, ctx: miParserParser.AssignStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #functionCallStatement.
    def visitFunctionCallStatement(self, ctx: miParserParser.FunctionCallStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #expressionStatement.
    def visitExpressionStatement(self, ctx: miParserParser.ExpressionStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #argument.
    def visitArgument(self, ctx: miParserParser.ArgumentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #argumentsList.
    def visitArgumentsList(self, ctx: miParserParser.ArgumentsListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #sequenceAST.
    def visitSequenceAST(self, ctx: miParserParser.SequenceASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #expressionAST.
    def visitExpressionAST(self, ctx: miParserParser.ExpressionASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #comparisonAST.
    def visitComparisonAST(self, ctx: miParserParser.ComparisonASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #aditionalExpressionAST.
    def visitAditionalExpressionAST(self, ctx: miParserParser.AditionalExpressionASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #addFactor.
    def visitAddFactor(self, ctx: miParserParser.AddFactorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #multiplicationExpressionAST.
    def visitMultiplicationExpressionAST(self, ctx: miParserParser.MultiplicationExpressionASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #mulFactor.
    def visitMulFactor(self, ctx: miParserParser.MulFactorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #elementExpressionAST.
    def visitElementExpressionAST(self, ctx: miParserParser.ElementExpressionASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #elementAccessAST.
    def visitElementAccessAST(self, ctx: miParserParser.ElementAccessASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #expressionListAST.
    def visitExpressionListAST(self, ctx: miParserParser.ExpressionListASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #integerPE.
    def visitIntegerPE(self, ctx: miParserParser.IntegerPEContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #floatPE.
    def visitFloatPE(self, ctx: miParserParser.FloatPEContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #charPE.
    def visitCharPE(self, ctx: miParserParser.CharPEContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #stringPE.
    def visitStringPE(self, ctx: miParserParser.StringPEContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #identifierPE.
    def visitIdentifierPE(self, ctx: miParserParser.IdentifierPEContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #expressPE.
    def visitExpressPE(self, ctx: miParserParser.ExpressPEContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #listExPE.
    def visitListExPE(self, ctx: miParserParser.ListExPEContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #lenPE.
    def visitLenPE(self, ctx: miParserParser.LenPEContext):
        return self.visitChildren(ctx)

    # Visit a parse tree #listExpressionAST.
    def visitListExpressionAST(self, ctx: miParserParser.ListExpressionASTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by miParserParser#ident.
    def visitIdentAST(self, ctx: miParserParser.IdentContext):
        return None

