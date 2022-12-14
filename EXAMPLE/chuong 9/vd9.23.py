#vi du ham tinh giai thua de qui
def giaithua(n):
    if n==1:
        return 1
    else:
        return (n*giaithua(n-1))
number1=5
number2= int(input("nhap so tien can tinh giai thua:"))
print("giai thu cua", number1, "la", giaithua(number1))
print("gai thua cua", number2, "la", giaithua(number2))

