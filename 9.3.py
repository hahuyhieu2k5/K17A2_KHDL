def bmi(can_nang,chieu_cao):
    bmi = can_nang  / (chieu_cao ** 2)
    if bmi < 18.5:
        return "Gầy"
    elif 18.5 <= bmi <= 24.99:
        return "Bình thường"
    else:
        return "Thừa cân"
#Nhập chiều cao,can nặng
can_n=int(input("Nhập cân nặng:"))
chieu_c= float(input("Nhập chiều cao:"))
print(bmi(can_n,chieu_c))
