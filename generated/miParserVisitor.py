# Generated from D:/Sebas/TEC/2022/1 Semestre/Compiladores e Interpretes/ProyectoCompiladores/miniPython\miParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miParserParser import miParserParser
else:
    from miParserParser import miParserParser

# This class defines a complete generic visitor for a parse tree produced by miParserParser.

class miParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miParserParser#programAST.
    def visitProgramAST(self, ctx:miParserParser.ProgramASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#defStatement.
    def visitDefStatement(self, ctx:miParserParser.DefStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#ifStatement.
    def visitIfStatement(self, ctx:miParserParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#returnStatement.
    def visitReturnStatement(self, ctx:miParserParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#printStatement.
    def visitPrintStatement(self, ctx:miParserParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#whileStatement.
    def visitWhileStatement(self, ctx:miParserParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#forStatement.
    def visitForStatement(self, ctx:miParserParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#assignStatement.
    def visitAssignStatement(self, ctx:miParserParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#functionCallStatement.
    def visitFunctionCallStatement(self, ctx:miParserParser.FunctionCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#expressionStatement.
    def visitExpressionStatement(self, ctx:miParserParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#argument.
    def visitArgument(self, ctx:miParserParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#argumentsList.
    def visitArgumentsList(self, ctx:miParserParser.ArgumentsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#sequenceAST.
    def visitSequenceAST(self, ctx:miParserParser.SequenceASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#elseSequenceAST.
    def visitElseSequenceAST(self, ctx:miParserParser.ElseSequenceASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#expressionAST.
    def visitExpressionAST(self, ctx:miParserParser.ExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#comparisonAST.
    def visitComparisonAST(self, ctx:miParserParser.ComparisonASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#aditionalExpressionAST.
    def visitAditionalExpressionAST(self, ctx:miParserParser.AditionalExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#addFactor.
    def visitAddFactor(self, ctx:miParserParser.AddFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#multiplicationExpressionAST.
    def visitMultiplicationExpressionAST(self, ctx:miParserParser.MultiplicationExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#mulFactor.
    def visitMulFactor(self, ctx:miParserParser.MulFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#elementExpressionAST.
    def visitElementExpressionAST(self, ctx:miParserParser.ElementExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#elementAccessAST.
    def visitElementAccessAST(self, ctx:miParserParser.ElementAccessASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#expressionListAST.
    def visitExpressionListAST(self, ctx:miParserParser.ExpressionListASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#integerPE.
    def visitIntegerPE(self, ctx:miParserParser.IntegerPEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#floatPE.
    def visitFloatPE(self, ctx:miParserParser.FloatPEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#charPE.
    def visitCharPE(self, ctx:miParserParser.CharPEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#stringPE.
    def visitStringPE(self, ctx:miParserParser.StringPEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#boolPE.
    def visitBoolPE(self, ctx:miParserParser.BoolPEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#identifierPE.
    def visitIdentifierPE(self, ctx:miParserParser.IdentifierPEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#callPE.
    def visitCallPE(self, ctx:miParserParser.CallPEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#expressPE.
    def visitExpressPE(self, ctx:miParserParser.ExpressPEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#listExPE.
    def visitListExPE(self, ctx:miParserParser.ListExPEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#lenPE.
    def visitLenPE(self, ctx:miParserParser.LenPEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#listExpressionAST.
    def visitListExpressionAST(self, ctx:miParserParser.ListExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#identAST.
    def visitIdentAST(self, ctx:miParserParser.IdentASTContext):
        return self.visitChildren(ctx)



del miParserParser