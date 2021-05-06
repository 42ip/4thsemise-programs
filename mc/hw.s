.global _start

_start:
  Mov R7,#4 @moving 4 to R7 indicating write
  Mov R2,#12  @length of message
  LDR R1,=message @loading message to r1
  swi 0 @software interrupt 0

end:
  Mov R0,#0  @ exit code 0
  Mov R7,#1 @ exit syscall
  swi 0 

.data
message:
  .ascii "Hello World\n"
