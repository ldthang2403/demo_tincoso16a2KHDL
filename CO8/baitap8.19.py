n=int(input("nhạp số n="))
i=int(1)
day_so=" "
print("nhập dãy số bắt đầu = số 1:")
while i<n:
    i = int(input("i="))
    day_so+=str(i)
kq=" "
for ch in day_so:
    kq=ch+kq
for ch in kq:
    if int(ch)%2 !=0:
        print(ch, end = " ")