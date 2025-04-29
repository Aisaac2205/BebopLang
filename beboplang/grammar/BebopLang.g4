grammar BebopLang;

programa    : instruccion+ ;
instruccion : iniciar
            | asignacion
            | rastreo
            | captura
            | abandono
            | decision
            | fin ;

iniciar     : 'iniciar' 'misión' ';' ;
asignacion  : 'asignar' ID '=' CADENA ';' ;
rastreo     : 'rastrear' ID ';' ;
captura     : 'capturar' ID ';' ;
abandono    : 'abandonar' 'misión' ';' ;
fin         : 'terminar' 'misión' ';' ;

decision    : 'if' '(' condicion ')' '{' instruccion* '}' ('else' '{' instruccion* '}')? ;
condicion   : ID COMPARADOR NUMERO ;

COMPARADOR  : '>' | '<' | '>=' | '<=' | '==' | '!=' ;
ID          : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMERO      : [0-9]+ ;
CADENA      : '"' (~["\r\n])* '"' ;

WS          : [ \t\r\n]+ -> skip ;
COMENTARIO  : '//' ~[\r\n]* -> skip ;
