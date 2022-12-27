try:
    a= int(input("nhap mot so nguyen duong nho hon 100:"))
    if a <=0:
        raise ValueError("ban da nhap mot so qua nho:")
    if a >100:
        raise ValueError("ban can nhap 1 so nho hon 100:")
except ValueError as ex:
    print(ex)