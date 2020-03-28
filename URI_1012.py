#-*-coding:utf-8-*-
A,B,C=input().split()

A=float(A)
B=float(B)
C=float(C)

tria = A * C / 2
circ = 3.14159 * C**2
trap = (A + B) * C / 2
quad = B**2
reta = A * B

print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(tria,circ,trap,quad,reta))
