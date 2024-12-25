import pandas as pd
stocks1 = pd.read_csv(r'F:\23174600119_HÀ HUY HIẾU\BÀI TẬP THỰC HÀNH\LAB3\stocks1.csv')
# 1. Hiển thị 5 dòng đầu tiên
print("5 dòng đầu tiên của stocks1:")
print(stocks1.head())

# 2. Hiển thị kiểu dữ liệu của mỗi cột
print("\nKiểu dữ liệu của mỗi cột trong stocks1:")
print(stocks1.dtypes)

# 3. Xem thông tin tổng quan
print("\nThông tin tổng quan về stocks1:")
print(stocks1.info())