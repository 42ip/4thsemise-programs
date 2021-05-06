.global _start

_start:
  Mov R1,#0xA @moving 10 to register 1
  Add R0,R1,#0x14 @adding register 1 with 20 and storing in R0 , gives an exit code of 30
  Mov R7,#1 @moving 1 to R7 indicates syscall exit 
  SWI 0 @software interrupt with exit code 0
