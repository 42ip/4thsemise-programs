;Assembly program to copy one string from one location to another. this is not in the portion but better to do 
;first before doing the search question
	AREA PROB2A, CODE,READONLY
strbase rn 1
locbase rn 2
loaded rn 3
entry
	ldr strbase,=strsrc
	ldr locbase,=base
loop
	ldrb loaded,[strbase],#1 ; increment by one byte
	strb loaded,[locbase],#1
	cmp loaded,#0
	bne loop
go b go

	area string,DATA,readonly
strsrc DCB "This is a sample string",0 ; we use 0 here for null character
base equ 0x40000000
; note that dcb since ascii characters take one byte each
	end