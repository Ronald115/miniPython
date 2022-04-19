grammar miParser;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from miParserParser import miParserParser
}
@lexer::members {
class MyCoolDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: miParserLexer = lexer

    def pull_token(self):
        return super(miParserLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MyCoolDenter(self, self.NEWLINE, miParserParser.INDENT, miParserParser.DEDENT, False)
    return self.denter.next_token()
}


program : statement*    #programAST;




//2 ***
statement : DEF ID LEFTP argList RIGHTP COLON sequence  #defStatement                            //3
            | IF LEFTP? expression RIGHTP? COLON sequence (ELSE COLON sequence)? #ifStatement                         //6
            | RETURN LEFTP? expression RIGHTP? NEWLINE #returnStatement                                            //7
            | PRINT LEFTP expression RIGHTP NEWLINE #printStatement                                              //8
            | WHILE LEFTP? expression RIGHTP? COLON sequence #whileStatement                                       //9
            | FOR LEFTP? expression RIGHTP? IN expressionList COLON sequence #forStatement                         //10
            | ID ASSIGN expression NEWLINE  #assignStatement                                         //11
            | primitiveExpression LEFTP expressionList RIGHTP NEWLINE  #functionCallStatement       //12
            | expressionList NEWLINE #expressionStatement;                                          //13
//3
//defStatement : DEF ID LEFTP argList RIGHTP COLON sequence   #defStatementAST;

//4 ***
argList :     ID?  #argument
            | ID(COMMA ID)*   #argumentsList;

//14 ***
sequence : INDENT (statement)+ DEDENT #sequenceAST;


//16
expression : additionExpression comparison #expressionAST;

//17
comparison : ( (LT| GT  | LET | GET | EQUAL)   additionExpression)* #comparisonAST;

//18
additionExpression : multiplicationExpression additionFactor #aditionalExpressionAST;

//19 ///////////////////////////////////////////////////////////////////////////
additionFactor : ( (ADD | SUB) elementExpression)* #addFactor;

//20
multiplicationExpression : elementExpression multiplicationFactor #multiplicationExpressionAST;


//21
multiplicationFactor : ( (MUL|DIV) elementExpression )* #mulFactor;

//22
elementExpression : primitiveExpression elementAccess #elementExpressionAST;

//23 ***
elementAccess : (LEFTSQUARE expression RIGHTSQUARE)* #elementAccessAST;

//24 ***
//expressionList : (expression moreExpressions)* #expressionListAST;
expressionList : expression (COMMA expression)*  #expressionListAST;




/*
identifierExpression : ID LEFTP expressionList RIGHTP #callMultipleExpressions
                        | ID LEFTP expression RIGHTP #callExpression
                        | ID listExpression #listExpressions
                        | LEN LEFTP expression RIGHTP  #lenExpression;
*/
//26
primitiveExpression : '-'?NUM     #integerPE
                    | '-'?FLOAT   #floatPE
                    | CHAR    #charPE
                    | STRING  #stringPE
                    | ID (LEFTP expressionList? RIGHTP)?     #identifierPE
                    | LEFTP expression RIGHTP # expressPE
                    | listExpression #listExPE
                    | LEN LEFTP expression RIGHTP #lenPE;



//27 ***
listExpression : LEFTSQUARE expressionList RIGHTSQUARE #listExpressionAST;


//símbolos
COMMA : ',';
COLON : ':';
LEFTSQUARE : '[';
RIGHTSQUARE : ']';
LEFTP : '(';
RIGHTP : ')';
ASSIGN : '=';
SQUOTES : ['];
DQUOTES : '"';
QUOTES : SQUOTES | DQUOTES;

//Palabras reservadas
IF : 'if';
ELSE : 'else';
ELIF : 'elif';
WHILE : 'while';
CONST : 'const';
FOR : 'for';
RETURN : 'return';
PRINT : 'print';
LEN : 'len';
IN : 'in';
DEF : 'def';


//Operadores
//Arithmetic
ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
INTDIV : '//';


//Comparisons
GT : '>';
LT : '<';
LET : '<=';
GET : '>=';
EQUAL : '==';





BSN : '\\n';
BST : '\\t';

ES : BSN | BST;

FLOAT : NUM'.'NUM;


CHAR : SQUOTES (LETTER | DIGIT | SYMBOLS | ES) SQUOTES;
STRING :  QUOTES (LETTER | DIGIT | SYMBOLS | ES)* QUOTES;

//otros tokens
NUM : DIGIT DIGIT*;
ID : LETTER (LETTER | DIGIT | '_')*;


NEWLINE: ('\r'? '\n' (' ' | '\t')*); //For tabs just switch out ' '* with '\t'*

WS  :   [ +\r\n\t] -> skip ;
SKIPP : (  COMMENT  | LINECOMMENT ) -> skip;


fragment DIGIT : [0-9];
fragment LETTER : [a-zA-Z];
fragment SYMBOLS : ' ' | ':' | ';' | ',' | '_' | '-' | '%' | '$';
fragment COMMENT : '"""' .*? '"""';
fragment LINECOMMENT : '#' ~[\r\n]*;



















/*
grammar Parser;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from ParserParser import ParserParser
}
@lexer::members {
class MyCoolDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: ParserLexer = lexer

    def pull_token(self):
        return super(ParserLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MyCoolDenter(self, self.NEWLINE, ParserParser.INDENT, ParserParser.DEDENT, False)
    return self.denter.next_token()

}



//1 ***
//program :


program : INDENT command NEWLINE DEDENT;

command : ID ASSIGN NUM;

/*
program : statement*    #programAST;




//2 ***
statement : DEF ID LEFTP argList RIGHTP COLON sequence  #defStatement                            //3
            | IF expression COLON sequence ELSE COLON sequence #ifStatement                         //6
            | RETURN expression NEWLINE #returnStatement                                            //7
            | PRINT expression NEWLINE #printStatement                                              //8
            | WHILE expression COLON sequence #whileStatement                                       //9
            | FOR expression IN expressionList COLON sequence #forStatement                         //10
            | ID ASSIGN expression NEWLINE  #assignStatement                                         //11
            | primitiveExpression LEFTP expressionList RIGHTP NEWLINE  #functionCallStatement       //12
            | expressionList NEWLINE #expressionStatement;                                          //13
//3
//defStatement : DEF ID LEFTP argList RIGHTP COLON sequence   #defStatementAST;

//4 ***
argList :     ID?  #argument
            | ID(COMMA ID)*   #argumentsList;

//14 ***
sequence : INDENT (statement)+ DEDENT #sequenceAST;


//16
expression : additionExpression comparison #expressionAST;

//17
comparison : ( (LT| GT  | LET | GET | EQUAL)   additionExpression)* #comparisonAST;

//18
additionExpression : multiplicationExpression additionFactor #aditionalExpressionAST;

//19 ///////////////////////////////////////////////////////////////////////////
additionFactor : ( (ADD | SUB) elementExpression)* #addFactor;

//20
multiplicationExpression : elementExpression multiplicationFactor #multiplicationExpressionAST;


//21
multiplicationFactor : ( (MUL|DIV) elementExpression )* #MulFactor;

//22
elementExpression : primitiveExpression elementAccess #elementExpressionAST;

//23 ***
elementAccess : (LEFTSQUARE expression RIGHTSQUARE)* #elementAccessAST;

//24 ***
//expressionList : (expression moreExpressions)* #expressionListAST;
expressionList : expression (COMMA expression)*  #expressionListAST;



identifierExpression : ID (
                        (LEFTP expressionList RIGHTP)?
                        | LEFTP expression RIGHTP
                        | listExpression
                        | LEN LEFTP expression RIGHTP
                      ) #identifierEx;


//26
primitiveExpression : NUM     #integerPE
                    | FLOAT   #floatPE
                    | CHAR    #charPE
                    | STRING  #stringPE
                    | identifierExpression #identifierPE;




//27 ***
listExpression : LEFTSQUARE expressionList RIGHTSQUARE #listExpressionAST;


//Simbolos
COMMA : ',';
COLON : ':';
LEFTSQUARE : '[';
RIGHTSQUARE : ']';
LEFTP : '(';
RIGHTP : ')';
ASSIGN : '=';
DQUOTES : '"';

//Palabras reservadas
IF : 'if';
ELSE : 'else';
ELIF : 'elif';
WHILE : 'while';
CONST : 'const';
FOR : 'for';
RETURN : 'return';
PRINT : 'print';
LEN : 'len';
IN : 'in';
DEF : 'def';

//Operadores
//Arithmetic
ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
INTDIV : '//';

//Comparisons
GT : '>';
LT : '<';
LET : '<=';
GET : '>=';
EQUAL : '==';


FLOAT : NUM'.'NUM;
CHAR : DQUOTES LETTER+ DQUOTES;
STRING :  DQUOTES ID DQUOTES;


//Otros tokens
NUM : DIGIT DIGIT*;
ID : LETTER (LETTER | DIGIT | '_')*;

//DataTypes


fragment DIGIT : [0-9];
fragment LETTER : [a-zA-Z];


NL: ('\r'? '\n' '\t'*); //For tabs just switch out ' '* with '\t'*


fragment COMMENT : '"""' .*? '"""';
fragment SPACES : [ \t]+ ;
fragment LINECOMMENT : '#' ~[\r\n]*;

SKIPP : ( SPACES | COMMENT  | LINECOMMENT ) -> skip;
NEWLINE: ('\r'? '\n' (' ' | '\t')*); //For tabs just switch out ' '* with '\t'*

WS  :   [ +\r\n\t] -> skip ;

//6
//ifStatement : IF expression COLON sequence ELSE COLON sequence #ifStatementAST;

//7
//whileStatement : WHILE expression COLON sequence #whileStatementAST;

//8
//forStatement : FOR expression IN expressionList COLON sequence #forStatementAST;

//9
//returnStatement : RETURN expression NEWLINE #returnStatementAST;

//10
//printStatement : PRINT expression NEWLINE #printStatementAST;

//11
//assignStatement : ID ASSIGN expression NEWLINE #assignStatementAST;

//12
//functionCallStatement : primitiveExpression LEFTP expressionList RIGHTP NEWLINE  #functionCallStatementAST;

//13
//expressionStatement : expressionList NEWLINE #expressionStatementAST;



//15
//moreStatements : (statement)* #moreStatementsAST;


//25
//moreExpressions : (COMMA expression)* #moreExpressionsAST;


/*
Logic
AND: 'and';
OR: 'or';
NOT: 'not';
*/

