LW r1, 0(r0)
ADDI r2, r0, 4
SW r2, 0(r0)
LW r3, 4(r1)
BEQ r3, r2, 16
ADD r2, r3, r1
MUL r4, r3, r2
DIV r8, r3, r4
ADDI r2, r2, 8
ECALL

.data
1
2
3
4
5
6
