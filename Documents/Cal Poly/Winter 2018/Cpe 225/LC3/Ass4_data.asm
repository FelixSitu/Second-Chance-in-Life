  .ORIG x3500

        ; Question 1
Q1STR   .FILL Q1  ; Address of prompt
Q1PTS   .FILL #10 ; Point value for option 1
        .FILL #5  ; Point value for option 2
        .FILL #0  ; Point value for option 3
        .FILL #2  ; Point value for option 4

        ; Question 2
Q2STR   .FILL Q2
Q2PTS   .FILL #2
        .FILL #10
        .FILL #1
        .FILL #0

        ; Question 3
Q3STR   .FILL Q3
Q3PTS   .FILL #0
        .FILL #5
        .FILL #7
        .FILL #10

        ; Results
RESULTS .FILL GOODMSG
        .FILL PASSMSG
        .FILL FAILMSG

        ; Strings must be declared separately because their lengths are variable.
Q1      .STRINGZ "\nWho is the best anime?\n    1) Corey in the house\n    2) Spongebob\n    3) Berserk (2016)\n    4) Mojojo BA\n"
Q2      .STRINGZ "\nWhat is the most powerful weapon?\n    1) Commusion\n    2) DLC\n    3) SAVE/LOAD\n    4) SALT"
Q3      .STRINGZ "\nWhat is the best trap?\n    1) OUT\n    2) GETC\n    3) PUT\n    4) FELIX\n"

GOODMSG .STRINGZ "GOOD JOB"
PASSMSG .STRINGZ "YOU DIED"
FAILMSG .STRINGZ "GIT GUD S*****"

        .END

;Felix Situ and David Bass