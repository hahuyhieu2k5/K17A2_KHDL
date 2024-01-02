def danh_sach_bua_an(meals):
    """
    Kiểm tra xem có bữa ăn liên tiếp nào nhàm chán hay không.
    
    Parameters:
    - meals: danh sách các bữa ăn
    
    Returns:
    - True nếu có bữa ăn liên tiếp nào nhàm chán, False nếu ngược lại.
    """
    for i in range(1, len(meals)):
        if meals[i] == meals[i - 1]:
            return True
    return False

# Ví dụ 
meals_1 = ['Redneck Ribs', 'Prawn Star', 'San Quentin Squid', 'Fist Full of Pizza', 'Honky Tonk Chicken']
meals_2 = ['Redneck Ribs', 'Prawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']

result_1 = danh_sach_bua_an(meals_1)
result_2 = danh_sach_bua_an(meals_2)

print("Danh sách bữa ăn 1:", meals_1)
print("Có bữa ăn liên tiếp nào nhàm chán hay không:", result_1)

print("\nDanh sách bữa ăn 2:", meals_2)
print("Có bữa ăn liên tiếp nào nhàm chán hay không:", result_2)