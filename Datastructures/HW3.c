// Shreyas Patil
// G01382371
// CS 531 Assignment 3

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// structure declaration
typedef struct address_t{
    int octet[4];
    char alias[11];
    struct address_t *next;
}address_t;

address_t *start = NULL;
int count=-1;
char str[20],str1[20];

//add address to linked list and check for duplicate
void add(char a[],int o[]){
    address_t *n=(address_t *)malloc(sizeof(address_t)),*q=start;
    while(q!=NULL){
        if(q->octet[0]==o[0]&&q->octet[1]==o[1]&&q->octet[2]==o[2]&&q->octet[3]==o[3]){
            sprintf(str1,"%d.%d.%d.%d",q->octet[0],q->octet[1],q->octet[2],q->octet[3]);
            printf("%s already exists\n",str1);
            return;
        }
        if(strcasecmp(q->alias,a)==0){
            printf("%s already exists\n",a);
            return;
        }
        q=q->next;
    }
    strcpy(n->alias,a);
    for(int i=0;i<4;i++)
        n->octet[i]=o[i];
    if(start==NULL){
        start = n;
        start->next = NULL;
    }
    else{
        q = start;
        while(q->next!=NULL)
            q = q->next;
        q->next = n;
        n->next = NULL;
    }
    count++;
}

// update the address by searching the alias in the linked list
void update(char a[],int o[]){
    address_t *t = start;
    if(start==NULL)
        printf("Empty\n");
    else{
        while(t!=NULL){
            if(strcasecmp(t->alias,a)==0){
                printf("Update address for %s: %d.%d.%d.%d\n",a,t->octet[0],t->octet[1],t->octet[2],t->octet[3]);
                address_t *q=start;
                while(q!=NULL){
                    if(q->octet[0]==o[0]&&q->octet[1]==o[1]&&q->octet[2]==o[2]&&q->octet[3]==o[3]){
                        sprintf(str1,"%d.%d.%d.%d",q->octet[0],q->octet[1],q->octet[2],q->octet[3]);
                        printf("%s already exists\n",str1);
                        return;
                    }
                    q=q->next;
                }
                for(int i=0;i<4;i++)
                    t->octet[i]=o[i];
                printf("%s updated\n",t->alias);
                return;
            }
            t=t->next;
        }
    printf("%s does not exist\n",a);
    }
}

// search the alias in the linked list
void lookup(char a[]){
    address_t *t = start;
    if(t==NULL)
        printf("Empty\n");
    else{
        while(t!=NULL){
            if(strcasecmp(t->alias,a)==0)
            {
                sprintf(str,"%d.%d.%d.%d",t->octet[0],t->octet[1],t->octet[2],t->octet[3]);
                break;
            }
            t=t->next;
            strcpy(str,"");
        }
    }
}

// display the linked list and state the total node count
void display(){
    address_t *t = start;
    int i=0;
    if(start==NULL)
        printf("Empty\n");
    else{
        while(t!=NULL){
            char str[20];
            sprintf(str,"%d.%d.%d.%d",t->octet[0],t->octet[1],t->octet[2],t->octet[3]);
            printf("%s %s\n",str,t->alias);
            t=t->next;
            i++;
        }
    }
    printf("Total Node count = %d\n",i);
}

//display all the alias with same location nodes
void adisplay(int o[]){
    address_t *t = start;
    if(start==NULL)
        printf("Empty\n");
    else{
        while(t!=NULL){
            if(t->octet[0]==o[0]&&t->octet[1]==o[1])
                printf("%d\t%s\n",t->octet[3],t->alias);
            t=t->next;
        }
    }
}

// delete a node in the linked list using alias
void delete(char a[]){
    address_t *t = start,*q;
    char ch;
    if(start==NULL){
        printf("Empty\n");
    }
    else{
        while(t!=NULL){
            if(strcasecmp(t->alias,a)==0){
                printf("Delete %s %d.%d.%d.%d (y/n): ",a,t->octet[0],t->octet[1],t->octet[2],t->octet[3]);
                scanf(" %c",&ch);
                printf("\n");
                if(ch=='y'){
                    printf("%s deleted\n",a);
                    if(q==NULL)
                        start=t->next;
                    else
                        q->next=t->next;
                    free(t);
                    return;
                }
                else
                    return;
            }
            q=t;
            t=t->next;
        }
    }
    printf("%s does not exist\n",a);
}

// enter a filename and save to a new text file
void savetofile(char filename[]){
    address_t *t = start;
    if(start==NULL)
        printf("Empty\n");
    else{
        FILE *fp = fopen(filename,"w");
        while(t!=NULL){
            fprintf(fp,"%d.%d.%d.%d %s\n",t->octet[0],t->octet[1],t->octet[2],t->octet[3],t->alias);
            t=t->next;
        }
        fclose(fp);
    }
    printf("File saved\n");
}

//convert string ip address to int and validate it
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

//check if length of alias is less than 10
int acheck(char k[]){
    int g=0;
    if(strlen(k)<1||strlen(k)>10)
        g = -1;
    return g;
}

//The main function reads the file and displays the menu driven part of the code listing the input to be given to the device
int main(){
    FILE *fp;
    fp = fopen("CS531_Inet.txt","r");
    if(fp==NULL){
        fprintf(stderr,"Couldn't open file\n");
        exit(1);
    }
    int ip[5];
    char a3[11];
    while(fscanf(fp,"%d.%d.%d.%d %s\n",&ip[0],&ip[1],&ip[2],&ip[3],a3)==5){
        address_t *temp = (address_t*)malloc(sizeof(address_t));
        for(int i=0;i<4;i++)
            temp->octet[i]=ip[i];
        strcpy(temp->alias,a3);
        temp->next = start;
        start=temp;
    }
    fclose(fp);
    int ch,n1[4],o1[2],o[4];
    char a1[15],a2[30];
p:  printf("1. Add address\n2. Look up address\n3. Update address\n4. Delete address\n5. Display list\n6. Display alias for location\n7. Save to file\n8. Quit\nEnter option: ");
    scanf("%d",&ch);
    switch(ch)
    {
    case 1:
k1:     printf("Enter alias: ");
        scanf("%s",a1);
        if(acheck(a1)== -1){
            printf("Enter again\n");
            goto k1;
        }
k2:     printf("Enter address for %s: ",a1);
        scanf("%s",a2);
        if(check(a2)==-1){
            printf("%s is an illegal address - please reenter\n",a2);
            goto k2;
        }
        sscanf(a2,"%d.%d.%d.%d",&n1[0],&n1[1],&n1[2],&n1[3]);
        add(a1,n1);
        goto p;
    case 2:
p1:     printf("Enter alias: ");
        scanf("%s",a1);
        if(acheck(a1)==-1){
            printf("Enter again\n");
            goto p1;
        }
        lookup(a1);
        if(strlen(str)>1)
            printf("Address for %s: %s\n",a1,str);
        else
            printf("%s does not exist\n",a1);
        goto p;
    case 3:
q1:     printf("Enter alias: ");
        scanf("%s",a1);
        if(acheck(a1)==-1){
            printf("Enter again\n");
            goto q1;
        }
        for(int i=0;i<4;i++){
q2:         printf("Enter value # %d (0-255): ",i);
            scanf("%d",&o[i]);
            if(o[i]<0 || o[i]>255){
                printf("%d is an illegal entry - please reenter\n",o[i]);
                goto q2;
            }
        }
        update(a1,o);
        goto p;
    case 4:
r1:     printf("Enter alias: ");
        scanf("%s",a1);
        if(acheck(a1)==-1){
            printf("Enter again\n");
            goto r1;
        }
        delete(a1);
        goto p;
    case 5:
        display();
        goto p;
    case 6:
        for(int i=0;i<2;i++)
        {
f1:         printf("Enter location value # i (0-255): ");
            scanf("%d",&o1[i]);
            if(o1[i]<0 || o1[i]>255){
                printf("%d is an illegal entry - please reenter\n",o1[i]);
                goto f1;
            }
        }
        adisplay(o1);
        goto p;
    case 7:
        printf("Enter file name: ");
        scanf("%s",a1);
        savetofile(a1);
        goto p;
    case 8:
        printf("Good bye!\n");
        break;
    default:
        printf("Enter proper option from (1-8): ");
        goto p;
    }
    return 0;
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

/*
Output
PS D:\Documents\MasonSem1\CS531> gcc HW3.c -o HW3
PS D:\Documents\MasonSem1\CS531> ./HW3
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 5
172.66.7.89 wabash2
83.123.150.205 opal
131.250.47.63 baker
111.22.5.66 green
172.66.7.88 wabash
131.250.95.21 jet
111.22.3.44 platte
Total Node count = 7
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 1
Enter alias: wabash
Enter address for wabash: 1
wabash already exists
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 1
Enter alias: wabash3
Enter address for wabash3: 172.666.7.90
172.666.7.90 is an illegal address - please reenter
Enter address for wabash3: 172.66.7.90 
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 6
Enter location value # i (0-255): 272
272 is an illegal entry - please reenter
Enter location value # i (0-255): 172
Enter location value # i (0-255): 66
89      wabash2
88      wabash
90      wabash3
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 4
Enter alias: jet2
jet2 does not exist
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 4
Enter alias: jet
Delete jet 131.250.95.21 (y/n): y

jet deleted
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 2
Enter alias: jet
jet does not exist
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 2
Enter alias: cat
cat does not exist
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 2
Enter alias: baker
Address for baker: 131.250.47.63
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 3
Enter alias: baker
Enter value # 0 (0-255): 83
Enter value # 1 (0-255): 123
Enter value # 2 (0-255): 447
447 is an illegal entry - please reenter
Enter value # 2 (0-255): 47
Enter value # 3 (0-255): 63
Update address for baker: 131.250.47.63
baker updated
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 5
172.66.7.89 wabash2
83.123.150.205 opal
83.123.47.63 baker
111.22.5.66 green
172.66.7.88 wabash
111.22.3.44 platte
172.66.7.90 wabash3
Total Node count = 7
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 7
Enter file name: CS531_Inetv2.txt
File saved
1. Add address
2. Look up address
3. Update address
4. Delete address
5. Display list
6. Display alias for location
7. Save to file
8. Quit
Enter option: 8
Good bye!
*/

/*CS531_Inetv2.txt
172.66.7.89 wabash2
83.123.150.205 opal
83.123.47.63 baker
111.22.5.66 green
172.66.7.88 wabash
111.22.3.44 platte
172.66.7.90 wabash3
*/