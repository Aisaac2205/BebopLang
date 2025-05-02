grammar BebopLang;

programa
    : instruccion+ ;

instruccion
    : iniciar
    | asignacion
    | rastreo
    | captura
    | imprimir
    | entrada
    | decision
    | bucle
    | abandono
    | fin ;

iniciar     : INICIAR MISION PUNTOYCOMA ;
asignacion  : (LET | ASIGNAR) tipo ID '=' valor PUNTOYCOMA ;
rastreo     : RASTREAR ID PUNTOYCOMA ;
captura     : CAPTURAR ID PUNTOYCOMA ;
imprimir    : SPIKE valor PUNTOYCOMA ;
entrada     : ED ID PUNTOYCOMA ;
bucle       : HYPERSPACE '(' condicion ')' '{' instruccion* '}' ;
abandono    : ABANDONAR MISION PUNTOYCOMA ;
fin         : TERMINAR MISION PUNTOYCOMA ;

decision
    : IF '(' condicion ')' '{' instruccion* '}' (ELSE '{' instruccion* '}')? ;

condicion
    : valor COMPARADOR valor ;

tipo
    : JET    
    | FAYE   
    | EIN ;

valor
    : expresion
    | CADENA
    | TRUE
    | FALSE ;

expresion
    : expresion op=('*' | '/' | '^') expresion
    | expresion op=('+' | '-') expresion
    | ID
    | NUMERO
    | '(' expresion ')' ;


// Palabras reservadas
INICIAR     : 'iniciar' ;
MISION      : 'misión' ;
LET         : 'let' ;
ASIGNAR     : 'asignar' ;
JET         : 'jet' ;
FAYE        : 'faye' ;
EIN         : 'ein' ;
SPIKE       : 'spike' ;
ED          : 'ed' ;
RASTREAR    : 'rastrear' ;
CAPTURAR    : 'capturar' ;
HYPERSPACE  : 'hyperspace' ;
ABANDONAR   : 'abandonar' ;
TERMINAR    : 'terminar' ;
IF          : 'if' ;
ELSE        : 'else' ;
TRUE        : 'true' ;
FALSE       : 'false' ;

// Tokens
COMPARADOR  : '>' | '<' | '>=' | '<=' | '==' | '!=' ;
ID          : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMERO      : [0-9]+ ;
CADENA      : '"' (~["\r\n])* '"' ;
PUNTOYCOMA  : ';' ;

// Ignorar espacios y comentarios
WS          : [ \t\r\n]+ -> skip ;
COMENTARIO  : '//' ~[\r\n]* -> skip ;
