  .ORIG x3300 ;Save PC from USE1 into 0x32FF
  
  STI R7, Mem_Loc
  ST R2, SAVER2
  ST R3, SAVER3
  
  ;Enable Beyboard Interrupts
  ;ADD 1 to bit 14 into KBSR/FxE00 (Add 2^14)
  LDI R3, KBSR ;Content inside KBSR
  LD R2, Bit14
  AND R2, R2, R3
  BRp Done
  LD R2, Bit14
  ADD R3, R3, R2
  STI R3, KBSR
Done  LD R7, USE2
  LD R2, SAVER2
  LD R3, SAVER3
  JMP R7 ;JMP to transfer control to Use2
 
 
Mem_Loc .FILL x32FF
Bit14   .FILL x4000
KBSR    .FILL xFE00
SAVER2  .FILL x0000
SAVER3  .FILL X0000
USE2    .FILL x3400

  .END