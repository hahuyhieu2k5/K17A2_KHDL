import pandas as pd
stocks1 = pd.read_csv(r'F:\23174600119_HÀ HUY HIẾU\BÀI TẬP THỰC HÀNH\LAB3\stocks1.csv')
# Kiểm tra dữ liệu Null
print("Kiểm tra dữ liệu Null trong stocks1:")
print(stocks1.isnull().sum())

# Thay thế dữ liệu Null ở cột 'high' bằng giá trị trung bình của cột 'high'
stocks1['high'] = stocks1['high'].fillna(stocks1['high'].mean())

# Thay thế dữ liệu Null ở cột 'low' bằng giá trị trung bình của cột 'low'
stocks1['low'] = stocks1['low'].fillna(stocks1['low'].mean())

# Hiển thị thông tin tổng quan sau khi xử lý dữ liệu Null
print("\nThông tin tổng quan sau khi xử lý dữ liệu Null:")
print(stocks1.info())