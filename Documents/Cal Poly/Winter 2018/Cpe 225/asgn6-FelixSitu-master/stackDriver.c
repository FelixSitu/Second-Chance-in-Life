#include <stdio.h>
#include "stack.h"
/* I have used the helper function: stackDriver to take my functions */

void stackDriver(int stack[], int *size, int *val, char mode, int first){
    
    char option = 'a';
    
    int number;
    
    if (first == 0){
        printf("Welcome to the stack program.\n");
        first = 1;
    }

    printf("\nEnter option: ");
    
    
    scanf(" %c", &option);
    if (option == 'q'){
        printf("Goodbye!\n");
    }
    else{
        if (option == '+'){
            printf("What number? ");
            scanf("%d",&number);

            if (push(stack,size,number) == 0){
                printf("Stack: ");
                printStack(stack,*size,mode);
            }
            else{
                printf("Error: Stack overflow!\n");
                printf("Stack: ");
                printStack(stack,*size,mode);
            }
        }
        else if (option == '-'){
            if (pop(stack,size,val) == 0){
                printf("Popped ");
                printf("%d",*val);
                printf(".");
            }
            else{
                printf("Error: Stack underflow!");
            }
            printf("\nStack: ");
            printStack(stack,*size,mode);
        }
        else if (option == 'd'){
            printf("Stack: ");
            mode = DEC_MODE;
            printStack(stack,*size,mode);
        }
        else if (option == 'x'){
            printf("Stack: ");
            mode = HEX_MODE;
            printStack(stack,*size,mode);
        }
        else if (option == 'c'){
            printf("Stack: ");
            mode = CHAR_MODE;
            printStack(stack,*size,mode);
        }
        else{
            printf("Stack: ");
            printStack(stack,*size,mode);
        }
        stackDriver(stack,size,val,mode,first);
    }
}


int main()
{
    int size = 0;
    int stack[10];
    int val;
    int first = 0;
    char mode = DEC_MODE;
    
    stackDriver(stack,&size,&val,mode,first);   
    return 0;
}
