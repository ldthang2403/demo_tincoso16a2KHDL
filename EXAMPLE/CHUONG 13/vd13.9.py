import csv
def read_csv_file(suu_tam):
    f= open(suu_tam)
    for row in csv.reader(f):
        print(row)
    f.close()
suu_tam=input("ten file csv: ")
read_csv_file(suu_tam)