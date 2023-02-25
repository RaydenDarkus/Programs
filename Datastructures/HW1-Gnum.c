// Shreyas Patil
// G01382371
// CS 531 Assignment 2

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

//Take an array of strings, temporary string in ascending/descending order and string for maximum/minimum ASCII values as GLOBAL variables
char s[10][25],temp[25],max[25],min[25];
int count;

//The function stringcheck() detects invalid characters like ’#’, ’$’, ’%’, ’^’, ‘@’, ’(’, or ’)’ 
//It also checks duplicate string and empty string as well as required length of the string
int stringcheck(char k[]){
    int t = 0;
    if(strlen(k)==0){
        printf("Empty string - please re-enter\n");
        t = 1;
    }
    else{
        if(strlen(k)>1 && strlen(k)<25){
            char q[] = {'#','$','^','@','(',')','%'};
            for(int j=0;j<strlen(q);j++){
                if((strchr(k,q[j]))!= NULL){
                    printf("%c is an illegal character. Please re-enter\n",q[j]);
                    t = 1;
                    break;
                }
            }
            if(count>1){
                for(int i=0;i<count-1;i++){
                    if(strcmp(k,s[i])==0){
                        printf("Duplicate string - please re-enter\n");
                        t = 1;
                        break;
                    }
                }      
            }
        }
        else{
            printf("The string does not have the appropriate length - please re-enter\n");
            t = 1;
        }
    }
    return t;
}

//This function prints the strings with the lowest and the highest ASCII value
void checkmaxmin(char min[],char max[]){
    printf("The string with the lowest ASCII value is: %s\n",min);
    printf("The string with the highest ASCII value is: %s\n",max);
}

//This function is used to input strings
void stringinput(char k[],int i){
    printf("Enter the string %d: ",i);
    fgets(k,50,stdin);
    // int size = strlen(k);
    // k[size-1] = '\0';
    // scanf("%s",k);
}

//Function to print array of strings
void stringprint(char k[][25]){
    for(int i=0;i<10;i++){
        puts(k[i]);
    }
}

//Function for ascending order
void ascending(char k[][25]){
    printf("Ascending Order:\n");
    for(int i=0;i<10;i++){
        for(int j=i+1;j<10;j++){
            if(strcmp(k[i],k[j])>0){
                strcpy(temp,k[i]);
                strcpy(k[i],k[j]);
                strcpy(k[j],temp);
            }        
        }
    }
    stringprint(k);
    strcpy(max,k[9]);
    strcpy(min,k[0]);
    checkmaxmin(min,max);
}

//Function for descending order
void descending(char k[][25]){
    printf("Descending Order:\n");
    for(int i=0;i<10;i++){
        for(int j=i+1;j<10;j++){
            if(strcmp(k[i],k[j])<0){
                strcpy(temp,k[i]);
                strcpy(k[i],k[j]);
                strcpy(k[j],temp);
            }        
        }
    }
    stringprint(k);
    strcpy(max,k[0]);
    strcpy(min,k[9]);
    checkmaxmin(min,max);
}

//Main function calls input and check function as well as asks us to display the array in Ascending/Descending order
int main(){
    char v;
    printf("Enter 10 character strings\n");
    for(int i=0;i<10;i++){
        stringinput(s[i],i);
        count++;
la:     if(stringcheck(s[i]) == 1){
            stringinput(s[i],i);
            goto la;
        }
    }
lb: printf("\nDo you want ascending or descending order or Exit? A or D or E\n");
    scanf("%c",&v);
    if(v == 'A'){
        ascending(s);
        goto lb;
    }
    else if(v == 'D'){
        descending(s);
        goto lb;
    }
    else if(v == 'E'){
        goto ex;
    }
    else{
        printf("Enter the correct input as A or D or E to exit\n");
        goto lb;
    }
ex: return(0);
}

/*
Output:
PS D:\Documents\C Programs> gcc HW1-Gnum.c -o HW1-Gnum
PS D:\Documents\C Programs> ./HW1-Gnum
Enter 10 character strings
Enter the string 0: Test string 1
Enter the string 1: Test string  1
Enter the string 2: hello world
Enter the string 3: CS 531
Enter the string 4: George Mason University
Enter the string 5: abcedfg hijk
Enter the string 6: George Mason University
Duplicate string - please re-enter
Enter the string 6: k j i
Enter the string 7: Test string 2
Enter the string 8: test string @
@ is an illegal character. Please re-enter
Enter the string 8: test String 1
Enter the string 9: test string 1

Do you want ascending or descending order or Exit? A or D or E
A
Ascending Order:
CS 531

George Mason University

Test string  1

Test string 1

Test string 2

abcedfg hijk

hello world

k j i

test String 1

test string 1

The string with the lowest ASCII value is: CS 531

The string with the highest ASCII value is: test string 1


Do you want ascending or descending order or Exit? A or D or E
Enter the correct input as A or D or E to exit
Do you want ascending or descending order or Exit? A or D or E
D
Descending Order:
test string 1

test String 1

k j i

hello world

abcedfg hijk

Test string 2

Test string 1

Test string  1

George Mason University

CS 531

The string with the lowest ASCII value is: CS 531

The string with the highest ASCII value is: test string 1


Do you want ascending or descending order or Exit? A or D or E
Enter the correct input as A or D or E to exit
Do you want ascending or descending order or Exit? A or D or E
E
*/
