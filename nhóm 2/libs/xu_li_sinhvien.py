import csv
def mo_file_danh_sach(_path, lstSinhvien):
    try:
        f=open(_path,'r',encoding='utf-8')
        for dong in csv.reader(f):
            if dong[0]=='ma_sv':
                continue
            lstSinhvien.append({'ma_sv':dong[0],'ten_sv':dong[1],'nam_sinh':dong[2],'gioi_tinh':dong[3],\
                'tbcn':dong[4],'hoc_bong':dong[5]})
        f.close()
        return 1
    except Exception as ex1:
        print('khong mo duoc file hop le', ex1)
        return 0 
#---------------------------End function: mo_file_hoa_don()------------
#hàm lưu ds hóa đơn ra file csv và lưu vào thư mục
def luu_ds_sv(_path,lstSinhvien):
    try:
        f=open(_path,'w',newline='',encoding='utf-8')
        csv.writer(f).writerow(['ma_sv','ten_sv','nam_sinh','gioi_tinh','tbcn','hoc_bong'])
        for hd in lstSinhvien:
            csv.writer(f).writerow(hd['ma_sv'],hd['ten_sv'],hd['nam_sinh'],hd['gioi_tinh'],hd['tbcn'],hd['hoc_bong'])
        f.close()
        return 1
    except Exception as ex1:
        return 0
#------------------------------
def them_sinh_vien(lstSinhvien):
    while True:
        ma_sv=input('nhập mã sinh viên:')
        ten_sv=input('nhập tên sinh viên:')
        nam_sinh=int(input('nhập năm sinh:'))
        gioi_tinh=input('nhập giới tính:')
        tbcn=float(input('nhập điểm trung bình cả năm:'))
        if 7.0 <= tbcn <= 8.0:
           hoc_bong=3000000
        elif tbcn<=9.0:
           hoc_bong=5000000
        elif tbcn >=9.0:
           hoc_bong=8000000
        else:
            hoc_bong=0
        lstSinhvien.append({'ma_sv':ma_sv,'ten_sv':ten_sv,'nam_sinh':nam_sinh,'gioi_tinh':gioi_tinh,'tbcn':tbcn,'hoc_bong':hoc_bong})
        #----------------
        tt=input('bạn có muốn tiếp tục thêm? (1:TT)')
        if tt!='1':
             break
        return
#--------------------------------
def in_ds_sinhvien(lstSinhvien):
    print('{:12}{:12}{:>20}{:>20}{:>20}'.format('ma_sv','ten_sv','nam_sinh','gioi_tinh','tbcn','hoc_bong'))

    for hd in lstSinhvien:
      print('{:12}{:12}{:>20}{:>20}{:>20}'.format(hd['ma_sv'],hd['ten_sv'],hd['nam_sinh'],hd['gioi_tinh'],hd['tbcn'],hd['hoc_bong']))

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
#----------------------------
#sắp xếp sinh viên theo trung bình cả năm
def sapxep(lstSinhvien):
    sort_tbcn=sorted(lstSinhvien, key =lambda x: x['tbcn'])

    return sort_tbcn
#kết thúc mô dun xu_ly sinh vien



                     