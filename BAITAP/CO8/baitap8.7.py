def so_kwh(x):
 a = 50*1.678
 b = 50*1.734
 c = 100*2.014
 d = 100*2.536
 e = 100*2.834
 f = (x-400)*2.927
 print("số tiền quý khách phải trả là: ")
 if x <=50:
  print(x*1.678,"đồng")
 elif 50<+x <=100:
  print(a+x*1.734,"đồng")
 elif 100<=x <= 200:
  print(a+b+x*2.014,"đồng")
 elif 200<=x<=300:
  print(a+b+c+x*2.536,"đồng")
 elif 300<=x<=400:
  print(a+b+c+d+x*2.834,"đồng")
 else:
  print(a+b+c+d+e+f,"đồng")
x = input("nhập số so_kwh: ")
x = float(x)
so_kwh(x)