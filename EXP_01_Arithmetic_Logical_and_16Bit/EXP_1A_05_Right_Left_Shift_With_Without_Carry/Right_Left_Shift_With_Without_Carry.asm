; (i) Right shift with & without carry
ORG 00H
MOV A, #0ACH
RR A
MOV R0, A
CLR C
MOV A, #0ACH
RRC A
MOV R1, A
SETB C
MOV A, #0ACH
RRC A
MOV R2, A
END

; (ii) Left shift with & without carry
ORG 00H
MOV A, #0ACH
RL A
MOV R0, A
CLR C
MOV A, #0ACH
RLC A
MOV R1, A
SETB C
MOV A, #0ACH
RLC A
MOV R2, A
END
