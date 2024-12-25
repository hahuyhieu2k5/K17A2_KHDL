import numpy as np

# Tạo dữ liệu nhiệt độ
temperatures = np.round(np.random.uniform(15, 35, 30), 2)  #Tạo 1 mảng chứa 30 gt nhiệt độ ngẫu nhiên từ 15 đến 30, làm tròn đến 2 chữ số thập phân
print("Nhiệt độ hàng ngày trong tháng:", temperatures)  
print("Nhiệt độ trung bình trong tháng:", np.mean(temperatures)) 

# Xác định xu hướng nhiệt độ
max_temp_day = np.argmax(temperatures) + 1  #Ngày có nhiệt độ cao nhất (+1 để có thể từ ngày 1 đến ngày 30 chứ k phải từ ngày 0 đến 29)
min_temp_day = np.argmin(temperatures) + 1
print(f"Nhiệt độ cao nhất vào ngày {max_temp_day}, thấp nhất vào ngày {min_temp_day}")
   # Ngày có biến đổi độ lớn nhất
temp_diff = np.diff(temperatures)  #np.diff() tính hiệu số giữa hai ngày liên tiếp.
max_diff_day = np.argmax(np.abs(temp_diff)) + 1  #np.abs() lấy giá trị tuyệt đối của hiệu số, rồi dùng np.argmax() để tìm ngày có sự biến đổi lớn nhất
print(f"Ngày có biến đổi nhiệt độ cao nhất là ngày {max_diff_day}")

# Fancy indexing
above_20 = temperatures[temperatures > 20]  #Tạo mảng con gồm các giá trị lớn hơn 20°C
days_5_10_15_20_25 = temperatures[[4, 9, 14, 19, 24]]  #Chọn nhiệt độ ngày 5, 10, 15, 20, 25 bằng chỉ số tương ứng (chỉ số bắt đầu từ 0)
above_avg = temperatures[temperatures > np.mean(temperatures)]  #Chỉ lấy các giá trị lớn hơn nhiệt độ trung bình
even_days = temperatures[1::2] #even_days: Chọn các giá trị ở vị trí ngày chẵn (bắt đầu từ chỉ số 1)
odd_days = temperatures[0::2] #odd_days: Chọn các giá trị ở vị trí ngày lẻ (bắt đầu từ chỉ số 0)

print("Nhiệt độ > 20°C:", above_20)
print("Nhiệt độ ngày 5, 10, 15, 20, 25:", days_5_10_15_20_25)
print("Nhiệt độ trên trung bình:", above_avg)
print("Nhiệt độ ngày chẵn:", even_days)
print("Nhiệt độ ngày lẻ:", odd_days)