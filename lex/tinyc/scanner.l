%{
#define YYSTYPE char *
#include "y.tab.h"
int cur_line = 1;
void yyerror(const char *msg);
void unrecognized_char(char c);
void unterminate_string();
#define _DUPTEXT {yylval = strdup(yytext);}
%}

OPERATOR        [-/+*%=,;!()<>{}]
INTEGER         [0-9]+
STRING          \"[^\"\n]*\"
UNTERM_STRING   \"[^\"\n]*
IDENTIFIER      [_a-zA-Z][_a-zA-Z0-9]*
WHITESPACE      [ \t\r\a]+
SINGLE_COMMENT1 "//"[^\n]*
SINGLE_COMMENT2 "#"[^\n]*

%%
{OPERATOR}      { return yytext[0]; }
"int"           { return T_Int; }
"void"          { return T_Void; }
"return"        { return T_Return; }
"print"         { return T_Print; }
"readint"       { return T_ReadInt; }
"while"         { return T_While; }
"if"            { return T_If; }
"else"          { return T_Else; }
"break"         { return T_Break; }
"continue"      { return T_Continue; }
"<="            { return T_Le; }
">="            { return T_Ge; }
"=="            { return T_Eq; }
"!="            { return T_Ne; }
"&&"            { return T_And; }
"||"            { return T_Or; }

{INTEGER}       { _DUPTEXT; return T_IntConstant; }
{STRING}        { _DUPTEXT; return T_StringConstant; }
{IDENTIFIER}    { _DUPTEXT; return T_Identifier; }

{WHITESPACE}    { /* ignore every whitespace */ }
{SINGLE_COMMENT1}    { /* ignore every whitespace */ }
{SINGLE_COMMENT2}    { /* ignore every whitespace */ }
\n              { cur_line++; }

{UNTERM_STRING} { unterminate_string(); }
.               { unrecognized_char(yytext[0]); }
%%

int yywrap(void) {
    return 1;
}

void unrecognized_char(char c) {
    char buf[32] = "Unrecognized character: ?";
    buf[24] = c;
    yyerror(buf);
}

void unterminate_string() {
    yyerror("Unterminate string constant");
}

void yyerror(const char *msg) {
    printf("Error at line %d:\n\t%s\n", cur_line, msg);
    exit(1);
}
