/*Count number of characters,digits,spaces,tabs,lines and words*/
%{
    #include<stdio.h>
    int c = 0,s = 0,tc = 0 ,lc = 0,sc = 0,wc = 0;
%}

%%
[0-9] {c++;}
\t {tc++;}
\n {lc++;}
[a-zA-Z]+ {wc++;s+=yyleng;}
([ ])+ {sc++;}
. {s++;}
%%

int main()
{
    yyin = fopen("abc.txt","r");
    yylex();
    printf("the no of digits is : %d \n",c);
    printf("the no of characters is : %d \n",s + sc);
    printf("the no of tabs is : %d \n",tc);
    printf("the no of words is : %d \n",wc);
    printf("the no of lines is : %d \n",lc+1);
    printf("the no of spaces is : %d \n",sc);
    fclose(yyin);
    return 0;
}
int yywrap()
{
    return 1;
}
int yyerror()
{
	printf("error");
	exit(0);
}

