# pt bậc nhất có pt ax+b=0
a = int(input('nhap a :'))
b = int(input('nhap b :'))
if a == 0 and b == 0:
     print("pt vo so nghiem")
if a == 0 and b != 0:
     print("pt vo nghiem")
else:
   print("pt có nghiệm duy nhất x= ", -b/a )