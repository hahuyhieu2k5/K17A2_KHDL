a = int(input("nhập số nguyên N: "))

b = 0

for i in range(1, a+1):

    print("nhập số hạng thứ:", i)

    b1 = int(input())

    b = b + b1

print("tổng",a,"số hạng là ", b)