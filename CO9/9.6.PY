def kiem_tra_so_nguyen_to(n):
    #flag = 0 => không phải là số nguyên tố
    #flag = 1 => số nguyên tố
    flag = 1;
    if (n<2):
        flag = False
        return flag #số nhỏ hơn 2 không phải là số nguyên tố nên trả về là 0
    for p in range(2,n):
        if n%p==0:
            flag == True
            break
    return flag
n=int(input("nhập vào số tự nhiên n:"))
kiem_tra=kiem_tra_so_nguyen_to(n);
if kiem_tra == 1:
    print(n,"là số nguyên tố")
else:
    print(n,"không là số nguyên tố")