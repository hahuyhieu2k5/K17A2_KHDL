s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")
s3 = input("Nhập chuỗi s3: ")
index = int(input("Nhập chỉ mục index: "))
chieu_dai_s1 = len(s1)
chieu_dai_s2 = len(s2)
chieu_dai_s3 = len(s3)
print(f"Chiều dài của chuỗi s1: {chieu_dai_s1}")
print(f"Chiều dài của chuỗi s2: {chieu_dai_s2}")
print(f"Chiều dài của chuỗi s3: {chieu_dai_s3}")
s4 = s1[index:]
lap_lai_chuoi_s2 = s2 * 2
print(f"Chuỗi con s4 từ index đến hết: {s4}")
print(f"Chuỗi s2 lặp lại 2 lần: {lap_lai_chuoi_s2}")