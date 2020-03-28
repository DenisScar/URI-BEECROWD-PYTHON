#-*-coding:utf-8-*-
num = int(input())

ced100 = num // 100
resto100 = num % 100

ced50 = resto100 // 50
resto50 = resto100 % 50

ced20 = resto50 // 20
resto20 = resto50 % 20

ced10 = resto20 // 10
resto10 = resto20 % 10

ced5 = resto10 // 5
resto5 = resto10 % 5

ced2 = resto5 // 2
resto2 = resto5 % 2

ced1 = resto2 // 1

print("{}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00".format(num,ced100,ced50,ced20,ced10,ced5,ced2,ced1))
