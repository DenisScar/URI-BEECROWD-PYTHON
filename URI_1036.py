#-*-coding:UTF-8-*-
A,B,C=input().split()

A = float(A)
B = float(B)
C = float(C)

delta = (B ** 2) - 4 * A * C

if (A == 0) or (delta < 0):
    print("Impossivel calcular")
else:
    R1 = (-B + (delta ** 0.5)) / (2 * A)
    R2 = (-B - (delta ** 0.5)) / (2 * A)
    print("R1 = {:.5f}\nR2 = {:.5f}".format(R1,R2))
