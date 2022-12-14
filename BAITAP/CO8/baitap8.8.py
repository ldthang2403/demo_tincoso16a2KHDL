n = int(input("Nhập loại phòng(từ 1-8):"))
if n == 1:
    a = 1260
if n == 2:
    a = 1550
if n == 3 or 4:
    a = 1830
if n == 5 or 6:
    a = 2120
if n == 7:
    a = 2540
if n == 8:
    a = 4800
b = int(input("Nhập số đêm:"))
if 2 <= b <= 3:
    b*=3/4
if b >= 4:
    b*=0.7

print("Thành tiền:",a*b)