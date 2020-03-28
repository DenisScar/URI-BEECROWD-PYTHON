#-*-coding:utf-8-*-
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

n1 = (a+b+abs(a-b))/2
n2 = int((n1+c+abs(n1-c))/2)

print("{} eh o maior".format(n2))
