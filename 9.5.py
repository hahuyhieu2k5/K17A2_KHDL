def tinh_a(n, x):
    return (x ** 2 + x + 1) ** n + (x ** 2 - x + 1) ** n

#Nhập giá trị biểu thức
print(tinh_a(3, 2))  # A = (2^2 + 2 + 1)^3 + (2^2 - 2 + 1)^3