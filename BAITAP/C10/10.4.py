# dùng hàm pow tính A = (x^2 + x + 1)xn + (x^2 - x + 1)^n
x = int(input("nhập x: "))
n = int(input("nhập n: "))
A = pow((pow(x,x)+x+1),n) + pow((pow(x,x) - x + 1),n)
print("giá trị của biểu thức là: ",A)