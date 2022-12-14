# nhập vào một số nguyên n
n = int(input("Nhập vào số nguyên: ")) 
a = 0
temp = 0
c = 1
d = 1
if n <= 0:
    d = 0
    c = 0
e = 0
f = 0

if n >=0:
    def check_SNT(n):
        flag = True
        # Kiểm tra SNT
        if (n < 2):
            flag = False
        elif (n == 2):
            flag = True
        elif (n % 2 == 0):
            flag = False
        else:
            # Lặp qua các số lẻ nên bắt đầu từ 3 với bước nhảy là 2
            for i in range(3, n, 2):
                if (n % i == 0):
                    flag = False
        return flag
        
    for i in range(1,n+1):
        c*=i
        temp+=i
        if i%2 == 1:
            a += i
        if i%3 == 0:
            d *= i
        if (check_SNT(i)):
            e += i
        if i%2 == 1:
            f+=(1/i)
        else:
            f-=(1/i)

# else:
#    for i in range(n,0):
#         if i%2 == 1:
#             f+=(1/i)
#         else:
#             f-=(1/i)



print("Tổng các số lẻ nhỏ hơn hay bằng n:  ",a)
print("Tổng các số chắn nhỏ hơn hay bằng n:    ",(temp-a))
print("Tích các từ 1 đến n   ",c)
print("Tích các số chia hết cho 3 nhỏ hơn hay bằng n:  ",d)
print("Tổng các số nguyên tố nhỏ hơn bằng n:    ",e)
print("Tổng chuỗi đan dấu:  ",f)