LW      r1, 12(r0)      // r1 = 4
ADDI    r2, r0, 8       // r2 = 8
SW      r2, 0(r1)       // MEM[4] = 8
LW      r3, 4(r1)       // r3 = 3
BEQ     r3, r2, 16      // r3 = 3, r2 = 8   NO Branch
ADD     r2, r3, r1      // r2 = 7
ADDI    r8, r1, 0       // r8 = 4
LW      r1, 8(r8)       // r1 = 4
MUL     r3, r1, r2      // r3 = 28
BEQ     r1, r8, 8       // r1 = 4, r8 = 4   Branch to ECALL
DIV     r8, r3, r2      // r8 = 4           Not Commited
ADDI    r2, r2, 8       // r2 = 15          Not Commited
ECALL                   // End

.data
1
2
3
4
5
6
