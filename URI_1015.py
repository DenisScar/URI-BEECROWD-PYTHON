#-*-coding:utf-8-*-
x1,y1=input().split()
x1=float(x1)
y1=float(y1)

x2,y2=input().split()
x2=float(x2)
y2=float(y2)

dist = (((x2 - x1)**2) + ((y2 - y1)**2))**.5

print("{:.4f}".format(dist))
