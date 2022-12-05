ADDI    r1, r0, 0       // r1 = 0
ADDI    r2, r0, 0       // r2 = 0
ADDI    r3, r0, 4       // r3 = 4
SW      r2, 0(r1)       // MEM[r1] = r2
ADDI    r1, r1, 4       // r1 += 4
ADDI    r2, r2, 1       // r2 += 1
BEQ     r3, r2, 4       // Se r2 == r3 go to ECALL
BEQ     r0, r0, -20     // Contador 
ECALL                   // End

.data
0
0
0
0