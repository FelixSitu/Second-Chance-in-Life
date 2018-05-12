#include <stdio.h>
#include "wordList.h"
#include <malloc.h>
#include <string.h>

/*takes a word and file name as arguments*/

int main(int argc, char **argv){
  
    char line[100];
    FILE *file;

    if (argc != 3){
        printf("%s","myGrep : Improper number of arguments \n");
        printf("Usage: ");
       	printf("%s %s %s\n",argv[0],"<word>","<filename>");
    }
    else{
 	
        file = fopen(argv[2],"r");
        
        if (file == NULL){
        	printf("%s %s\n","myGrep: Unable to open file: ",argv[2]);
        }
        else{
        	char str[100];
        	char *token;
        	int lineNum=0;
        	int wordNum= 0;
        	int charCount=0;
        	int occur = 0;
        	int temp=0;
        	char longline[100];
        	Node *head = (Node*)malloc(sizeof(Node));
        	Node *tail;
        	char temp_line[100];
        	const char filter[20] = {' ', ',', '.', '!'};
        	head->wordNum = -1;
			        	

        	printf("%s %s %s\n",argv[0],argv[1],argv[2]);
        	/*Go through each line, then go through each word per line, fgets*/
        	
        
        	while (fgets(str, sizeof(line), file)){
        		
        		temp = strlen(str);
        		str[temp-2] = '\0';

        		if (charCount < temp){
        			charCount = temp;
        			strcpy(longline,str);
        		}
        		strcpy(temp_line,str);
        		token = strtok(str,filter);
        		while (token!=NULL){
        			wordNum++;
        			if (strcmp(argv[1],token) == 0){
        				occur++;
        				if (head->wordNum == -1){
        					head = addToTail(head,temp_line,lineNum,wordNum);
        					tail = head;
        				}
        				else{
        					tail = addToTail(tail,temp_line,lineNum,wordNum);
        				}
        			}
        			
        			token = strtok(NULL,filter);
        		
        		}
        		wordNum = 0;
        		lineNum++;
        	}

        	

			printf("%s%d %s %s\n","Longest line (",charCount-1, " characters):", longline);
        	printf("%s %d\n","Number of lines: ",lineNum);
        	printf("%s \" %s \": %d\n","Total occurrences of ",argv[1],occur);
        		
        	while (head !=NULL){
        		head = rmFromHead(head,temp_line,&lineNum,&wordNum);
        		if (lineNum!=0){
        			printf("%s %d, %s %d: %s\n","Line",lineNum,"word",wordNum-1,temp_line);
        		}
        	}

        fclose(file);
    	}
    }
    return -1;
    
}