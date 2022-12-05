LW r1, 12(r0)
ADDI r2, r0, 2
SW r2, 0(r1)
LW r3, 4(r1)
BEQ r3, r2, 16
ADD r2, r3, r1
ADDI r8, r1, 0
MUL r3, r1, r2
BEQ r1, r8, 8
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
