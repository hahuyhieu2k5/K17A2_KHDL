# Tạo danh sách các con thú
animals = ['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo']

# In ra danh sách các con thú và số lượng các con thú
print("List of animals:", animals)
print("Number of animals:", len(animals))

# Nhập vào con thú cần tìm
thu_dang_tim = input("\nI want to find:\n")

# Kiểm tra xem con thú có trong danh sách không và in kết quả
if thu_dang_tim in animals:
    print("There is", thu_dang_tim, "in list of animals")
else:
    print("There is no", thu_dang_tim, "in list of animals")

