o_tien = int(input("Nhập số tiền cần đổi (VND): "))
so_tien_500000 = so_tien // 500000
so_tien = so_tien % 500000
so_tien_200000 = so_tien // 200000
so_tien = so_tien % 200000

so_tien_100000 = so_tien // 100000
so_tien = so_tien % 100000

so_tien_50000 = so_tien // 50000
print(f"Số lượng tờ tiền 500000 VND: {so_tien_500000}")
print(f"Số lượng tờ tiền 200000 VND: {so_tien_200000}")
print(f"Số lượng tờ tiền 100000 VND: {so_tien_100000}")
print(f"Số lượng tờ tiền 50000 VND: {so_tien_50000}")