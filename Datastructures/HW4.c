// Shreyas Patil
// G01382371
// CS 531 Assignment 4

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

typedef struct address_t{
    int octet[4];
    char alias[10];
    struct address_t *leftchild;
    struct address_t *rightchild;
}address_t;

//global variables
address_t *root = NULL;
int op;
FILE *fp;

//function for checking validity of address
int check(char k[]){
    int o[4],g=0;
    sscanf(k,"%d.%d.%d.%d",&o[0],&o[1],&o[2],&o[3]);
    for(int i=0;i<4;i++){
        if(o[i]<0 || o[i]>255){
            g=-1;
            break;
        }
    }
    return g;
}

//function for checking the length of the alias
int acheck(char k[]){
    int g=0;
    if(strlen(k)<1||strlen(k)>10)
        g = -1;
    return g;
}

//Displays the UDF menu and checks for validity
void menu(){
    printf("1. Add address\n2. Look up address\n3. Update address\n4. Delete address\n5. Display list\n6. Display alias for location\n7. Save to file\n8. Quit\nEnter option: ");
    scanf("%d",&op);
    if(op<1||op>9){
        printf("Invalid option\n");
        menu();
    }
}

//Check if the tree is empty
int empty(){
    if(root==NULL)
        return -1;
    else
        return 0;
}

//Insert a new node and return it and add into the BST
address_t* newNode(int o[],char a[])
{
    address_t* temp = (address_t*)malloc(sizeof(address_t));
    if(temp==NULL)
        return NULL;
    for(int i=0;i<4;i++)
        temp->octet[i]=o[i];
    strcpy(temp->alias,a);
    temp->leftchild = temp->rightchild = NULL;
    return temp;
}

//Displaying the alias with address
void aafind(address_t* k,int o[]){
    if(empty()==-1){
        printf("Empty\n");
        return;
    }
    if(k==NULL){
        return;
    }
    aafind(k->leftchild,o);
    if(k->octet[0]==o[0]&&k->octet[1]==o[1])
        printf("%d\t%s\n",k->octet[3],k->alias);
    aafind(k->rightchild,o);
}

//Find if the address already exists in the tree
address_t* afind(address_t* k,int o[]){
    if(k==NULL)
        return k;
    if(k->octet[0]==o[0]&&k->octet[1]==o[1]&&k->octet[2]==o[2]&&k->octet[3]==o[3])
        return k;
    address_t *temp = afind(k->leftchild,o);
    if(temp!=NULL)
        return temp;
    temp = afind(k->rightchild,o);
    if(temp!=NULL)
        return temp;
    return NULL;
}

//Find if the alias already exists in the tree
int find(char a[]){
    address_t *p=root;
    while(p!=NULL){
        if(strcmp(p->alias,a)==0){
            printf("Alias already exists\n");
            return 1;
        }
        else if(strcmp(p->alias,a)<0)
            p=p->rightchild;
        else
            p=p->leftchild;
    }
    return 0;
}

//Lookup a node in the tree
void lookup(char a[],int b){
    char str[20];
    address_t *p=root;
    if(p==NULL){
        printf("Empty\n");
        return;
    }
    while(p!=NULL){
        if(strcmp(p->alias,a)==0){
            sprintf(str,"%d.%d.%d.%d",p->octet[0],p->octet[1],p->octet[2],p->octet[3]);
            printf("%s: %s\n",a,str);
            b=1;
            break;
        }
        else if(strcmp(p->alias,a)<0)
            p=p->rightchild;
        else
            p=p->leftchild;
    }
    if(b==0)
        printf("\nNot Found\n");
}

//Insert a node into the tree
void add(address_t *k,int o[4],char a1[10]){
    char a[10];
    k = newNode(o,a1);
    if(find(a1)==1)
        return;
    if(afind(root,o)!=NULL){
        printf("Address already exists\n");
        return;
    }
    if(k!=NULL){
        if(root==NULL){
            root=k;
            return;
        }
        address_t *temp=root,*p;
        while(temp!=NULL){
            p=temp;
            if(strcmp(a1,temp->alias)>0)
                temp=temp->rightchild;
            else
                temp=temp->leftchild;
        }
        if(strcmp(a1,p->alias)>0)
            p->rightchild=k;
        else
            p->leftchild=k;
    }  
}

//Read the file ie. create a BST from the data given in the file
void readfile(){
    int ip[4];
    char a[10];
    FILE *fp = fopen("CS531_Inet.txt","r");
    if(fp==NULL){
        fprintf(stderr,"Couldn't open file\n");
        exit(1);
    }
    while(fscanf(fp,"%d.%d.%d.%d %s\n",&ip[0],&ip[1],&ip[2],&ip[3],a)==5){
        address_t *temp=(address_t*)malloc(sizeof(address_t));
        for(int i=0;i<4;i++)
            temp->octet[i]=ip[i];
        strcpy(temp->alias,a);
        temp->rightchild=NULL;
        temp->leftchild=NULL;
        add(temp,temp->octet,temp->alias);
    }
    fclose(fp);
}

//Convert all aliases to lower case as only lower case input is needed
void lower(char k[]){
    for(int i = 0; k[i]!='\0'; i++)
        k[i] = tolower(k[i]);
}

//Update the address of a node in the tree
void update(char a[],int o[]){
    address_t *p=root;
    if(p==NULL){
        printf("Empty\n");
        return;
    }
    while(p!=0){
        if(strcmp(p->alias,a)==0){
            for(int i=0;i<4;i++)
                p->octet[i]=o[i];
            if(afind(root,o)!=NULL){
                printf("Address already exists\n");
                return;
            }
            break;
        }
        else if(strcmp(p->alias,a)<0)
            p=p->rightchild;
        else
            p=p->leftchild;
    }
}

//Display the tree in inorder form
void display(address_t *k){
    int count=0;
    if(empty()==-1)
        return;
    if(k!=NULL){
        char str[20];
        display(k->leftchild);
        sprintf(str,"%d.%d.%d.%d",k->octet[0],k->octet[1],k->octet[2],k->octet[3]);
        printf("%s %s\n",str,k->alias);
        count++; 
        display(k->rightchild);
    }
}

//returns the node with minimum value from the given subtree
address_t* minval(struct address_t* n){
    address_t* p = n;
    while (p && p->leftchild != NULL)
        p = p->leftchild;
    return p;
}

//Delete a node from the tree using an alias
address_t* delete(address_t *k,char a[]){
    address_t *temp;
    if(k==NULL){
        return k;
    }
    if(strcmp(k->alias,a)>0)
        k->leftchild=delete(k->leftchild,a);
    else if(strcmp(k->alias,a)<0)
        k->rightchild=delete(k->rightchild,a);
    else{
        if(k->leftchild==NULL){
            temp = k->rightchild;
            free(k);
            return temp;
        }
        else if(k->rightchild==NULL){
            temp=k->leftchild;
            free(k);
            return temp;
        }
        temp=minval(k->rightchild);
        strcpy(k->alias,temp->alias);
        k->rightchild=delete(k->rightchild,a);
    }
    return k;
}

//Save the tree to a text file and input the filename
void save(address_t *p,char filename[]){
    // if(p==NULL){
    //     printf("Empty\n");
    //     return;
    // }
    if(p!=NULL){
        save(p->leftchild,filename);
        fprintf(fp,"%d.%d.%d.%d %s\n",p->octet[0],p->octet[1],p->octet[2],p->octet[3],p->alias);
        save(p->rightchild,filename);
    }
    // printf("File Saved\n");
}

//Quit the program
void quit(){
    printf("Done\n");
    exit(0);
}

//Main function reads the file and displays user menu, using which further operations can be performed
int main(){
    char a[10],o[16],ch,filename[30];
    int o1[4],o2[4],o3[2],b=0;
    address_t *k,*h,*d;
    readfile();
    while(1)
    {
        menu();
        switch(op)
        {
            case 1:
                while(1){
                    printf("Enter alias: ");
                    scanf("%s",a);
                    lower(a);
                    if(acheck(a)==-1){
                        printf("Invalid alias - Enter again\n");
                        continue;
                    }
p:                  printf("Enter address: ");
                    scanf("%s",o);
                    if(check(o)==-1){
                        printf("Invalid address - Enter again\n");
                        goto p;
                    }
                    break;
                }
                sscanf(o,"%d.%d.%d.%d",&o1[0],&o1[1],&o1[2],&o1[3]);
                add(k,o1,a);
                break;
            case 2:
                while(1){
                    printf("Enter the alias: ");
                    scanf("%s",a);
                    lower(a);
                    if(acheck(a)==-1){
                        printf("Invalid alias - Enter again\n");
                        continue;
                    }
                    else
                        break;
                }
                lookup(a,b);
                break;
            case 3:
                while(1){
                    printf("Enter alias: ");
                    scanf("%s",a);
                    lower(a);
                    if(acheck(a)==-1){
                        printf("Invalid alias - Enter again\n");
                        continue;
                    }
                    for(int i=0;i<4;i++){
m:                      printf("Enter value # %d (0-255): ",i);
                        scanf("%d",&o2[i]);
                        if(o2[i]<0 || o2[i]>255){
                            printf("%d is an illegal entry - please reenter\n",o[i]);
                            goto m;
                        }
                    }
                    break;
                }
                update(a,o2);
                break;
            case 4:
                while(1){
                    printf("Enter the alias: ");
                    scanf("%s",a);
                    lower(a);
                    if(acheck(a)==-1){
                        printf("Invalid alias - Enter again\n");
                        continue;
                    }
                    else
                        break;
                }
                if(find(a)==0){
                    printf("Alias not found\n");
                    break;
                }
                printf("Do you wish to delete the address?(y/n) :");
                scanf(" %c",&ch);
                if(tolower(ch)=='y'){
                    d=delete(root,a);
                    printf("%s is deleted\n",a);
                }
                break;
            case 5:
                display(root);
                break;
            case 6:
                for(int i=0;i<2;i++)
                {
f1:                 printf("Enter location value # i (0-255): ");
                    scanf("%d",&o3[i]);
                    if(o3[i]<0 || o3[i]>255){
                        printf("%d is an illegal entry - please reenter\n",o3[i]);
                        goto f1;
                    }
                }
                aafind(root,o3);
                break;
            case 7:
                printf("Enter file name: ");
                scanf("%s",filename);
                fp = fopen(filename,"w");
                save(root,filename);
                fclose(fp);
                break;
            case 8:
                quit();
                break;
            default:
                fflush(stdin);
                printf("Enter proper option from 1-8\n");
                break;
        }
    }
    return(0);
}

/*CS531_Inet.txt
111.22.3.44 platte
131.250.95.21 jet
172.66.7.88 wabash
111.22.5.66 green
131.250.47.63 baker
83.123.150.205 opal
172.66.7.89 wabash2
*/

/*Output
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 5
131.250.47.63 baker
111.22.5.66 green
131.250.95.21 jet
83.123.150.205 opal
111.22.3.44 platte
172.66.7.88 wabash
172.66.7.89 wabash2
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 6
Enter location value # i (0-255): 131
Enter location value # i (0-255): 250
63      baker
21      jet
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 2
Enter the alias: jet
jet: 131.250.95.21
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 1
Enter alias: 131.250.42.18
Invalid alias - Enter again
Enter alias: barbara
Enter address: 131.250.42.18
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 5
131.250.47.63 baker
131.250.42.18 barbara
111.22.5.66 green
131.250.95.21 jet
83.123.150.205 opal
111.22.3.44 platte
172.66.7.88 wabash
172.66.7.89 wabash2
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 4
Enter the alias: barbara
Alias already exists
Do you wish to delete the address?(y/n) :y
barbara is deleted
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 5
131.250.47.63 baker
111.22.5.66 green
131.250.95.21 jet
83.123.150.205 opal
111.22.3.44 platte
172.66.7.88 wabash
172.66.7.89 wabash2
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 7
Enter file name: CS531Inetv3.txt
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 8
Done
*/

/*CS531Inetv3.txt
131.250.47.63 baker
111.22.5.66 green
131.250.95.21 jet
83.123.150.205 opal
111.22.3.44 platte
172.66.7.88 wabash
172.66.7.89 wabash2
*/