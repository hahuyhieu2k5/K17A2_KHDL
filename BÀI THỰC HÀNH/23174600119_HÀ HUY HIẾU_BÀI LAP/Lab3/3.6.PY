import pandas as pd
stocks1 = pd.read_csv(r'F:\23174600119_HÀ HUY HIẾU\BÀI TẬP THỰC HÀNH\LAB3\stocks1.csv')
stocks2 = pd.read_csv(r'F:\23174600119_HÀ HUY HIẾU\BÀI TẬP THỰC HÀNH\LAB3\stocks2.csv')
stocks = pd.concat([stocks1, stocks2], ignore_index=True)
# 1. Tạo Pivot Table với close trung bình
pivot_table = stocks.pivot_table(
    values='close', 
    index='date', 
    columns='symbol', 
    aggfunc='mean'
)

# 2. Thêm một cột tính tổng volume giao dịch
pivot_table['Total Volume'] = stocks.groupby('symbol')['volume'].sum()

# 3. Sắp xếp Pivot Table dựa trên tổng volume giao dịch
sorted_pivot = pivot_table.sort_values(by='Total Volume', ascending=False)

# 4. Hiển thị 5 mã chứng khoán có tổng volume giao dịch cao nhất
print(sorted_pivot.head())