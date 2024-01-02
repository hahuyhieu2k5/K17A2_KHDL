# Tạo tuple a chứa 4 số nguyên dương đầu tiên
a = (1, 2, 3, 4)

# Tạo tuple b chứa 4 số nguyên dương tiếp theo
b = (5, 6, 7, 8)

# Tạo tuple c là sự kết hợp của các phần tử trong tuple a và b
c = a + b

# Tạo tuple d từ tuple c với các phần từ được sắp xếp
d = tuple(sorted(c))

# In phần tử thứ 3 của d
print("Phần tử thứ 3 của d:", d[2])

# In 3 phần tử cuối cùng của d
print("3 phần tử cuối cùng của d:", d[-3:])
