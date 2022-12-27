f=open('baitho.txt','r',encoding='utf-8')
a=f.read(25) #doc 25 ki tu dau tien
print('noi dung 25 ki tu dau tien la :\n', a)
b=f.read(35) 
print('noi dung 35 ki tu tiep theo la :\n', b)
c=f.read()
print('noi dung ki tu con lai la :\n', c)
