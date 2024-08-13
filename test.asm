mvi a, 48h
mvi b, 00h
mvi c, 0ah
lxi h, 2050h

loop: cmp m
jnz next
inr b

next: inx h
dcr c
jnz loop
mov a, b
sta 2080h
hlt