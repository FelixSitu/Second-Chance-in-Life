#include <stdio.h>
#include "stack.h"

int main()
{
    int size;
    int stack[10];
    int val;
    push(stack,&size,15);
    push(stack,&size,20);
    push(stack,&size,32);
    //pop(stack,&size,val);
    printStack(stack,size, HEX_MODE);
}
