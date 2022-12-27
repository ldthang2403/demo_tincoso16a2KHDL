import csv
def mo_file_hoa_don(_path, lstHoaDon):
    try:
        f=open(_path,'r', encoding ='utf-8')
        for dong in csv.reader(f):
            if dong[0]=='so_hd':
                continue
            lstHoaDon.append({'so_hd':dong[0],'ngay_hd':dong[1], 'ho_tenkh':dong[2],'dia_chi':dong[3],'quan':dong[4],\
            'dien_thoai':dong[5],'tong_tien_hd':dong[6],'tam_ung':dong[7],'con_lai':dong[8]})
        f.close()
        return 1
    except Exception as ex1:
        print('Khong mở được file hop le ', ex1)
        return 0
#---------------------------End function: mo_file_hoa_don()-------------------------------------------------------
def them_hoa_don(lstHoaDon):
    while True:
        so_hd=input('Nhập số hóa đơn: ')
        ngay_hd=input('Ngày hóa đơn: ')
        ho_tenkh=input('Họ tên khách hàng: ')
        dia_chi=input('Địa chỉ khách hàng: ')
        quan=input('Quận : ')
        dien_thoai=input('Điện thoại: ')
        tong_tien_hd=float(input('Tổng tiền hợp đồng: '))
        tam_ung=float(input('Tạm ứng: '))
        con_lai=float(tong_tien_hd-tam_ung)
        lstHoaDon.append({'so_hd':so_hd,'ngay_hd':ngay_hd, 'ho_tenkh':ho_tenkh,'dia_chi':dia_chi,'quan':quan,\
        'dien_thoai':dien_thoai,'tong_tien_hd':tong_tien_hd,'tam_ung':tam_ung,'con_lai':con_lai})
        tt=input('Bạn có muốn tiếp tục thêm ? (1:TT)')
        if tt!='1':
            break
        return
#-------------------------------------------
def in_ds_hoa_don(lstHoaDon):
    print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format('so_hd','ngay_hd', 'ho_tenkh','dia_chi','quan',\
        'dien_thoai','tong_tien_hd','tam_ung','con_lai'))
    
    for hd in lstHoaDon:
        print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format(hd['so_hd'],hd['ngay_hd'], hd['ho_tenkh'],hd['dia_chi'],hd['quan'],\
        hd['dien_thoai'],hd['tong_tien_hd'],hd['tam_ung'],hd['con_lai']))

    return
#------------------------------------------------------------------------------------
#--Hàm tra_cuu_hoa_don() theo số hóa đơn.
def tra_cuu_hoa_don(lstHoaDon,sohd):
    for hd in lstHoaDon:
        if hd['so_hd']==sohd:
            return hd
    return
#----------------Hàm Xóa hóa đơn (xoa_hoa_don()), cho phép xóa hóa đơn theo số hóa đơn
def xoa_hoa_don(lstHoaDon, sohd):
    for i in range(len(lstHoaDon)):
        hd=lstHoaDon[i]
        if hd['so_hd']==sohd:
            del(lstHoaDon[i])
            return 1
    return 0
#----------------Hàm thống kê (thong_ke()), cho phép thống kê tổng tiền, tạm ứng, Tiền còn lại của tất cả hóa đơn.
def thong_ke(lstHoaDon):
    tong=0
    tong_tamung=0
    lstthongke=[]
    for hd in lstHoaDon:
            tong+=float(hd['tong_tien_hd'])
            tong_tamung+=float(hd['tam_ung'])
    tong_conlai=float(tong-tong_tamung)
    print('Tổng tiền tất cả các hóa đơn: %f'%tong)
    print('Tổng tiền tạm ứng tất cả các hóa đơn: %f'%tong_tamung)
    print('Tổng tiền còn lại của tất cả các hóa đơn: %f'%tong_conlai)
    return 
#----------------Hàm Lưu danh sách hóa đơn ra file csv và lưu vào thu mục (luu_file_csv)----------------------------

def luu_ds_hoa_don(_path,lstHoaDon):
    try:
        f=open(_path,'w',newline='', encoding = 'utf-8')
        csv.writer(f).writerow(['so_hd','ngay_hd','ho_tenkh','dia_chi','quan','dien_thoai','tong_tien_hd','tam_ung','con_lai'])
        for hd in lstHoaDon:
            csv.writer(f).writerow([hd['so_hd'],hd['ngay_hd'], hd['ho_tenkh'],hd['dia_chi'],hd['quan'],\
            hd['dien_thoai'],hd['tong_tien_hd'],hd['tam_ung'],hd['con_lai']])
        f.close()
        return 1
    except Exception as ex1:
        return 0
#-----------------------------------Kết thúc mô đun xu_ly_hoa_don.py---------------------------------------------