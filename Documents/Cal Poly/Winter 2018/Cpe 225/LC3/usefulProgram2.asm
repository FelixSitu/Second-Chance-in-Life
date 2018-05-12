  .ORIG x3400
  LD R0, Star ;Prints *

Loop AND R1, R1, #0 ;Counter
 
Plus ADD R1, R1, #1
  BRp Plus
  OUT
  BRnzp Loop
  
Star .FILL #42

  .END