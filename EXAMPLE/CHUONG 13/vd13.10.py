import csv
def read_csv_file(suu_tam):
    f= open(suu_tam)
    data=[]
    for row in csv.reader(f):
        data.append(row)
    f.close()
    return data
suu_tam=input("ten file csv: ")
lst=read_csv_file(suu_tam)
print(lst)