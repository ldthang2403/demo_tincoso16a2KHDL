#doc tap tin heights.txt
f= open('heights.txt')
data=f.read()
f.close()

#doi sang list phần tử kiêu chuỗi
lst = data.split(",")

#tạo líst height la các phần tử kiẻue so thuc
height= [float(item) for item in lst]
print(height)

#doi don vi do inch sang met
height_m =[h*0.0254 for h in height]
print(height_m)
 #tinh chieu cao trung binh
mean = sum(height_m)/len(height_m)
print("chieu cao trung binh cac van dong vien la:", round(mean,2))
print("so van đôngj viên được lưu trữ về chiều cao la:", )


