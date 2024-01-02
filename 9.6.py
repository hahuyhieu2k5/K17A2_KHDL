def so_nguyen_to(x):
    if x <2:
        return "không là số nguyên tố"
    for i in range(2, int(x**0.5) + 1):#key 
        if x % i == 0:
            return "không là số nguyên tố"
    return "là số nguyên tố"

#Nhập số bất kỳ
a=int(input("Nhập vào số bất kỳ:"))
print(so_nguyen_to(a))