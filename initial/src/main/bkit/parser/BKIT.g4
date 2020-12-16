//---------------1811912------------
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
} 


/*
 * PARSER definition
 */



program             : var_declars_part func_declars_part EOF
                    ;
/*
 * Global variable declaration
 */
// ..........................................................................................................\\
// ..........................................................................................................\\
// ..........................................................................................................\\
var_declars_part    : var_declar var_declars_part 
                    | 
                    ;
var_declar          : VAR COLON var_list SM
                    ;
var_list            : variable CM var_list 
                    | variable
                    ;
variable            : scalar 
                    | composite
                    ;

scalar              : ID 
                    | ID EQ init_value
                    ;

composite           : ID dimensions_of_var
                    | ID dimensions_of_var EQ init_value
                    ;
dimensions_of_var   : dimen_of_var dimensions_of_var
                    | dimen_of_var
                    ;
dimen_of_var        : LSB int_lit_dimen RSB
                    | LSB RSB
                    ;
int_lit_dimen       : INT_DECE
                    | INT_HEXA
                    | INT_OCTO
                    ;

dimensions          : dimen dimensions    
                    | dimen
                    ;
dimen               : LSB relation RSB
                    | LSB RSB
                    ;

init_value          : int_lit
                    | float_lit
                    | string_lit
                    | array_lit
                    | bool_lit
                    ;
// init_composite      : LB list_composite RB
//                     ;
// list_composite      : init_composite CM list_composite2
//                     | list_value
//                     ;
// list_composite2     : init_composite CM list_composite2
//                     | init_composite
//                     ;
// list_value          : list_int 
//                     | list_float 
//                     | list_bool
//                     | list_str
//                     ;
// list_int            : int_lit CM list_int
//                     | int_lit
//                     ;
// list_float          : float_lit CM list_float
//                     | float_lit
//                     ;
// list_bool           : bool_lit CM list_bool
//                     | bool_lit
//                     ;
// list_str            : string_lit CM list_str
//                     | string_lit
//                     ;
/*
 * Function declarations
 */
// ..........................................................................................................\\
// ..........................................................................................................\\
// ..........................................................................................................\\
func_declars_part   : func_declar func_declars_part
                    | 
                    ;

func_declar         : FUNCTION COLON ID para_declar body_declar
                    ;

para_declar         : PARAMETER COLON list_para 
                    | 
                    ;
list_para           : para CM list_para
                    | para
                    ;
para                : scalar_para 
                    | composite_para
                    ;
scalar_para         : ID
                    ;
composite_para      : ID dimensions_of_var
                    ;
                
body_declar         : BODY COLON list_stmts ENDBODY DOT
                    ;



/*
 * Statement
 */
// ..........................................................................................................\\
// ..........................................................................................................\\
// ..........................................................................................................\\

list_stmts          : list_var_stmts list_other_stmts
                    ;
list_var_stmts      : var_declar list_var_stmts
                    | 
                    ;
list_other_stmts    : stmt list_other_stmts
                    | 
                    ;
stmt                : assign_stmt
                    | if_stmt
                    | for_stmt
                    | while_stmt
                    | do_stmt
                    | break_stmt
                    | continue_stmt
                    | call_stmt
                    | return_stmt
                    ;

assign_stmt         : ID EQ relation SM
                    | exp5 EQ relation SM
                    ;

if_stmt             : IF relation THEN list_var_stmts list_other_stmts
                      list_elseif
                      case_else
                      ENDIF DOT
                    ;
list_elseif         : el_if list_elseif
                    | 
                    ;
el_if               : ELSEIF relation THEN list_var_stmts list_other_stmts
                    ;
case_else           : ELSE list_var_stmts list_other_stmts
                    | 
                    ;


for_stmt            : FOR LP ID EQ relation CM relation CM relation RP DO list_stmts ENDFOR DOT
                    ;

while_stmt          : WHILE relation DO list_stmts ENDWHILE DOT
                    ;

do_stmt             : DO list_stmts WHILE relation ENDDO DOT
                    ;

break_stmt          : BREAK SM
                    ;

continue_stmt       : CONTINUE SM       
                    ;

call_stmt           : ID LP list_args RP SM
                    ;
call                : ID LP list_args RP
                    ;
list_args           : relation CM list_args
                    | relation
                    |
                    ;

return_stmt         : RETURN relation SM  
                    | RETURN SM
                    ;

builtin_func        : print_ln 
                    | print_func 
                    | print_str_ln 
                    | read SM
                    ;
print_ln            : PRINTLN LP RP SM
                    ;
print_func          : PRINT LP relation RP SM
                    ;
print_str_ln        : PRINTSTRLN LP relation RP SM 
                    ;
read                : READ LP RP 
                    ;

/*
 * Expression
 */
// ..........................................................................................................\\
// ..........................................................................................................\\
// ..........................................................................................................\\
relation            : logical relation_op logical
                    | logical
                    ;
relation_op         : EQ_RELATION | NOT_EQ | LESS | GREATER | LESS_EQ | GREATER_EQ
                    | F_NOT_EQ | F_LESS | F_GREATER | F_LESS_EQ | F_GREATER_EQ
                    ;

logical             : logical logical_op exp
                    | exp
                    ;

logical_op          : AND
                    | OR
                    ;

exp                 : exp ADD exp2
                    | exp SUB exp2
                    | exp F_ADD exp2  
                    | exp F_SUB exp2  
                    | exp2
                    ;

exp2                : exp2 MUL exp3
                    | exp2 DIV exp3
                    | exp2 MOD exp3
                    | exp2 F_MUL exp3
                    | exp2 F_DIV exp3 
                    | exp3
                    ;

exp3                : NOT exp3
                    | exp4
                    ;

exp4                : SUB exp4
                    | F_SUB exp4
                    | exp5
                    ;

exp5                : exp5 dimensions
                    | exp6
                    ;

exp6                : int_lit
                    | float_lit
                    | bool_lit
                    | array_lit
                    | string_lit
                    | ID
                    | call 
                    | LP relation RP
                    ;


//-----------------------Literal--------------------------------
bool_lit            : BOOL_LIT
                    ;          
int_lit             : INT_DECE
                    | INT_HEXA
                    | INT_OCTO
                    ;
float_lit           : FLOAT_LIT
                    ;
string_lit          : STRING_LIT
                    ;
array_lit           : LB array_lit_element RB
                    ;
array_lit_element   : init_value CM array_lit_element
                    | init_value
                    |
                    ;

/*
 * LEXER definition
 */
// ..........................................................................................................\\
// ..........................................................................................................\\
// ..........................................................................................................\\

// // Comment
// COMMENT : '**' .*? '**' -> skip ;

// // Keywords
// ELSE: 'Else';

// INT_OF_FLOAT: 'int_of_float';
// FLOAT_OF_INT: 'float_of_int';
// INT_OF_STRING: 'int_of_string';
// STRING_OF_INT: 'string_of_int';
// FLOAT_OF_STRING: 'float_of_string';
// STRING_OF_FLOAT: 'string_of_float';
// BOOL_OF_STRING: 'bool_of_string';
// STRING_OF_BOOL: 'string_of_bool';
// BODY:'Body';
// ENDBODY: 'EndBody';
// PARAMETER: 'Parameter';
// FUNCTION: 'Function';
// RETURN: 'Return';   
// BREAK: 'Break';
// CONTINUE: 'Continue';
// DO: 'Do';
// ELSEIF: 'ElseIf';
// ENDIF: 'EndIf';
// ENDFOR: 'EndFor';
// ENDWHILE: 'EndWhile';
// FOR: 'For';
// IF: 'If';
// THEN: 'Then';
// WHILE: 'While';
// TRUE: 'True';
// FALSE: 'False';
// ENDDO: 'EndDo'; 
// VAR: 'Var' ;


// // Operator
// ADD: '+';
// SUB: '-';
// MUL: '*';
// DIV: '\\';
// ADD_F: '+.';
// SUB_F: '-.';
// MUL_F: '*.';
// DIV_F: '\\.';
// MOD: '%';
// NOT: '!';
// AND: '&&';
// OR: '||';
// NOT_EQ: '!=';
// GREATER: '>';
// LESS: '<';
// GREATER_EQ: '>=';
// LESS_EQ: '<=';
// NOT_EQ_F: '=/=';
// GREATER_F: '>.';
// LESS_F: '<.';
// GREATER_EQ_F: '>=.';
// LESS_EQ_F: '<=.';
// EQ: '=';

// // Seperator
// LSB: '[';
// RSB: ']';
// LB: '{';
// RB: '}';
// SM: ';';
// CM: ',';
// LP: '(';
// RP: ')';
// COLON: ':' ;
// DOT: '.';

// // Identifier
// ID  : [a-z][a-zA-Z0-9_]*;

// //Literals
// INT : [1-9][0-9]*
//     | '0'
//     | '0'[xX][1-9A-F][0-9A-F]*
//     | '0'[Oo][1-7][0-7]* 
//     ;
 

// fragment INT_PART: [0-9]+;
// fragment DEC_PART: '.'[0-9]*;
// fragment EXP_PART: [eE]('-'| '+' )?[0-9]+;
// FLOAT: INT_PART DEC_PART EXP_PART
//      | INT_PART DEC_PART
//      | INT_PART EXP_PART
//      ;

// // FLOAT:  [1-9]NUMBER* (
// //             ('.' NUMBER+ (('e'|'E') '-'? NUMBER+)?)
// //             |
// //             (('e'|'E') '-'? NUMBER+)
// //         );
// // ARRAY   : 
// //         ;

// // fragment ESCAPE_SEQUENCES
// // 	: '\\' [bfrnt"'\\]
// //     | [']["]
// // 	;
// // STRING : '"' (ESCAPE_SEQUENCES | ~[\n\r"'\\])* '"'
// // 	{
// // 		self.text = self.text[1:-1]
// // 	}
// //     ;
// fragment ESC_SEQ : '\\' [bfrtn'\\];
// fragment STR_CHAR      : (~[\n\r\\'"] | ESC_SEQ | '\'"'); 
// STRING                 : '"'STR_CHAR*'"' 
//         {
//                 y = str(self.text)
//                 self.text = y[1:-1]
//         }
//         ;
// fragment ESC_ILLEGAL: '\\' ~[bfrtn'\\] | ~'\\';


// BOOL: TRUE | FALSE;



// WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines




// /*
//  * Error
//  */

// UNCLOSE_STRING  : '"' STR_CHAR*
//                 {
//                     raise UncloseString(self.text[1:])
//                 }
//                 ;
// ILLEGAL_ESCAPE  : '"' STR_CHAR* ESC_ILLEGAL
//                 {
//                     raise IllegalEscape(self.text[1:])
//                 }
//                 ;
// UNTERMINATED_COMMENT: '**' .*?
//                 {
//                     raise UnterminatedComment()
//                 }
//                 ;
// ERROR_CHAR      : .
//                 {
//                     raise ErrorToken(self.text)
//                 }
//                 ;







/*
 * Tutuarial 2
 */
// //Cau 1:
// //ID: [a-z][a-z0-9]* ;

// //Cau 2:
// fragment LETTER: [a-z] ;
// fragment NUMBER: [0-9] ;
// ID: Letter (NUMBER | LETTER)* ;

// //Cau 3:
// //REAL: [0-9]+ ('.')? [0-9]* [eE]? ('-')? [0-9]+ ;

// REAL: NUMBER+ (
//     ('.' NUMBER+ (('e'|'E') '-'? NUMBER+)?)
//     |
//     (('e'|'E') '-'? NUMBER+)
// )

// //Cau 4:



/*
 * Tutuarial 3
 */
// program: list_dec EOF;
// list_dec: dec list_dec
//         | dec
//         | ;
// dec:  var_declar
//     | function_declar;
// var_declar: type_id listid SM;
// function_declar: type_id ID LP listpara RP LB liststmt RB;
// listid: ID CM listid
//       | ID;
// listpara: var_declar2 SM listpara
//         | var_declar2
//         | ;
// var_declar2: type_id listid;
// type_id: ('int') | ('float');
// liststmt: stmt liststmt
//         | stmt
//         | ;
// stmt: assignment_stmt 
//     | call_stmt
//     | trave_stmt
//     | var_declar;
// assignment_stmt: ID EQ exp SM;
// call_stmt: ID LP listexp RP SM;
// trave_stmt: RETURN exp SM;
// listexp: exp CM listexp
//        | exp
//        | ;
// exp: exp1 ADD exp
//    | exp1;
// exp1: exp2 SUB exp2
//     | exp2;
// exp2: exp2 MUL exp3
//     | exp2 DIV exp3
//     | exp3;
// exp3: INT
//     | FLOAT
//     | ID
//     | call_stmt2
//     | LP exp RP;
// call_stmt2: ID LP listexp RP;

BOOL_LIT        :   TRUE | FALSE ;
WS : [ \t\f\r\n]+ -> skip ; // skip spaces, tabs, newlines

//3.2 COMMENT con thieu block
CMT :   ('**' .*? '**') -> skip ;

//3.3 TOKENS SET
////IDENTIFIERS
ID              :   LOWER (LOWER | UPPER | UNDERSCORES | DIGITS)* ;    

////KEYWORDS
BODY            :   'Body'  ;

BREAK           :   'Break' ;

CONTINUE        :   'Continue' ;

DO              :   'Do' ;

ELSE            :   'Else' ;

ELSEIF          :   'ElseIf' ;

ENDBODY         :   'EndBody' ;

ENDIF           :   'EndIf' ;

ENDFOR          :   'EndFor' ;

ENDDO           :   'EndDo' ;

ENDWHILE        :   'EndWhile' ;

FOR             :   'For' ;

FUNCTION        :   'Function' ;

FALSE           :   'False' ;

IF              :   'If' ;

PARAMETER       :   'Parameter' ;

RETURN          :   'Return' ;

THEN            :   'Then' ;

TRUE            :   'True' ;

WHILE           :   'While' ;

VAR             :   'Var' ;

PRINTLN         :   'printLn';

PRINT           :   'print';

PRINTSTRLN      :   'printStrLn';

READ            :   'read';

////OPERATORS

//INTEGER
ADD             :   '+' ;
SUB             :   '-' ;
MUL             :   '*' ;
DIV             :   '\\' ;
MOD             :   '%' ;
EQ              :   '=' ;
LESS            :   '<' ;
GREATER         :   '>' ;
LESS_EQ         :   '<=' ;
GREATER_EQ      :   '>=' ;
NOT_EQ          :   '!=' ;
EQ_RELATION     :   '==';

//BOOLEAN
NOT             :   '!' ;
AND             :   '&&' ;
OR              :   '||' ;

//FLOAT
F_ADD           :   '+.' ;
F_SUB           :   '-.' ;
F_MUL           :   '*.' ;
F_DIV           :   '\\.' ;
F_LESS          :   '<.' ;
F_GREATER       :   '>.' ;
F_LESS_EQ       :   '<=.' ;
F_GREATER_EQ    :   '>=.' ;
F_NOT_EQ        :   '=/=' ;

////SEPERATORS
LP              :	'(' ;
RP              :	')' ;
LB              :	'{' ;
RB              :	'}' ;
LSB             :	'[' ;
RSB             :	']' ;
COLON           :   ':' ;
CM              :   ',' ;
DOT             :   '.' ;
SM              :   ';' ;

////LITERALS
//INTEGER
INT_HEXA                 : INT_HEX;
INT_OCTO                 : INT_OCT;
INT_DECE                 : INT_DEC;
fragment INT_DEC         :   [1-9] DIGITS* | '0' ;
fragment INT_HEX         :   '0' [xX] [1-9A-F][0-9A-F]* ;
fragment INT_OCT         :   '0' [oO] [1-7][0-7]* ;

//FLOAT
FLOAT_LIT                :  DIGITS+ ((FLOAT_DEC_PART FLOAT_EXP_PART?) | FLOAT_EXP_PART) ;
//fragment FLOAT_INT_PART  :   INT_DEC ;
fragment FLOAT_DEC_PART  :   DOT DIGITS* ;
fragment FLOAT_EXP_PART  :   [eE] (ADD | SUB)? DIGITS+ ;
//BOOLEAN

//ARRAY
//fragment LITERALS        :   INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT | ARRAY_LIT ;
//ARRAY_LIT          :    LP ' '*((LITERALS |ARRAY_LIT) ' '* (COMMA ' '* (LITERALS |ARRAY_LIT)' '*)*)? RP ;
// ARRAY_LIT       :    ARRAY_INT | ARRAY_FLOAT | ARRAY_STRING | ARRAY_ARRAY | ARRAY_BOOL | LP RP ;
// fragment ARRAY_INT          :   LP (' '* INT_LIT ' '* (COMMA ' '* INT_LIT ' '*)*)* RP ;
// fragment ARRAY_FLOAT        :   LP FLOAT_LIT (COMMA FLOAT_LIT)* RP ;
// fragment ARRAY_STRING       :   LP STRING_LIT (COMMA STRING_LIT)* RP ;
// fragment ARRAY_ARRAY        :   LP ARRAY_INT (COMMA ARRAY_INT)*
//                             |   ARRAY_FLOAT (COMMA ARRAY_FLOAT)* 
//                             |   ARRAY_STRING (COMMA ARRAY_STRING)*
//                             |   ARRAY_BOOL (COMMA ARRAY_BOOL)* RP ;
// fragment ARRAY_BOOL         :   LP BOOL_LIT (COMMA BOOL_LIT)* RP ;

//FRAGMENT
fragment LOWER  :   [a-z] ;
fragment UPPER  :   [A-Z] ;
fragment UNDERSCORES    : '_' ;
fragment DIGITS :   [0-9] ;
STRING_LIT  :   '"' (('\'"') | '\\'([bfrnt\\'])| ~(["\n\\]| '\''))* '"'
            {
                self.text = self.text[1:-1]
            }
            ;
ILLEGAL_ESCAPE  :   '"' (('\'"') | '\\'([bfrnt\\'])| ~(["\n\\]| '\''))* ('\\'~[bfrnt'\\] | '\''~'"')
                {
                    raise IllegalEscape(self.text[1:])
                };
UNCLOSE_STRING  :   '"'  (('\'"') | '\\'([bfrnt\\'])| ~(["\n\\]| '\''))* 
                {
                    raise UncloseString(self.text[1:])
                };
ERROR_CHAR      :   .
                {
                    raise ErrorToken(self.text)
                };

UNTERMINATED_COMMENT: '**' .*? 
                {
                    raise UnterminatedComment()
                };
