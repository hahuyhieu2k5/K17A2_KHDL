
tong = 0
while True:
    so_nguyen = int(input("Nhập số nguyên (nhập 0 để kết thúc): "))
    if so_nguyen == 0:
        break 
    tong += so_nguyen
print(f"Tổng của các số nguyên là: {tong}")