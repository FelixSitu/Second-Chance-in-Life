#include <stdio.h>
#include "stack.h"
/* I have used the helper function: stackDriver to take my functions */

int push(int stack[], int *size, int val){
	/* TODO: Complete this function. */
	
	if (*size >= MAX_SIZE){
	    return 1; 
	} 
	
	stack[*size] = val; 
	
	*size = *size + 1;
	
	return 0;
}

int pop(int stack[], int *size,int *val){
    if (*size <= 0){
        return 1;
    }
    *val = stack[*size-1];
    *size = *size - 1;
    return 0;
    
    }

void printStack(int stack[],int size, int mode){
    if (size == 0){
        printf("[]\n");
    }
    else
    {
        int i;
        if (mode == DEC_MODE){ 
            printf("[");
            for (i=0;i<size;i++){
                
                printf("%d",stack[i]);
                if (i<size-1){
                    printf(",");
                    printf(" ");
                }
            }
            printf("]\n");
        }
        else if (mode == HEX_MODE){ 
            printf("[");
            for (i=0;i<size;i++){
                printf("0x");
                printf("%X",stack[i]);
                if (i<size-1){
                    printf(",");
                    printf(" ");
                }
            }
            printf("]\n");
        }
        else if (mode == CHAR_MODE){ 
            printf("[");
            for (i=0;i<size;i++){
                printf("'");
                printf("%c",stack[i]);
                printf("'");
                if (i<size-1){
                    printf(",");
                    printf(" ");
                }
            }
            printf("]\n");
        }
        
    }
}


