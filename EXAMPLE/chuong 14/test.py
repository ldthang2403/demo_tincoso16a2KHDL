#bai mau dan
j=[]
for i in range(270,651):
  if ((i%2!=0)):
    j.append(str(i))
print(','.join(j))