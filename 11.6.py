def inch_to_meter(height_inch):
    return height_inch*0.0254
heights=[74,74,72,72,73,69,69,71,76,71]
heights_meters=[inch_to_meter(height) for height in heights]
print("3 CHIỀU CAO ĐẦU TIÊN:",heights_meters[:3])
print("3 CHIỀU CAO CUỐI CÙNG:",heights_meters[-3:])
TB_heights=sum(heights_meters)/len(heights_meters)
print("CHIỀU CAO TRUNG BÌNH:",TB_heights)
max_height=max(heights_meters)
min_height=min(heights_meters)
print("CHIỀU CAO LỚN NHẤT:",max_height)
print("CHIỀU CAO NHỎ NHẤT:",min_height)
heights_meters.sort(reverse=True)
print("SẮP XẾP GIẢM DẦN:",heights_meters)


