#-*-coding:utf-8-*-
cod1,qtd1,valor1=input().split()
cod2,qtd2,valor2=input().split()
cod1 = int(cod1)
qtd1 = int(qtd1)
valor1 = float(valor1)
cod2 = int(cod2)
qtd2 = int(qtd2)
valor2 = float(valor2)
total = (int(qtd1) * float(valor1)) + (int(qtd2) * float(valor2))
print("VALOR A PAGAR: R$ {:.2f}".format(total))
