def so_hoan_hao(x):
    tong_uoc = sum(i for i in range(1, x) if x % i == 0)
    return tong_uoc == x

#Nhập số bất kỳ
a=int(input("Nhập giá trị của a:"))
print(so_hoan_hao(a))  
