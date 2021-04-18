%{
#include<stdio.h>
#include "y.tab.h"
%}

%%

[0-9]*\.[0-9]+		{yylval.floatval=atof(yytext); return NUMF;}
[0-9]+				{yylval.intval=atoi(yytext); return NUMI;}

sin 	return SIN;   
cos 	return COS;   
tan 	return TAN;       
sqrt 	return SQRT;
log		return LOG;   

[\t ]+
\n				{return 0;}
.				{return yytext[0];}
%%

int yywrap()
{
return 1;
}