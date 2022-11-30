S=0

print("Chương trình tính tổng N số nguyên")

n = int(input("N="))
 
for i in range(1,n+1):
   print("Nhập số nguyên thứ",i,":",end=" ")
   S += int(input())

print("S =",S)