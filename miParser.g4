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
            | IF LEFTP? expression RIGHTP? COLON sequence (ELSE COLON elseSequence)? #ifStatement                         //6
            | RETURN (LEFTP? expression RIGHTP?)? NEWLINE #returnStatement                                            //7
            | PRINT LEFTP expression RIGHTP NEWLINE #printStatement                                              //8
            | WHILE LEFTP? expression RIGHTP? COLON sequence #whileStatement                                       //9
            | FOR LEFTP? expression RIGHTP? IN expressionList COLON sequence #forStatement                         //10
            | ID elementAccess ASSIGN expression NEWLINE  #assignStatement                                         //11
            | primitiveExpression LEFTP expressionList? RIGHTP NEWLINE  #functionCallStatement       //12
            | expressionList NEWLINE #expressionStatement;                                          //13
//3
//defStatement : DEF ID LEFTP argList RIGHTP COLON sequence   #defStatementAST;

//4 ***
argList :     ID?  #argument
            | ID(COMMA ID)*   #argumentsList;

//14 ***
sequence : INDENT (statement)+ DEDENT #sequenceAST;

elseSequence : INDENT (statement)+ DEDENT #elseSequenceAST;

//16
expression : additionExpression comparison #expressionAST;

//17
comparison : ( (LT| GT  | LET | GET | EQUAL | NOTEQUAL)   additionExpression)* #comparisonAST;

//18
additionExpression : multiplicationExpression additionFactor #aditionalExpressionAST;

//19 ///////////////////////////////////////////////////////////////////////////
additionFactor : ( (ADD | SUB) elementExpression )*  #addFactor;

//20
multiplicationExpression : elementExpression multiplicationFactor #multiplicationExpressionAST;


//21
multiplicationFactor : ( (MUL|DIV|MOD|POW) elementExpression )* #mulFactor;

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
                    | BOOL #boolPE
                    | ident #identifierPE
                    | ident (LEFTP expressionList? RIGHTP) #callPE
                    | LEFTP expressionList RIGHTP # expressPE
                    | listExpression #listExPE
                    | LEN LEFTP expression RIGHTP #lenPE;



//27 ***
listExpression : LEFTSQUARE expressionList? RIGHTSQUARE #listExpressionAST;

//28
ident : ID #identAST;

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
POW : '**';
MUL : '*';
DIV : '/';
MOD : '%';

//Comparisons
GT : '>';
LT : '<';
LET : '<=';
GET : '>=';
EQUAL : '==';
NOTEQUAL : '!=';




BSN : '\\n';
BST : '\\t';

ES : BSN | BST;

FLOAT : NUM'.'NUM;

BOOL : 'True' | 'False';
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


