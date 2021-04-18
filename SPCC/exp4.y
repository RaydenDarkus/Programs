/*Write YACC program for a Scientific Calculator*/
%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
%}

%union
{
	int intval;
	float floatval;
}

%token <intval> NUMI
%token <floatval> NUMF
%token SIN COS TAN SQRT LOG 
%type <floatval> E
%type <floatval> s
%left '+' '-' 
%left '*' '/'
%left '(' ')'
%%

s:E			{printf("Answer = %.2f\n", $$);};
	
E:E'+'E		 {$$ = $1 + $3;}
|E'-'E		 {$$ = $1 - $3;}
|E'*'E		 {$$ = $1 * $3;}
|E'/'E		{
				if (($3)==0)
				{
					printf("Divided by 0\n");
					exit(0);
				}
				else
					$$=$1/$3;
			}
|'-'E 		 {$$ = -$2;}
|'('E')'	 { $$ = $2; }
|SIN'('E')'  {$$=sin($3);}
|COS'('E')'  {$$=cos($3);}
|TAN'('E')'  {$$=tan($3);}
|LOG'('E')'  {$$=log($3);}
|SQRT'('E')' {$$=sqrt($3);}
|NUMI		 { $$ = $1; }
|NUMF		 { $$ = $1; }
;
		
%%
int main()
{
	printf("Enter expression: \n");
	yyparse();
}

int yyerror()
{
	printf("Syntax error\n");
	exit(0);
}