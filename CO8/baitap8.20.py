import math
x = float(input("Nhập vào giá trị của x="))
Ex = 1
n = 1
t = x
while math.fabs(t)>0.0001:
    Ex += t
    n += 1
    t = t*(x/(float(n)))
print(Ex)