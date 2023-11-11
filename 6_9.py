lai_suat_nam = repr(input("Lãi suất 1 năm (%): "))
so_tien_gui = repr(input("Số tiền gửi (VNĐ): "))
so_thang_gui = int(input("Số tháng gửi: "))
lai_suat_thang = lai_suat_nam/100/12
tien_lai = (so_tien_gui * so_thang_gui) * lai_suat_thang
tong_so_tien = so_tien_gui + tien_lai
print(f"Tiền lãi = {tien_lai:.1f} ")
print(f"Tiền vốn + lãi = {so_tien_gui:.0f} + {tien_lai:.0f} = {tong_so_tien:.0f}")