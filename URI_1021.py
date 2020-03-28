#-*-coding:utf-8-*-
N = float(input())

n100 = N // 100
rn100 = N % 100

n50 = rn100 // 50
rn50 = rn100 % 50

n20 = rn50 // 20
rn20 = rn50 % 20

n10 = rn20 // 10
rn10 = rn20 % 10

n5 = rn10 // 5
rn5 = rn10 % 5

n2 = rn5 // 2
rn2 = rn5 % 2

m = rn2*100

m100 = m // 100
rm100 = m % 100

m50 = rm100 // 50
rm50 = rm100 % 50

m25 = rm50 // 25
rm25 = rm50 % 25

m10 = rm25 // 10
rm10 = rm25 % 10

m5 = rm10 // 5
rm5 = rm10 % 5

m1 = rm5

print("NOTAS:\n{:.0f} nota(s) de R$ 100.00\n{:.0f} nota(s) de R$ 50.00\n{:.0f} nota(s) de R$ 20.00\n{:.0f} nota(s) de R$ 10.00\n{:.0f} nota(s) de R$ 5.00\n{:.0f} nota(s) de R$ 2.00\nMOEDAS:\n{:.0f} moeda(s) de R$ 1.00\n{:.0f} moeda(s) de R$ 0.50\n{:.0f} moeda(s) de R$ 0.25\n{:.0f} moeda(s) de R$ 0.10\n{:.0f} moeda(s) de R$ 0.05\n{:.0f} moeda(s) de R$ 0.01".format(n100,n50,n20,n10,n5,n2,m100,m50,m25,m10,m5,m1))
