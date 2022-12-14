a = float(input("Nhập cân nậng của bạn(kg): "))
b = float(input("Nhập chiều cao của bạn(m): "))
c = a/(b*b)
print("Chỉ số BMI của bạn là: ",c)
print('Phân loại: ',c)
if c<18.5:
       print("Gày")
elif c<=24.9:
       print("Bình thường")
else:
    print("thừa cân")