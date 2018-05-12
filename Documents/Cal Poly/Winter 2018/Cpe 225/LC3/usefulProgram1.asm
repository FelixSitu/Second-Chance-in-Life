; A very useful program.
; CSC 225, Assignment 5

        .ORIG x3000

        ; TODO: Set the Trap Vector Table.

        ; TODO: Set the Interrupt Vector Table.

        ; TODO: Initialize the stack pointer.
        
        LD R1, Trap_26
	LD R2, Memory
        STR R2, R1, #0

	LD R1, Inturp
	LD R2, KB_Inter
	STR R1, R2, #0

	LD R6, ThreeK

MAIN    LEA R0, INITMSG ; Print the starting message.
        PUTS
        TRAP x26        ; Get a character.
        OUT             ; Print the character.
        TRAP x26        ; Repeat four more times.
        OUT
        TRAP x26
        OUT
        TRAP x26
        OUT
        TRAP x26
        OUT
        LEA R0, ENDMSG  ; Print the ending message.
        PUTS
        BRnzp MAIN

INITMSG .STRINGZ "Enter five characters: "
ENDMSG  .STRINGZ "\nSuccess! Running again...\n\n"
Trap_26 .FILL x0026
Memory  .FILL x3300
Inturp  .FILL x3500
KB_Inter .FILL x0180
ThreeK  .FILL x3000

        .END