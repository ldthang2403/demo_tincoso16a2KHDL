a = int(input('nhập số phần tử trong zip: '))
b = 0
j = []
for i in range(1,a+1):
    print("nhập phần tử thứ",i)
    c = int(input())
    j.append(c)
    b +=1
print(j)
if b == 6:
    d = True
    print(d)
else:
    d = False
    print(d)