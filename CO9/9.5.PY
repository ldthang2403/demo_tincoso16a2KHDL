def A(x,n):
    ham_A=(x**2+x+1)**n + (x**2-x+1)**n
    print("giá trị trả về là:%0.2f"%ham_A)
x=float(input("nhập x:"))
n=float(input("nhập n:"))
A(x,n)