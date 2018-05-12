#include <stdio.h>
#include "stack.h"

int push(int stack[], int *size, int val){
	/* TODO: Complete this function. */
	//use *size to serve as Stack's integer
	
	if (*size >= MAX_SIZE){
	    printf("\nError: Stack overflow!");
	    return 1; //check if overflow first so that it stops
	} 
	
	//printf("\nWhat number?");
	//scanf("%d",&val);
	
	stack[*size] = val; //Puts the value into stack array
	
	*size = *size + 1;
	
	return 0;
}

int pop(int stack[], int *size,int *val){
    //take stack[current *size] and have *val pointer take the val.
    //then decrement *size
    
    if (*size <= 0){
        printf("\nError: Stack underflow!");
        return 1;
    }
    val = stack[*size-1];
    *size = *size - 1;
    return 0;
    
}

void printStack(int stack[],int size, int mode){
    if (size == 0){
        printf("\n[]");
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
                }
            }
            printf("]");
        }
        else if (mode == HEX_MODE){ 
            printf("[");
            for (i=0;i<size;i++){
                printf("0x");
                printf("%x",stack[i]);
                if (i<size-1){
                    printf(",");
                }
            }
            printf("]");
        }
        else if (mode == CHAR_MODE){ 
            printf("[");
            for (i=0;i<size;i++){
                printf("%c",stack[i]);
                if (i<size-1){
                    printf(",");
                }
            }
            printf("]");
        }
        
    }
}

