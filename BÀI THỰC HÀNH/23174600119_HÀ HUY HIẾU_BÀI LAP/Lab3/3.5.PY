import pandas as pd
stocks1 = pd.read_csv(r'F:\23174600119_HÀ HUY HIẾU\\BÀI TẬP THỰC HÀNH\LAB3\stocks1.csv')
stocks2 = pd.read_csv(r'F:\23174600119_HÀ HUY HIẾUH\\BÀI TẬP THỰC HÀNH\LAB3\stocks2.csv')
stocks = pd.concat([stocks1, stocks2], ignore_index=True)
# 1. Tạo MultiIndex từ cột date và symbol
stocks.set_index(['date', 'symbol'], inplace=True)

# 2. Tính giá trung bình và volume trung bình
grouped = stocks.groupby(['date', 'symbol']).agg({
    'open': 'mean',
    'high': 'mean',
    'low': 'mean',
    'close': 'mean',
    'volume': 'mean'
})

# 3. Sắp xếp dữ liệu theo ngày và mã chứng khoán
sorted_grouped = grouped.sort_index()

# 4. Hiển thị kết quả cho 5 ngày đầu tiên
print(sorted_grouped.head())