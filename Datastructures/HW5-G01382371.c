/*Name:Shreyas Patil
Mason ID: G01382371
Assignment No:5*/

#include<stdio.h>
#include<stdlib.h>
#include<signal.h>
#include<fcntl.h>
#include<unistd.h>
#include<sys/stat.h>
#include<sys/wait.h>
#include<sys/types.h>

//Handling of signals
void sig_handler(int signo){
    if(signo==SIGINT)
        printf("Received SIGINT\n");
    if(signo==SIGQUIT)
        printf("Received SIGQUIT\n");
    if(signo==SIGSTOP)
        printf("Received SIGSTOP\n");
    if(signo==SIGKILL)
        printf("Received SIGKILL\n");
}

//User defined function
void udf(char *s,int argc){
    int status=0,pid,i,pdfs[2],j,n=0;
    char buf;
    pipe(pdfs);
    printf("\nPID now = %d, Parent PID now = %d\n",getpid(),getppid());
    pid = fork();
    //Child process is not created
    if(pid==-1){
        perror("fork error");
        exit(EXIT_FAILURE);
    }
    //Child Process
    else if(pid==0){
        printf("Child pid = %d, Parent PID = %d\n",getpid(),getppid());
        if(signal(SIGINT,sig_handler)==SIG_ERR)
            printf("Can't catch SIGINT\n");
        if(signal(SIGQUIT,sig_handler)==SIG_ERR)
            printf("Can't catch SIGQUIT\n");
        if(signal(SIGSTOP,sig_handler)==SIG_ERR)
            printf("Can't catch SIGSTOP\n");
        if(signal(SIGKILL,sig_handler)==SIG_ERR)
            printf("Can't catch SIGKILL\n");
        sleep(10);
        printf("Child pid = %d, Parent PID = %d\n",getpid(),getppid());
        //Redirect the output of this process to the pipe
        close(1); dup(pdfs[1]);
        close(pdfs[0]);
        for(j=0;j<10;j++){
            printf("%d ",n);
            n++;
        }
        exit(EXIT_SUCCESS);
    }
    //Parent Process
    else{
        //Wait process waits till the one child process terminates otherwise the parent process is printed first
        printf("Parent PID now = %d, Parent of Parent PID = %d, Child PID = %d\n",getpid(),getppid(),pid);
        if (wait(&status) >= 0)
            if(WIFEXITED(status))
                // Child process exited normally, through `return` or `exit`
                printf("Child process exited with %d status\n", WEXITSTATUS(status));
        while(1){
            i = waitpid(-1, &status, WNOHANG | WUNTRACED |WCONTINUED);
            if(i==-1)
                break;
            if (i > 0){
                if(WIFEXITED(status))
                    printf("child exited, status = %d\n", WEXITSTATUS(status));
                else if(WIFSTOPPED(status))
                    printf("stopped by signal %d\n", WSTOPSIG(status));
                else if(WIFSIGNALED(status)) 
                    printf("killed by signal %d\n", WTERMSIG(status));
                else if(WIFCONTINUED(status))
                    printf("resumed by signal\n");
                else
                    printf("compilation problem\n");
            }
        }
        //Redirect the output of the previous process while executing the child process as the input of this process
        printf("Demonstration of dup:\n");
        close(0); dup(pdfs[0]);
        for(j=0;j<10;j++){
            scanf("%d",&n);
            printf("n=%d ",n);
            sleep(1);
        }
        printf("\n");
        printf("Demonstration of execlp:\n");
        execlp("ls","ls","-a","-s",NULL);
    }
}

//Main function
int main(int argc, char *argv[]){
    int status;
    if(argc<2)
        return 1;
    udf(argv[1],argc);
    return 0;
}

/*Output
raydendarkus@raydendarkus-IdeaPad-3-15ADA05:/media/raydendarkus/Data/Documents/MS-1st Sem/CS531$ gcc HW5-G01382371.c -o HW5
raydendarkus@raydendarkus-IdeaPad-3-15ADA05:/media/raydendarkus/Data/Documents/MS-1st Sem/CS531$ ./HW5 16

PID now = 79591, Parent PID now = 55325
Parent PID now = 79591, Parent of Parent PID = 55325, Child PID = 79592
Child pid = 79592, Parent PID = 79591
Can't catch SIGSTOP
Can't catch SIGKILL
Child pid = 79592, Parent PID = 79591
Child process exited with 0 status
Demonstration of dup:
n=0 n=1 n=2 n=3 n=4 n=5 n=6 n=7 n=8 n=9 
Demonstration of execlp: 
total 55451
   12  .                                                                           20  .fuse_hidden0000067d00000009              16  HW3.c
    4  ..                                                                          20  .fuse_hidden0000067f0000000a              60  HW3.exe
  140 '0. Install bitvise SSH(1).docx'                                             20  .fuse_hidden000006830000000b              60  HW3.out
   24 '1. Basic UNIX(1) (1).docx'                                                2832  GMU_CS531_Week10_GDB_fork.pptx            40  HW3_rubric.docx
   20 '2. Basic UNIX and vi(1).docx'                                             3636  GMU_CS531_Week11_BinaryFile_Pipe.pptx     16  HW4.c
20120  Advanced.Programming.in.the.UNIX.Environment.3rd.Edition.0321637739.pdf   2256  GMU_CS531_Week12_IPC.pptx                 68  HW4.exe
   60  a.exe                                                                     1796 'GMU_CS531_Week1_Introduction(1).pptx'     64  HW4.out
   20  Bshell.docx                                                               2604  GMU_CS531_Week2_Overview.pptx             20  HW4_rubric.docx
    1  CS531_Inet.txt                                                            2924  GMU_CS531_Week3_Overview2_C.pptx          20  HW5
    1  CS531_Inetv2.txt                                                          1876  GMU_CS531_Week4_Overview3_C.pptx          20  HW5-G01382371
    1  CS531Inetv3.txt                                                           2156  GMU_CS531_Week5_LinkedList.pptx            4  HW5-G01382371.c
   20  .fuse_hidden0000066e00000001                                              2712  GMU_CS531_Week6_byteOrdering.pptx          1  .~lock.GMU_CS531_Week11_BinaryFile_Pipe.pptx#
   20  .fuse_hidden0000066f00000002                                              1908  GMU_CS531_Week7_Recursion.pptx             4  new.c
   20  .fuse_hidden0000067100000003                                              2772 'GMU_CS531_Week8_BST(2).pptx'              56  new.exe
   20  .fuse_hidden0000067200000004                                              2344  GMU_CS531_Week9_Makefile.pptx             56  new.out
   20  .fuse_hidden0000067300000005                                                 1  Hello.txt                                  1  Sample.c
   20  .fuse_hidden0000067900000006                                                12  hw1                                       72  Unix_command_cheatsheet.pdf
   20  .fuse_hidden0000067b00000007                                                 8  HW1-Gnum.c                                 0  .vscode
   20  .fuse_hidden0000067c00000008                                              4416 'HW2-test_scenario(1).pptx'
raydendarkus@raydendarkus-IdeaPad-3-15ADA05:/media/raydendarkus/Data/Documents/MS-1st Sem/CS531$ 
*/

/* During sleep in child process do the following to test WIFSTOPPED(), WIFEXITTED(), WIFSIGNALLED(), WIFCONTINUED()
raydendarkus@raydendarkus-IdeaPad-3-15ADA05:~$ kill -STOP 56328
raydendarkus@raydendarkus-IdeaPad-3-15ADA05:~$ kill -9 56328
raydendarkus@raydendarkus-IdeaPad-3-15ADA05:~$ kill -STOP 56435
raydendarkus@raydendarkus-IdeaPad-3-15ADA05:~$ kill -CONT 56435
raydendarkus@raydendarkus-IdeaPad-3-15ADA05:~$ 
*/