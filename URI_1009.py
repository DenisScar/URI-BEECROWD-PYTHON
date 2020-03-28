#-*-coding:UTF-8-*-
nome = input()
salario = float (input())
comissao = float (input())
total = salario + 0.15*comissao
print ("TOTAL = R$ {:.2f}".format(total))
