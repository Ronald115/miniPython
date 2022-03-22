grammar Parser;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from ParserParser import ParserParser
}
@lexer::members {
class Denter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: ParserLexer = lexer

    def pull_token(self):
        return super(ParserLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.Denter(self, self.NEWLINE, ParserParser.INDENT, ParserParser.DEDENT, False)
    return self.denter.next_token()
}


//1
program : statement*    #programAST;

//2
statement : defStatement | ifStatement | returnStatement
            | printStatement | whileStatement | forStatement
            | assignStatement | functionCallStatement | expressionStatement
                        #statementAST;
//3
defStatement : DEF ID LEFTP argList RIGHTP COLON sequence   #defStatementAST;

//4
argList : ID | '' | ID(COMMA ID)*   #argListAST;

//6
ifStatement : IF expression COLON sequence ELSE COLON sequence #ifStatementAST;

//7
whileStatement : WHILE expression COLON sequence #whileStatementAST;

//8
forStatement : FOR expression IN expressionList COLON sequence #forStatementAST;

//9
returnStatement : RETURN expression NEWLINE #returnStatementAST;

//10
printStatement : PRINT expression NEWLINE #printStatement;

//11
assignStatement : ID ASSIGN expression NEWLINE #assignStatementAST;

//12
functionCallStatement : primitiveExpression LEFTP expressionList RIGHTP NEWLINE  #functionCallStatementAST;

//13
expressionStatement : expressionList NEWLINE #expressionStatementAST;

//14
sequence: INDENT moreStatements DEDENT #sequenceAST;

//15
moreStatements : (statement)* #moreStatementsAST; 

//16
expression: additionExpression comparison #expressionAST;

//17
comparison: ( (LT| GT  | LET | GET | EQUAL)   additionExpression)* #comparisonAST;

//18
additionExpression: multiplicationExpression additionFactor #aditionalExpressionAST;

//19 ///////////////////////////////////////////////////////////////////////////
additionFactor: (ADD multiplicationExpression
                | SUB multiplicationExpression)* 
                #additionFactorAST;

//20
multiplicationExpression : elementExpression multiplicationFactor #multiplicationExpressionAST;


//21
multiplicationFactor: ( (MUL|DIV) elementExpression )* #multiplicationFactorAST;

//22
elementExpression : primitiveExpression elementAccess #elementExpressionAST;

//23
elementAccess : (LEFTSQUARE expression RIGHTSQUARE)* #elementAccessAST;

//24
expressionList : (expression moreExpressions)* #expressionListAST;

//25
moreExpressions : (COMMA expression)* #moreExpressionsAST;

//26
primitiveExpression : (INTEGER | FLOAT | CHARCONST | STRING | ID) (
         LEFTP expressionList RIGHTP
        | LEFTP expression RIGHTP
        | listExpression
        | LEN LEFTP expression RIGHTP    
    ) #primitiveExpressionAST;

//27
listExpression: LEFTSQUARE expressionList RIGHTSQUARE #listExpressionAST;



//DataTypes
INTEGER: 'int';
FLOAT: 'float';
CHARCONST: 'char';
STRING: 'String';


//Simbolos
COMMA: ',';
COLON: ':';
LEFTSQUARE: '[';
RIGHTSQUARE: ']';
LEFTP: '(';
RIGHTP: ')';
ASSIGN: '=';

//Palabras reservadas
IF : 'if';
ELSE : 'else';
ELIF: 'elif';
WHILE : 'while';
CONST : 'const';
FOR: 'for';
RETURN: 'return';
PRINT: 'print';
LEN: 'len';
IN: 'in';
DEF: 'def';

//Operadores
//Arithmetic
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
INTDIV: '//';

//Comparisons
GT: '>';
LT: '<';
LET: '<=';
GET: '>=';
EQUAL: '==';

//Logic
AND: 'and';
OR: 'or';
NOT: 'not';

//Otros tokens
NUM : DIGIT DIGIT*;
ID: LETTER (LETTER | DIGIT | '_')*;

fragment DIGIT : [0-9];
fragment LETTER : [a-z A-Z];


NEWLINE: ('\r'? '\n' (' ' | '\t')*); //For tabs just switch out ' '* with '\t'*

WS  :   [ +\r\n\t] -> skip ;



