ADDI    r1, r0, 0       // r1 = 0
ADDI    r2, r0, 2       // r2 = 2
ADDI    r3, r0, 4       // r3 = 4
ADDI    r4, r0, 1       // r4 = 1
ADD     r1, r1, r2      // r1 += r2
SUB     r3, r3, r4      // r3 -= 1
BEQ     r3, r0, 4       // Se r2 == 0 go to ECALL
BEQ     r0, r0, -20     // Contador 
ECALL                   // End

.data
0
0
0
0