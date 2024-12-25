import pandas as pd
stocks1 = pd.read_csv(r'F:\23174600119_HÀ HUY HIẾUHIẾU\BÀI TẬP THỰC HÀNH\LAB3\stocks1.csv')
stocks2 = pd.read_csv(r'F:\23174600119_HÀ HUY HIẾU\BÀI TẬP THỰC HÀNH\LAB3\stocks2.csv')
stocks = pd.concat([stocks1, stocks2], ignore_index=True)
# Đọc file companies.csv vào DataFrame
companies = pd.read_csv(r'F:\23174600119_HÀ HUY HIẾU\BÀI TẬP THỰC HÀNH\LAB3\companies.csv')

# 1. Hiển thị 5 dòng đầu tiên của companies
print("\nThông tin tổng quan về companies:")
print(companies.info())

print("\n5 dòng đầu tiên của companies:")
print(companies.head())

# 2. Kết hợp stocks và companies dựa trên cột symbol
merged_data = stocks.merge(companies, left_on='symbol', right_on='name', how='inner')

# 3. Tính giá đóng cửa trung bình cho mỗi công ty
average_close = merged_data.groupby('name')['close'].mean()

# 4. Hiển thị kết quả cho 5 công ty đầu tiên
print(average_close.head())