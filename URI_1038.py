#-*-coding:UTF-8-*-
cod,qtd=input().split()
cod = int(cod)
qtd = int(qtd)
produtos = {1:4.00,2:4.50,3:5.00,4:2.00,5:1.50}
valor = produtos[cod]

total = valor * qtd

print("Total: R$ {:.2f}".format(total))
