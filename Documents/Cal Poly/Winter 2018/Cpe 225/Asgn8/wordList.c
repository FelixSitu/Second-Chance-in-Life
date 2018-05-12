/**
 * CSC 225, Assignment 8
 * Christopher Siu (cesiu@calpoly.edu)
 * Reference sol'n, Winter '18
 */

/* TODO: Included any required libraries. */
#include "wordList.h"
#include <stdio.h>
#include <string.h>
#include <malloc.h>

/**
 * Adds a new occurrence to the end of a list.
 * tail - A pointer to the current tail of a list, NULL if it's empty.
 * line - The line in which the word occurs
 * lineNum - The number of that line within the file
 * wordNum - The position of that word within that line
 *
 * Returns a pointer to the new tail of the list.
 */
Node *addToTail(Node *tail, char *line, int lineNum, int wordNum) {
    /* TODO: Implement this function. */
    /*Condition for if tail is Null = empty => make a node that it points to
        Else: make a node we make that'll it'll point to it next.*/
    if (tail == NULL){
        Node *newtail = (Node *)malloc(sizeof(Node));
        newtail->next = NULL;
        newtail->lineNum = lineNum;
        newtail->wordNum = wordNum;
        strcpy(newtail->line,line);
        return newtail;
    }
    else{
        tail->next = (Node *)malloc(sizeof(Node));
        tail->next->lineNum = lineNum;
        tail->next->wordNum = wordNum;
        strcpy(tail->next->line,line);
        tail->next->next = NULL;
        return tail->next;
    }
}

/**
 * Removes an occurrence from the beginning of a list.
 * head - A pointer to the current head of a list, NULL if it's empty
 * line - A pointer at which to store the removed line
 * lineNum - A pointer at which to store the removed line number
 * wordNum - A pointer at which to store the removed word number
 *
 * Returns a pointer to the new head of the list, NULL if it's (now) empty.
 */
Node *rmFromHead(Node *head, char *line, int *lineNum, int *wordNum) {
    /* TODO: Implement this function. */
    Node *temp;
    if (head == NULL){
        return NULL;
    }
    else{
        *lineNum = head->lineNum;
        *wordNum = head->wordNum;
        strcpy(line,head->line);
        temp = head->next;
        free(head);
        return temp;
    }
}

/**
 * Prints out every node in a list.
 * head - A pointer to the head of a list, NULL if it's empty
 */
void printList(Node *head) {
    /* TODO: Implement this function. */
    
    while (head != NULL){
        printf("Node: \n");
        printf(" - line: ");
        printf("%s\n",head->line);
    
        printf(" - lineNum: ");
        printf("%d\n",head->lineNum);
    
        printf(" - wordNum: ");
        printf("%d\n",head->wordNum);

        head = head->next;
    }
}
