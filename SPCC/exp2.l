/*Identify the identifiers,keywords,operators,brackets and count and display them*/
%{
	#include<stdio.h>
    #include <string.h>
    int  opr_count=0,ope_count=0,bracket_count=0,keyword_count=0,x=0,y=0,z=0,c=0,j=0,i=0,p=0;
    char operands[100][100], operators[100][100], stack[100][100] , keywords[100][100];
%}

%%
"{"|"}"|"("|")" {
    bracket_count++;
    strcpy(stack[z], yytext);
    z++ ;
}
"+"|"-"|"*"|"/"|"=" { 
    ope_count++; 
    strcpy(operators[x], yytext); 
    x++; 
} 
("int")|("float")|("char")|("case")|("default")|("if")|("for")|("printf")|("scanf")|("else") {
    keyword_count++;
    strcpy(keywords[p],yytext);
    p++;
}
[a-zA-Z]*|[a-zA-Z0-9_]* { 
    opr_count++; 
    for (i=0;i<y;i++)
    {
        if(strcmp(operands[i],yytext)==0)
        {
            break;
        }
    }
    if(i==y)
        {
            strcpy(operands[y], yytext); 
        }
    y++; 
} 
%%

int main(){
    yyin=fopen("eq.txt","r");
	yylex();
    printf("\nNumber of Brackets is %d",bracket_count);
    printf("\nNumber of identifier is %d",opr_count);
    printf("\nNumber of Keywords is %d",keyword_count);
    printf("\nNumber of operators are %d",ope_count);

    printf("\nOperators are :");
    for(i=0;i<ope_count;i++)
    {
        printf("%s\t",operators[i]);
    }
    printf("\nKeywords are :");
    for(i=0;i<keyword_count;i++)
    {
        printf("%s\t",keywords[i]);
    }
    printf("\nidentifier are :");
    for(j=0;j<opr_count;j++)
    {
        printf("%s\t",operands[j]);
    }
    printf("\n");
    fclose(yyin);
}

int yywrap(){

	return 1;
}

int yyerror(){

	printf("error");
	exit(0);
}