
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def bcnn(a, b):
    return (a * b) // ucln(a, b)
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
ket_qua = bcnn(a, b)
print(f"BCNN của {a} và {b} là: {ket_qua}")
#8.18
def kiem_tra_so_hoan_hao(num):
    tong_uoc = 0
    for i in range(1, num):
        if num % i == 0:
            tong_uoc += i
    return tong_uoc == num
num = int(input("Nhập một số nguyên dương: "))
if kiem_tra_so_hoan_hao(num):
    print(f"{num} là số hoàn hảo.")
else:
    print(f"{num} không phải là số hoàn hảo.")