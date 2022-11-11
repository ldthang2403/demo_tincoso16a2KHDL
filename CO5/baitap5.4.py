import math #goi thu vien math các hàm toán
print("nhap so do cac canh tam giac")
a = eval(input('a='))
b = eval(input('b='))
c = eval(input('c='))
P= (a+b+c)/2
S= math.sqrt(P*(P-a)*(P-b)*(P-c))

print("dien tích tam giác ABC là", S)