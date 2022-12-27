#quản lý mã sv
import os, csv
import libs.xu_li_sinhvien
#from csv import reader
_path="files/ds_sinhvien.csv"
lstSinhvien=[]
#--------hàm thứ nhất
def read_file():
	with open(_path) as f:
		print(f.read())
#------hàm thứ hai
def luu_ds_sv():
    header=['ma_sv','ten_sv','nam_sinh','gioi_tinh','tbcn','hoc_bong']
    with open(_path,'w') as csvfile:
        writer=csv.DictWriter(csvfile,fieldnames=header)
        writer.writeheader()
        writer.writerows(lstSinhvien)
        
#---hàm thứ ba
def them_sinh_vien(lstSinhvien):
    while True:
        ma_sv=input('nhập mã sinh viên:')
        ten_sv=input('nhập tên sinh viên:')
        nam_sinh=int(input('nhập năm sinh:'))
        gioi_tinh=input('nhập giới tính:')
        tbcn=float(input('nhập điểm trung bình cả năm'))
        if 7.0 <= tbcn <= 8.0:
           hoc_bong=3000000
        elif tbcn<=9.0:
           hoc_bong=5000000
        elif tbcn >=9.0:
           hoc_bong=8000000
        else:
            hoc_bong=0
        lstSinhvien.append({'ma_sv':ma_sv,'ten_sv':ten_sv,'nam_sinh':nam_sinh,\
            'gioi_tinh':gioi_tinh,'tbcn':tbcn,'hoc_bong':hoc_bong})
        #----------------
        tt=input('bạn có muốn tiếp tục thêm? (1:TT):')
        if tt!='1':
             break
        return
#----------------------------
def in_ds_sinhvien(lstSinhvien):
    print('{:12}{:12}{:20}{:>20}{:>20}{:>20}'.format('ma_sv','ten_sv','nam_sinh','gioi_tinh','tbcn','hoc_bong'))

    for hd in lstSinhvien:
      print('{:12}{:12}{:20}{:>20}{:>20}{:>20}'.format(hd['ma_sv'],hd['ten_sv'],hd['nam_sinh'],hd['gioi_tinh'],hd['tbcn'],hd['hoc_bong']))

    return
#----------------------------
# hàm tìm kiếm sinh vien theo mã
def tra_cuu(lstSinhvien, maSV):
    for hd in lstSinhvien:
        if hd['ma_sv']==maSV:
            return hd
    return
#---------------------------hàm xóa theo maSV
def xoa_ten(lstSinhvien, maSV):
    for i in range(len(lstSinhvien)):
        hd=lstSinhvien[i]
        if hd['ma_sv']==maSV:
            del(lstSinhvien[i])
            return 1
    return 0
#sắp xếp danh sách sinh viên 
def sapxep(lstSinhvien):
    sort_tbcn=sorted(lstSinhvien, key =lambda x: x['tbcn'])

    return sort_tbcn
    #------------------------------------
print('CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN')
print('được viết bởi nhóm 2 ngày viết 27-12-2022')
while True:
    print("1: thêm sinh viên")
    print("2: in danh sách sinh viên")
    print("3: tìm sinh viên")
    print("4: xóa sinh viên theo mã sv")
    print("5: thống kê sinh viên theo học bổng")
    print('6: lọc sinh viên theo trung bình cả năm')
    print('7: sinh viên có học bổng cao nhất')
    print('8:luu danh sách sv ra file csv')
    print('9: đọc file csv')
    print('số bất kì: thoát')
    chon = int(input("nhập lựa chọn của bạn:"))
    if chon == 1:
        them_sinh_vien(lstSinhvien)
    elif chon ==2:
        in_ds_sinhvien(lstSinhvien)
    elif chon==3:
        tra_cuu(lstSinhvien)
    elif chon==4:
        xoa_ten(lstSinhvien)
    elif chon==6:
        sapxep(lstSinhvien)
    elif chon==8:
        luu_ds_sv()
    elif chon==9:
        read_file()  
    else:
        break

    tt=input('bạn có muốn tiếp tục(1:TT):')

    if tt!='1':
        break
    else:
        os.system('cls')
    input('gõ phím bất kì để tiếp tục chương trình!!!')