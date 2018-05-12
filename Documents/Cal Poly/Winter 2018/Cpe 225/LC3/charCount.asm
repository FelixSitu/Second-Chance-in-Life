;Felix Situ
;David Bass

      .orig x3300
      ST R0, SAVE0
      ST R1, SAVE1
      ADD R0, R5, #-15
      ADD R0, R0, #-4
      ST R0, COUNT
      
LOOP  ADD R6, R6, #-1 ;Pushing return value
      ADD R6, R6, #-1 ;Pushing return address
      STR R7, R6, #0
      ADD R6, R6, #-1 ;Pushing Dynamic Link
      STR R5, R6, #0
      ADD R6, R6, #-1
      ADD R5, R6, #0  ;Move R5 to base of Locals
      
      LDR R0, R5, #4  ;Load address of str[n] into R0
      LDR R0, R0, #0  ;Puts 'n' into R0
      ADD R0, R0, #0
      BRz RES0
      
      LDR R0, R5, #4
      LDR R0, R0, #0  ;Load 'n' into R0
      LDR R1, R5, #5  ;Load key into R0
      NOT R1, R1
      ADD R1, R1, #1
      ADD R0, R0, R1  ;Compare H with key
      BRz RES1
      
      AND R0, R0, #0
      STR R0, R5, #0
      BRnzp DONE
      
RES1  AND R0, R0, #0
      ADD R0, R0, #1
      STR R0, R5, #0
      
DONE  ADD R6, R6, #-1
      LDR R0, R5, #5  ;Put Key into R0
      STR R0, R6, #0  ;Push key into new stack frame
      ADD R6, R6, #-1
      LD R0, COUNT
      ADD R0, R0, #1
      ST R0, COUNT
      STR R0, R6, #0  ;Store address of new string
      LD R0, NUM
      ADD R0, R0, #1
      ST R0, NUM
      BRnzp LOOP
      
RES0  AND R0, R0, #0
      STR R0, R5, #0  ;Store 0 into result
      
      ADD R6, R6, #1  ;Pop local variables
      LDR R5, R6, #0  ;Popping old dynamic link
      ADD R6, R6, #1
      LDR R7, R6, #0  ;Popping old return address
      ADD R6, R6, #1  ;At new return value
      LDR R0, R6, #-3  ;Get local var result
      STR R0, R6, #0    ;Store result into ret val
      
      ;LD R0, NUM
      ;ADD R0, R0, #-1
      ;ST R0, NUM
      
LOOP2 ADD R6, R6, #3    ;at old local var result
      LDR R0, R6, #0
      LDR R1, R6, #-3
      ADD R0, R0, R1    ;add ret val + old result
      STR R0, R6, #0    ;store result + ret val
      
      ADD R6, R6, #1    ;pop locals
      LDR R5, R6, #0    ;pop dynamic link
      ADD R6, R6, #1
      LDR R7, R6, #0    ;pop ret address
      ADD R6, R6, #1    ;at old ret val
      LDR R0, R6, #-3
      STR R0, R6, #0
      
      LD R0, NUM
      ADD R0, R0, #-1
      ST R0, NUM
      BRp LOOP2         ;do the previous recurse
      
      LD R0, SAVE0
      LD R1, SAVE1
      RET

SAVE0 .FILL x0
SAVE1 .FILL x0
COUNT .FILL x0
NUM   .FILL x0
      .END