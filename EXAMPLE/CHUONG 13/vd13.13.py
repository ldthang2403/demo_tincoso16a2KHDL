from csv import reader
with open('suu_tam22.csv','r') as read_obj:
     csv_reader = reader(read_obj)
     for row in csv_reader:
        print(row)
