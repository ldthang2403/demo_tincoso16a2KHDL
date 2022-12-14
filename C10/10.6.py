#giải pt bậc 2
import math as neo
a = int(input("nhập hệ số a: "))
b = int(input("nhập hệ số b: "))
c = int(input("nhập hệ số c: "))
def phuong_trinh_bac_2(a,b,c):
    delta = b**2 - 4*a*c
    if delta == 0:
        x = -b/2*a
        ket_qua = "phương trình có nghiệm kép x = ",x
    elif delta < 0:
        ket_qua = "phuong trình vô nghiệm"
    else:
        x1 = (-b+neo.sqrt(delta)/2*a)
        x2 = (-b-neo.sqrt(delta)/2*a)
        ket_qua = "phuong trình có 2 nghiệm phân biệt ","x1 = ",x1," x2 = ",x2
    return ket_qua
def phuong_trinh_bac_nhat(b,c):
    d = "đây là phương trình bậc nhất có dạng ax + b = 0"
    if b != 0:
        ket_qua = d," nghiệm của pt là: ",-c/b
    else:
        if c == 0:
            ket_qua = d," phương trình có vô số nghiệm"
        else:
            ket_qua = d," phương trình vô nghiệm"
    return ket_qua
if a ==0:
    print(phuong_trinh_bac_nhat(b,c))
else:
    print(phuong_trinh_bac_2(a,b,c))