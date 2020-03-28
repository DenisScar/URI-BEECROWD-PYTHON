#-*-coding:utf-8-*-
idade = int(input())

anos = idade // 365
rAnos = idade % 365

meses = rAnos // 30
rMeses = rAnos % 30

dias = rMeses

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(anos,meses,dias))
