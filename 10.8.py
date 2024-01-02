from datetime import datetime
# Nhập vào ngày, tháng, năm (hợp lệ)
ngay = int(input("Ngày: "))
thang = int(input("Tháng: "))
nam = int(input("Năm: "))

# Xuất ngày theo định dạng ngày - tháng - năm
date = datetime(ngay,thang,nam)
dinh_dang_ngay= date.strftime("%d-%m-%Y")
print("Ngày theo định dạng ngày - tháng - năm:", dinh_dang_ngay)

# Cho biết năm được nhập vào có phải là năm nhuận hay không
nam_nhuan  = (nam,"% 4 == 0 and year % 100 != 0) or (year % 400 == 0")
print("Năm", nam ,"là năm nhuận:",nam_nhuan )

# Cho biết ngày/tháng/năm nhập vào là thứ mấy
ngay = date.strftime("%A")
print("Ngày ",dinh_dang_ngay,"là thứ ",ngay)

# Cho biết tháng nhập vào có bao nhiêu ngày
so_ngay = (date.replace(month=date.month % 12 + 1, day=1) - date).days
print("Tháng",thang,"có ",so_ngay,"ngày.")