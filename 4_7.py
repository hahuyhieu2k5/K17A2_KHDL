n=int(input("Nhập vào số nguyên bất kỳ:"))
tong = 0
while n!=0 :
    r = n % 10
    tong +=r
    n//=10
print("Tổng chữ số vừa nhập là :",tong)
