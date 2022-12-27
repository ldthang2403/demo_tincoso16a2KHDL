'''
NHÓM 02 DHKL16A2HN
1: 22174600018 NGUYỄN VĂN HÀ
2: 22174600014 NGUYỄN THU THỦY
3: 22174600017 TRẦN TRỌNG CHINH
4: 22174600010 LÊ THỊ LINH PHƯƠNG
5: 22174600015 LƯƠNG ĐỨC THẮNG
'''
import csv
import libs.xu_ly_sinhvien1
listSinhvien = []
file = 'files/ds_sinh-vien.csv'
# hàm thêm sinh viên
def them_sv():
	print("thêm sinh viên: ")
	danh_sach_sv = {
		"ma_sv":'',
		"ten_sv":'',
		'nam_sinh': '',
		'gioi_tinh':'',
		'tbcn': '',
		'hoc_bong':''
		}
	print("nhập mã sinh viên: ")
	id = input()
	while True:
		sv = tim_sv(id)
		if sv != False:
			print('ID này đã tồn tại, nhập 1 ID khác: ')
			id = input()
		else:
			break
	danh_sach_sv['ma_sv'] = id
	# nhập tên
	print("nhập tên sv: ")
	danh_sach_sv["ten_sv"] = input()
	print("nhập năm sinh")
	danh_sach_sv['nam_sinh'] = int(input())
	print("nhập giới tính")
	danh_sach_sv['gioi_tinh'] = input()
	print("nhập điểm trung bình cả năm")
	danh_sach_sv['tbcn'] = float(input())
	a = danh_sach_sv['tbcn']
	if a >= 9.0:
		danh_sach_sv['hoc_bong'] = 8000000
	elif a >=8.0:
		danh_sach_sv['hoc_bong'] = 5000000
	elif a>=7.0:
		danh_sach_sv['hoc_bong'] = 3000000
	else:
		danh_sach_sv['hoc_bong'] = 0	
	listSinhvien.append(danh_sach_sv)
	print(listSinhvien)
# hàm tìm sinh viên theo mã sinh viên
def tim_sv(id):
	for i in range(0,len(listSinhvien)):
		if listSinhvien[i]['ma_sv'] == id:
			return [i, listSinhvien[i]]
	return False
def xoa_sv():
	print("XÓA SINH VIÊN")
	print("nhập ID cần xóa: ")
	id = input()
	student = tim_sv(id)
	if student != False:
		listSinhvien.remove(student[1])
		print("Xóa sinh viên thành công")
	else :
		print("Không tìm thấy sinh viên cần xóa")
# hàm hiển thị danh sách sinh viên
def in_ds_sv():
	print("DANH SÁCH SINH VIÊN HIỆN TẠI: ")
	for i in range(0, len(listSinhvien)):
		print("[",listSinhvien[i]['ma_sv'],"]",
		"[",listSinhvien[i]['ten_sv'],"]",
		listSinhvien[i]['nam_sinh'],"]")
def luu_thong_tin_csv():
	header = ['ma_sv','ten_sv','nam_sinh','gioi_tinh','tbcn','hoc_bong']
	with open(file, 'w') as csvfile:
		writer = csv.DictWriter(csvfile,fieldnames = header)
		writer.writeheader()
		writer.writerows(listSinhvien)
def read_file():
	with open(file) as f:
		print(f.read())
def sapxep():
	print(listSinhvien)
	sap_xep1 = sorted(listSinhvien, key=lambda x: x['hoc_bong'])
	return sap_xep1
def loc_sv_tbcn():
	sap_xep = sorted(listSinhvien, key=lambda x: x['tbcn'])
	return sap_xep
def sv_hoc_bong_max():
	for i in listSinhvien:
		if i['hoc_bong']==max(listSinhvien['hoc_bong']):
			print(i)
while True:
	print("-----------------------------------------------")
	print('-1: Thêm sinh viên                            -')
	print('-2: Danh sách sinh viên                       -')
	print('-3: Tra cứu sinh viên theo mã sv              -')
	print('-4: Xóa sinh viên theo mã sv                  -')
	print('-5: Thống kê sinh viên theo học bổng          -')
	print('-6: lọc sinh viên theo điểm trung bình cả năm -')
	print('-7: Lưu danh sách sinh viên ra file CSV       -')
	print('-8: Đọc file CSV                              -')
	print('-phím bất kì: thoát                           -')
	print('-----------------------------------------------')
	chon=int(input('Chọn chức năng cần thực hiện: '))
	if chon == 1:
		them_sv()
	elif chon == 2:
		in_ds_sv()
	elif chon == 3:
		print("nhập mã sv cần tìm: ")
		a = input()
		print(tim_sv(a))
	elif chon == 4:
		xoa_sv()
	elif chon == 5:
		print(sapxep())
	elif chon == 6:
		print(loc_sv_tbcn())
	elif chon == 7:
		luu_thong_tin_csv()
	elif chon == 8:
		read_file()
	else:
		break