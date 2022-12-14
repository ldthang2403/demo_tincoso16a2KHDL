from datetime import date
a = int(input("nhập ngày: "))
b = int(input("nhập tháng: "))
c = int(input("nhập năm: "))
def kiem_tra_nam_nhuan(c):
    if (c % 4 == 0 and c % 100 !=0) or (c % 400 == 0):
        print("năm ",c," là năm nhuận")
    else:
        print("năm ",c," không phải năm nhuận")
def kiem_tra_thu(a,b,c):
    d = date(c, b, a)
    print(d)
    e = [0,1,2,3,4,5,6]
    d = d.weekday()
    if d == 6:
        print(a," - ",b," - ",c," là chủ nhật")
    else:
        print(a," - ",b," - ",c, "là thứ: ",e[d]+2)
def kiem_tra_so_ngay_trong_thang(b):
    if (b<=7 and b%2!=0) or (b>7 and b%2==0):
        print("tháng ",b," có 31 ngày")
    elif b == 2:
        print("tháng ",b," có 28 ngày")
    else:
        print("tháng ",b," có 30 ngày")

kiem_tra_nam_nhuan(c)
kiem_tra_thu(a,b,c)
kiem_tra_so_ngay_trong_thang(b)