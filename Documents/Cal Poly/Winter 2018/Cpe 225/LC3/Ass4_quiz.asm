; CSC 225, Assignment 4
; David Bass
; Felix Situ

	.ORIG x3000
	AND R2, R2, #0  ; Clears R2
	LDI R0, Q1STR
	PUTS
        JSR RES2
	TRAP x26
	LD R1, Q1PTS
	JSR CALC        ; Outputs Q1 to console and takes user's choice. Adds to total score in R2
		
	LDI R0, Q2STR
	PUTS
	JSR RES2
	TRAP x26
	LD R1, Q2PTS
	JSR CALC        ; Outputs Q2 to console and takes user's choice. Adds to total score in R2
		
	LDI R0, Q3STR
	PUTS
	JSR RES2
	TRAP x26
	LD R1, Q3PTS
	JSR CALC        ; Outputs Q3 to console and takes user's choice. Adds to total score in R2
	
        LEA R0, ANS
        PUTS
	LD R0, RESULTS
	LD R3, HIGH
	ADD R3, R3, R2
	BRzp DONEH      ; Checks if score is >=27
	LD R3, LOW
	ADD R3, R3, R2
	BRnz DONEL      ; Checks if score is =< 20
	LDR R0, R0, #1
	BRnzp DONE
DONEL	LDR R0, R0, #2
        BRnzp DONE
DONEH	LDR R0, R0, #0
DONE    PUTS    ; Outputs final score to console
	HALT

RES2    LEA R0, RES
	ST R7, SAVER7
        PUTS
	LD R7, SAVER7
        RET
	
CALC	ADD R0, R0, #-1
	ADD R0, R1, R0
	LDR R0, R0, #0
	ADD R2, R0, R2
	RET

SAVER7  .FILL #0
HIGH	.FILL #-27
LOW	.FILL #-20
Q1STR	.FILL x3500
Q1PTS	.FILL x3501
Q2STR	.FILL x3505
Q2PTS	.FILL x3506
Q3STR	.FILL x350A
Q3PTS	.FILL x350B
RESULTS	.FILL x350F
RES     .STRINGZ "Answer: "
ANS     .STRINGZ "\nResult: "
	.END