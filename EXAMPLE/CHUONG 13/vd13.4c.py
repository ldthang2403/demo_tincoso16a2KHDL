f=open('baitho.txt','r',encoding='utf-8')
a=f.readline() #doc 25 ki tu dau tien
print('noi dung dong dau :\n', a)
b=f.readlines() 
print('noi dung dong con lai :\n', b)
c=f.readlines()
print('noi dung cac dong con lai :\n', c)


