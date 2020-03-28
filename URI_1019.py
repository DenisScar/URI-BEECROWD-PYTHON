#-*-coding:utf-8-*-
N = int(input())

h = N // 3600
restoh = N % 3600

m = restoh // 60
restom = restoh % 60

s = restom

print("{}:{}:{}".format(h,m,s))
