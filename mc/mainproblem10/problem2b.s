;Assembly program to copy one string from one location to another. this is not in the portion but better to do 
;first before doing the search question
; the result is stored in r0 : 1 is found and 0 is not found
; if found, r1 will give the location in memory
	AREA PROB2A, CODE,READONLY
strbase rn 1
sbase rn 2
loaded rn 3
loaded2 rn 4
cindex rn 5
found rn 0
entry
	ldr strbase,=strsrc
	mov cindex,strbase
	ldr sbase,=ssrc
loop
	ldrb loaded,[cindex] ; increment by one byte
	ldrb loaded2,[sbase]
	cmp loaded2,#0 ; if your search query is found
	beq final
	cmp loaded,#0 ; if end of the line
	beq final
	cmp loaded,loaded2
	addeq cindex,#1
	addeq sbase,#1
	beq loop
	
	ldr sbase,=ssrc
	add strbase,#1
	mov cindex,strbase
	b loop
final 
	cmp loaded2,#0
	moveq found,#1
	movne found,#0
go b go

	area string,DATA,readonly
strsrc DCB "Yo Yo honey singuu zer0 0 herhlo",0 ; we use 0 here for null character
ssrc DCB "Yo",0
base equ 0x40000000
; note that dcb since ascii characters take one byte each
	end