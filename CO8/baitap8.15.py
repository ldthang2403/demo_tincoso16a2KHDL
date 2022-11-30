print("Chương trình tính tổng N số nguyên")
S = 0
a = 1
while a!=0:
    print("Nhập một số nguyên (kết thúc là số 0):",end = " ")
    a = int(input())

    S += a
print("S=",S)