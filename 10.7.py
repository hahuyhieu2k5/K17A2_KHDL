s = "   hello world   "
s_sub = "o"
s_find = "world"
s_replace = "Python"

# In chuỗi s
print("Chuỗi s:", s)

# Loại bỏ khoảng trắng ở đầu và cuối chuỗi
s = s.strip()

# In chuỗi với ký tự đầu chuỗi viết hoa
print("Chuỗi viết hoa:", s.capitalize())

# Đếm và in ra số lần chuỗi con s_sub xuất hiện trong chuỗi s
print("Số lần ",s_sub," xuất hiện trong chuỗi s:", s.count(s_sub))

# Tìm kiếm s_find trong s và thay thế bằng s_replace
s = s.replace(s_find, s_replace)
print("Chuỗi sau khi tìm kiếm và thay thế:", s)
