; Encrypts a given 20 character string
; R0 - The current character
; R1 - Encryption Key
; R2 = 1, a reference check for bit0
; R3 - used to "reverse" bit0 in R0
; R4 - used as an offset for WORD
; R5 - used as a counter for the loop
; R6 - used to check if person presses enter

    .ORIG x3000
    AND R1, R1, #0
    AND R2, R2, #0
    ADD R2, R2, #1
    LD R7, LOADR
    LEA R4, WORD
CLEAR    STR R1, R4, #0
    ADD R4, R4, #1
    ADD R7, R7, #-1
    BRp CLEAR
    
    LEA R4, WORD
    LD R5, LOADR    ;Loop counter for the program

    LEA R0, NUM    ;Puts address of first phrase to R0
    PUTS    ;Writes the first phrase out to console
    GETC    ;Num ascii into R0
    OUT    ;Prints the num inputted
    ADD R1, R1, R0
    ADD R1, R1, #-16
    ADD R1, R1, #-16
    ADD R1, R1, #-16    ;Store num into R1
    
    LEA R0, CHAR    ;Puts address of second phrase to R0
    PUTS    ;Writes the second phrase out to console
LOOP    AND R3, R3, #0
    GETC    ;Takes character ascii into R0
    AND R6, R6, #0
    ADD R6, R6, #-10
    ADD R6, R6, R0    ;Checks if "new line" is entered
    BRz NEXT
    OUT    ;Outputs character to console
    ADD R3, R3, R0    ;Stores the character into R3
    AND R3, R3, R2    ;Checks if bit0 is 0 or 1
    BRp JUMP
    ADD R0, R0, #1    ;Reverses bit0
    BRnzp SKIP
JUMP    ADD R0, R0, #-1    ;Reverses bit0
SKIP    ADD R0, R0, R1    ;Encrypts the character
    STR R0, R4, #0    ;Stores the encrypted character
    ADD R4, R4, #1    ;Add 1 to the WORD offset
    ADD R5, R5, #-1    ;Subtract 1 from the loop counter
    BRp LOOP
        
NEXT    LD R0, NL
    OUT
    LEA R0, MESS
    PUTS    ;Outputs final phrase to console
    LEA R0, WORD
    PUTS    ;Outputs the encrypted phrase to console
    HALT    ;Halt

LOADR    .FILL #20
NL    .STRINGZ "\n"
NUM    .STRINGZ "Enter a number: "    ;Input num phrase
CHAR    .STRINGZ "\nEnter a phrase: "    ;Input String phrase
MESS    .STRINGZ "Encrypted Message: "    ;Output string message
WORD    .BLKW #21    ;Allocates 21 spaces in memory for the user's string
    .END

;David Bass
;Felix Situ