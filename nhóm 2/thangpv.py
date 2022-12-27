''' 
NHÓM SỐ: 01 16A2KHDL
22174600002	VŨ ĐỨC	HIẾU
22174600003	ĐẬU THỊ	THẢO
22174600007	LÊ KHẮC	ĐẠT
22174600008	LÊ THẾ	KHÔI
22174600009	PHẠM THỊ HÀ	NAM
'''
#Quản lý hóa đơn
import os, csv
import libs.xu_ly_hoa_don 
#from csv import reader
_path="files/ds_hoadon.csv"
lstHoaDon=[]
#--------Hàm thứ nhất-----------------------------------------------------
def mo_file_hoa_don(_path,lstHoaDon):
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
    return
#--------Hàm thứ hai---------------------------------------------------
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
#--------Hàm thứ ba-----------------------------------------------------
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
        lstHoaDon.append({'so_hd':so_hd,'ngay_hd':ngay_hd,\
             'ho_tenkh':ho_tenkh,'dia_chi':dia_chi,'quan':quan,\
        'dien_thoai':dien_thoai,'tong_tien_hd':tong_tien_hd,\
            'tam_ung':tam_ung,'con_lai':con_lai})
        #Hết lệnh append    
        tt=input('Bạn có muốn tiếp tục thêm ? (1:TT)')
        if tt!='1':
            break
    return   
#----------------------------------------------------------------------------------
def in_ds_hoa_don(lstHoaDon):
    print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format('so_hd','ngay_hd',\
         'ho_tenkh','dia_chi','quan',\
        'dien_thoai','tong_tien_hd','tam_ung','con_lai'))
    
    for hd in lstHoaDon:
        print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format(hd['so_hd'],\
            hd['ngay_hd'], hd['ho_tenkh'],hd['dia_chi'],hd['quan'],\
        hd['dien_thoai'],hd['tong_tien_hd'],hd['tam_ung'],hd['con_lai']))

    return
#---------------------------------------------------------------------------------
def tra_cuu_hoa_don(lstHoaDon):
    for hd in lstHoaDon:
        if hd['so_hd']==sohd:
            return hd
    return
#-------Hàm thống kê (thong_ke()), cho phép thống kê tổng tiền, tạm ứng, Tiền còn lại của tất cả hóa đơn.
def thong_ke(lstHoadon):
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
def xoa_hoa_don(lstHoaDon):
    for i in range(len(lstHoaDon)):
        hd=lstHoaDon[i]
        if hd['so_hd']==sohd:
            del(lstHoaDon[i])
            return 1
    return 0
#----------------------------------------------------------------------------------
#sắp xếp hóa đơn theo thứ tự giảm dần của tổng tiền hợp đồng
def sapxep(lstHoaDon):
    sorted_doanh_thu = sorted(lstHoaDon, key=lambda x: x['tong_tien_hd'])
    
    return sorted_doanh_thu 
#----------------------------------------------------------------------------------

#------------BẮT ĐẦU CHƯƠNG TRÌNH-------------------------------
print('CHƯƠNG TRÌNH QUẢN LÝ HÓA ĐƠN')
print('Được viết by nhóm .....xyz.....ngày viết......')
while True:
    print('1: Thêm hóa đơn')
    print('2: Danh sách hóa đơn')
    print('3: Tra cứu hóa đơn')
    print('4: Xóa hóa đơn')
    print('5: Thống kê')
    print('6: Sắp xếp')
    print('7: Lưu danh sách hóa đơn ra file CSV')
    print('8: Đọc file CSV')
   
    chon=int(input('Chọn chức năng cần thực hiện: '))
    if chon ==1:
        them_hoa_don(lstHoaDon)
    elif chon==2:
        in_ds_hoa_don(lstHoaDon)
    elif chon==3:
        sohd=input('Nhập số hóa đơn cần tra cứu')
        hd=tra_cuu_hoa_don(lstHoaDon,sohd)
        if hd==None:
            print("Không tra cứu được số hóa đơn %d"%sohd)
        else:
            print(hd)
    elif chon==4:
        sohd=input('Nhập số hóa đơn cần xóa: ')
        kt=input('Bạn có chắc chắn muốn xóa không? (c/C hay k/K?')
        if kt =='c' or kt =='C':
            kq=xoa_hoa_don(lstHoaDon,sohd)
            if kq==1:
                print('Đã xóa hóa đơn số ',sohd)
            else:
                print('Không tồn tại số hóa đơn bạn muốn xóa')
    elif chon==5:
        thong_ke(lstHoaDon)   
   
    elif chon==6:
        print("Danh sách trước khi sắp xếp theo tổng tiền là:",in_ds_hoa_don(lstHoaDon))   
        #sap_xep(lstHoaDon)
        print("Danh sách sau khi sắp xếp theo tổng tiền là:",in_ds_hoa_don(lstHoaDon))     
    elif chon==7:
        if luu_ds_hoa_don(_path, lstHoaDon)==1:
            print('Lưu thành công !')
        else:
            print('Không lưu được !!!')
        luu_ds_hoa_don(_path, lstHoaDon) 
    elif chon==8:
        if mo_file_hoa_don(_path,lstHoaDon):
            print("Đã đọc được file vào lstHoaDon ")
    else:
        break
    
    tt=input('Bạn có muốn tiếp tục (1:tt) ')
    
    if tt!='1':
        break
    else: 
        os.system('cls')
    input('Gõ phím bất kỳ để tiếp tục chương trình !!!')