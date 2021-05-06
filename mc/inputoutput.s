.global _start

_start:
  Mov R7,#3 @moving to 3 into R7 indicating read syscall
  Mov R0,#0 @moving 0 to R0 
  Mov R2,#11 @moving 10 to R2 as length of max buffer
  LDR R1,=message @moving buffer to R1
  SWI 0

_write:
  Mov R7,#4 @ write syscall
  Mov R0,#1 @ 1 to R0 exit code
  Mov R2,#11 @ lenght of buffer to write
  LDR R1,=message @ loading message to R1
  SWI 0

end:
  Mov R0,#0 @ exit code 0
  Mov R7,#1 @ syscall exit
  SWI 0

.data
message:
  .ascii "\n"
