def duong_lich_to_amlich(nam):
    # Danh sách Can
    can_list = ["Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm"]

    # Danh sách Chi
    chi_list = ["Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất"]

    # Tính năm Âm lịch
    can = can_list[(nam + 6) % 10]
    chi = chi_list[(nam  + 8) % 12]

    return "{can} {chi}"

# Sử dụng hàm
nam_duong_lich = 2023
nam_am_lich = duong_lich_to_amlich(nam_duong_lich)
print("Năm Dương lịch" ,nam_duong_lich, "chuyển sang Âm lịch là:", nam_am_lich)
